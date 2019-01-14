""" klasa trzymająca dane użytkownika """
""" imię, wiek, masa, wzrost """

import csv

class UserData:
    #def __init__(self, name, age, weight, height):
    def set_parameters(self, name, gender, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

    def write_to_file(self):
        with open('user_data.csv', mode='w', newline="") as csv_file:
            fieldnames = ['name', 'gender', 'age', 'weight', 'height']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'name': self.name, 'gender': self.gender, 'age': self.age, 'weight': self.weight, 'height': self.height})

    def read_from_file(self):
        with open('user_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            header = []
            dict_of_data = {}
            is_something = False
            for row in csv_reader:
                if line_count == 0:
                    for piece_of_data in row:
                        header.append(piece_of_data)
                    line_count += 1
                else:
                    for num in range(0, len(header)):
                        # podaje klucz oraz wartość
                        dict_of_data[header[num]] = row[num]
                    is_something = True
                    line_count += 1

            return dict_of_data, is_something

    def set_params_from_file(self, dict):
        self.name = dict['name']
        self.age = int(dict['age'])
        self.weight = int(dict['weight'])
        self.height = int(dict['height'])
        self.gender = dict['gender']

    def remove_data_from_file(self):
        f = open("user_data.csv", "w")
        f.truncate()
        f.close()



def main():
    usrData = UserData()
    usrData.set_parameters("Piotrek", "male", 21, 82, 185)
    usrData.write_to_file()
    #usrData.remove_data_from_file()
    b = usrData.read_from_file()
    a = 1

if __name__ == "__main__":
    main()