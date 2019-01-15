from ExcelHandler import ExcelHandler, NoProductException
from UserData import UserData
import datetime
from pathlib import Path
from decimal import Decimal
from run_trybun import *


class DietManager:

    eaten_today = 0
    date = datetime.datetime.now()


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

    def delete_content(self, file):
        with open(file, "w"):
            pass

    def get_date_from_file(self):
        file = open('date.csv', 'r+')
        last_date = file.read()
        file.close()
        return last_date

    def add_to_eaten_today(self, eaten_now):
        eaten_file = open("eaten.csv")
        eaten_today = int(eaten_file.read())
        eaten_today += eaten_now
        self.delete_content(eaten_file)
        eaten_file.write(str(eaten_today))
        eaten_file.close()

    def get_eaten_today(self):
        eaten_file = open("eaten.csv")
        eaten_today = int(eaten_file.read())
        eaten_file.close()
        return eaten_today

    def what_you_ate(self, product, product_weight, excel_object):
        try:
            found_cell = excel_object.find_product(product)
            product = excel_object.produkty[found_cell]
            kcal = excel_object.get_calories(found_cell)
            kcal = int(product_weight/100 * kcal.value)
            print("zjadłeś produkt: " + str(product.value) + " co daje: " + str(kcal) + " kcal")
            return kcal
        except NoProductException as exception:
            print(exception.args[0])

    def is_it_the_next_day(self):
        last_date = self.get_date_from_file()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        if date == last_date:
            return False
        elif last_date is None: # ???? nie wiem czy teraz ma sens
            return False
        else:
            return True

    def what_you_ate_today(self, product, product_weight, excel_object, userData, tribune):
        eaten_now = self.what_you_ate(product, product_weight, excel_object)
        limit = self.calculate_limit(userData)

        if not self.is_it_the_next_day():
            self.add_to_eaten_today(eaten_now)
            eaten_today = self.get_eaten_today()
        else:
            history_file = open("history.txt", "w+")
            eaten_today = self.get_eaten_today()
            date = self.get_date_from_file()
            history_file.write(date + str(eaten_today) + " kcal")
            self.delete_content("eaten_file.csv")
            self.delete_content("date.csv")

        left = limit-eaten_now
        if left > 0:
            tribune.say_something("dzisiaj zjadłeś: " + str(eaten_today) + " kcal, zostało Ci: " + str(left) + " kilokalorii")
        else:
            left = left*(-1)
            tribune.say_something("dzisiaj zjadłeś: " + str(eaten_today) + " kcal, to o " + str(left) + " kilokalorii za dużo! nie jedz już dzisiaj!")


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

