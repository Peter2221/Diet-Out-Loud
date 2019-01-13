from ExcelHandler import ExcelHandler
from UserData import UserData
import datetime
from pathlib import Path


class DietManager:

    eaten_today = 0
    date = str(datetime.datetime.now())

    def calculate_bmi(self, user):
        weight = user.weight
        height = user.height

        bmi = weight*(height/100)^2
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

        return daily_need

    def what_you_ate(self, product, product_weight, excel_object):
        found_cell = excel_object.find_product(product)
        product = excel_object.produkty[found_cell]
        kcal = excel_object.get_calories(found_cell)
        kcal = product_weight/100 * kcal.value
        print("zjadłeś produkt: " + str(product.value) + " co daje: " + str(kcal) + " kcal")
        self.date = str(datetime.datetime.now())
        return kcal

    def is_it_the_next_day(self): # robocza nazwa
        date = datetime.datetime.now()
        if date == str(self.date()):
            return False
        elif str(self.date) is None:
            return False
        else:
            return True

    def what_you_ate_today(self, product, product_weight, excel_object, user):
        eaten_now = self.what_you_ate(self, product, product_weight, excel_object)
        limit = self.calculate_limit(user)
        if not self.is_it_the_next_day():
            self.eaten_today += eaten_now
        else:
            file = open("history.txt", "w+")
            file.write(str(self.date) + str(self.eaten_today))
            self.eaten_today = eaten_now
            self.date = str(datetime.datetime.now())

        left = limit-eaten_now
        print("dzisiaj zjadłeś: " + self.eaten_today + " kcal, zostało Ci: " + left + " kcal")




