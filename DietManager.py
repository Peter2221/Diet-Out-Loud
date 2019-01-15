from ExcelHandler import ExcelHandler, NoProductException
from UserData import UserData
import datetime
from pathlib import Path
from decimal import Decimal
from run_trybun import *
from FileManager import FileManager


class DietManager:

    eaten_today = 0
    date = 0
    fm = FileManager()

    def calculate_bmi(self, user):
        weight = user.weight
        height = user.height

        bmi = weight/((height/100)**2)
        bmi = round(bmi, 1)
        return bmi

    def calculate_limit(self, user):
        weight = user.weight
        height = user.height
        age = user.age
        gender = user.gender

        if gender == "kobieta":
            daily_need = 9.99*weight+6.25*height-4.92*age-161
        else:
            daily_need = 9.99*weight+6.25*height-4.92*age+5

        daily_need = int(daily_need)
        return daily_need

    def what_you_ate(self, product, product_weight, excel_object, trybun):
        try:
            found_cell = excel_object.find_product(product)
            product = excel_object.produkty[found_cell]
            kcal = excel_object.get_calories(found_cell)
            kcal = int(product_weight/100 * kcal.value)
            trybun.say_something("zjadłeś produkt: " + str(product.value) + " co daje: " + str(kcal) + " kilokalorii")
            return kcal
        except NoProductException as exception:
            print(exception.args[0])

    def is_it_the_next_day(self):
        last_date = self.fm.get_date_from_file()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        if date == last_date:
            return False
        elif last_date is None: # jeśli nie ma daty, wpisz dzisiejszą, czy to ma sens tutaj ? ---------- ???
            self.fm.write_date_to_file(date)
            return False
        else:
            return True

    def what_you_ate_today(self, product, product_weight, excel_object, userData, tribune):
        eaten_now = self.what_you_ate(product, product_weight, excel_object, tribune)
        limit = self.calculate_limit(userData)
        next_day = self.is_it_the_next_day()

        self.fm.add_to_eaten_today(eaten_now)
        eaten_today = self.fm.get_eaten_today()

        if next_day:
            history_file = open("history.txt", "r+")
            eaten_today = self.fm.get_eaten_today()
            date = self.fm.get_date_from_file()
            history_file.write(date + " " + str(eaten_today) + " kcal")
            self.fm.clear_eaten_today()
            new_date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.fm.write_date_to_file(new_date)

        left = limit-eaten_today
        if left > 0:
            tribune.say_something("dzisiaj zjadłeś: " + str(eaten_today) + " kilokalorii, zostało Ci: " + str(left) + " kilokalorii")
        else:
            left = left*(-1)
            tribune.say_something("dzisiaj zjadłeś: " + str(eaten_today) + " kilokalorii, to o " + str(left) + " kilokalorii za dużo! nie jedz już dzisiaj!")


def main():
    exl = ExcelHandler()
    wb = exl.open_workbook("products.xlsx")
    exl.assign_sheets(wb)

    diet = DietManager()
    usrData = UserData()
    usrData.set_parameters("Piotrek", "male", 21, 82, 185)
    usrData.write_to_file()

    print(diet.calculate_bmi(usrData))
    print(diet.calculate_limit(usrData))
    diet.what_you_ate_today("banan", 300, exl, usrData)

if __name__ == "__main__":
    main()

