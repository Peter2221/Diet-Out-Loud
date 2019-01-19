import datetime

class FileManager:

    def write_date_to_file(self, date, file):
        f = open(file, "w")
        f.write(date)

    def get_date_from_file(self, datefile):
        file = open(datefile, 'r+')
        last_date = file.read()
        file.close()
        return last_date

    def get_eaten_today(self):
        eaten_file = open("eaten.txt", 'r+')
        eaten_today = int(eaten_file.read())
        eaten_file.close()
        return eaten_today

    def clear_eaten_today(self):
        eaten_file = open("eaten.txt", 'w')
        eaten_file.write(str(0))

    def add_to_eaten_today(self, eaten_now):
        eaten_today = self.get_eaten_today()
        eaten_today += eaten_now
        eaten_file = open("eaten.txt", "w")
        eaten_file.write(str(eaten_today))
        eaten_file.close()

    def write_yesterday_to_history(self):
        history_file = open("history.txt", "a")
        eaten_yesterday = self.get_eaten_today()
        date = self.get_date_from_file("date.txt")
        history_file.write('\n' + date + " " + str(eaten_yesterday) + " kcal") # tutaj wpisze się do historii
        self.clear_eaten_today() # tu wyzeruje plik z kaloriami z dzisiaj
        new_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.write_date_to_file(new_date, "date.txt")



# fm = FileManager()
# date = fm.get_date_from_file()
# print(date)
# date_today = datetime.datetime.now().strftime("%Y-%m-%d")
# print(date_today)
# fm.write_date_to_file("2019-01-02")
# new_date = fm.get_date_from_file()
# print(new_date)
#
# eaten = fm.get_eaten_today()
# print(eaten)
# new = 300
# fm.add_to_eaten_today(new)
# new_eaten = fm.get_eaten_today()
# print(new_eaten)