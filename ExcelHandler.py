from openpyxl import load_workbook
from xlsxwriter.utility import xl_rowcol_to_cell

class ExcelHandler():
    kalorie = []
    produkty = []

    def open_workbook(self, filename):
        wb = load_workbook("products.xlsx")  # wybieramy plik

    #nie jestem pewna czy ta funkcja jest potrzebna ale napisałam :3
    def assign_sheets(self, wb):
        self.produkty = wb["produkty"]  # wybieramy arkusz
        self.kalorie = wb["kalorie"]

    def find_product(self, searchedProduct):
        for row in range(1, self.produkty.max_row + 1):
            for col in range(1, self.max_column + 1):
                myCell = self.produkty.cell(row, col)
                if myCell.value == searchedProduct:
                    print("found: " + str(xl_rowcol_to_cell(row - 1, col - 1)))







