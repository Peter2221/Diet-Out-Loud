from openpyxl import load_workbook
from xlsxwriter.utility import xl_rowcol_to_cell

class ExcelHandler():
<<<<<<< HEAD

=======
    kalorie = []
>>>>>>> 6c36d2cae228c62d65c7bbfadd823cf065246482
    produkty = []
    kalorie = []

    def open_workbook(self, filename):
        wb = load_workbook(filename, data_only=True)  # wybieramy plik
        return wb

    #nie jestem pewna czy ta funkcja jest potrzebna ale napisałam :3
    def assign_sheets(self, wb):
        self.produkty = wb["produkty"]  # wybieramy arkusz
        self.kalorie = wb["kalorie"]

    def find_product(self):

        while True:
            searched_product = input("podaj produkt: ") #to zastapimy mowa + morfeusz

            for row in range(1, self.produkty.max_row + 1):
                for col in range(1, self.produkty.max_column + 1):
                    my_cell = self.produkty.cell(row, col)
                    if my_cell.value == searched_product:
                        found_cell = xl_rowcol_to_cell(row - 1, col - 1)
                        return found_cell
                        break

    def get_calories(self, found_cell):
        kcal = self.kalorie[found_cell]
        return kcal

    def what_you_ate(self):
        found_cell = self.find_product()
        product = self.produkty[found_cell]
        kcal = self.get_calories(found_cell)
        print("zjadłeś produkt: " + str(product.value) + " co daje: " + str(kcal.value) + "kcal")


exl = ExcelHandler()
wb = exl.open_workbook("products.xlsx")
exl.assign_sheets(wb)
exl.what_you_ate()













