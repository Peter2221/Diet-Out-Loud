from ExcelHandler import ExcelHandler, NoProductException
from UserData import UserData
import datetime
from pathlib import Path
from decimal import Decimal


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

    def what_you_ate(self, product, product_weight, excel_object):
        try:
            found_cell = excel_object.find_product(product)
            product = excel_object.produkty[found_cell]
            kcal = excel_object.get_calories(found_cell)
            kcal = int(product_weight/100 * kcal.value)
            print("zjadłeś produkt: " + str(product.value) + " co daje: " + str(kcal) + " kcal")
            self.date = datetime.datetime.now()
            return kcal
        except NoProductException as exception:
            print(exception.args[0])

    def is_it_the_next_day(self):
        date = datetime.datetime.now()
        if date == self.date:
            return False
        elif self.date is None:
            return False
        else:
            return True

    def what_you_ate_today(self, product, product_weight, excel_object, userData):
        eaten_now = self.what_you_ate(product, product_weight, excel_object)
        limit = self.calculate_limit(userData)
        if not self.is_it_the_next_day():
            self.eaten_today += eaten_now
        else:
            file = open("history.txt", "w+")
            file.write(str(self.date) + str(self.eaten_today))
            self.eaten_today = eaten_now
            self.date = datetime.datetime.now()

        left = limit-eaten_now
        print("dzisiaj zjadłeś: " + str(self.eaten_today) + " kcal, zostało Ci: " + str(left) + " kcal")


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

