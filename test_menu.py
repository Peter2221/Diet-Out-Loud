from run_trybun import *
from VoiceRecording import *
from run_sarmata import *
from UserData import UserData
from run_dictation import *
from DietManager import DietManager
from ExcelHandler import ExcelHandler

""" Trybun pracuje na pliku .wav tts_output

TODO: zapis informacji o użytkowniku, jeśli jest 1 raz -> waga, wzrost, wiek -> sarmata
Obsługa błędów, jeśli ktoś powie jakąś głupotę
Wczytywanie danych z pliku, po ponownym otwarciu programu.

Liczenie BMI
Liczenie dziennego zapotrzebowania kalorycznego

"""


def main():
    # Menu
    trybun = Trybun()
    dictation = Dictation()
    trybun.say_something("Witaj w Dajet. Aut. Laud.")
    usrData = UserData()
    # usrData.remove_data_from_file()
    dm = DietManager()
    exl = ExcelHandler()
    wb = exl.open_workbook("products.xlsx")
    exl.assign_sheets(wb)

    while True:
        data, is_something = usrData.read_from_file()

        if is_something == True:
            usrData.set_params_from_file(data)

            trybun.say_something("Witaj, %s. wybierz jedną z opcji. liczenie kalorii. liczenie BEEMI. dzienne zapotrzebowanie. lub wyjście z programu" % data['name'])
            sarmata = SarmataVoiceRecognition()
            # 1, 2 lub 3
            res_semantic_interpretation = sarmata.menu_choice_recognition("grammars/menu.abnf")
            # res_semantic_interpretation = '2'

            if res_semantic_interpretation == '1':
                trybun.say_something("Wybrałeś opcję. Liczenie Kalorii.")
                # podawanie produktu
                trybun.say_something("podaj nazwę produktu")
                produkt = dictation.dictation_recognize()
                trybun.say_something("podaj wagę produktu")
                waga = dictation.dictation_recognize()
                waga = int(waga)
                dm.what_you_ate_today(produkt, waga, exl, usrData, trybun)
                # dodawanie kolejnego produktu albo wracanie, na tak lub nie ----------------------
                trybun.say_something("")

            elif res_semantic_interpretation == '2':
                trybun.say_something("Wybrałeś opcje. Liczenie beemi")
                bmi = dm.calculate_bmi(usrData)
                trybun.say_something("Twoje beemi wynosi %s" % bmi)
                continue

            elif res_semantic_interpretation == '3':
                trybun.say_something("Wybrałeś opcję. Dzienne zapotrzebowanie")
                limit = dm.calculate_limit(usrData)
                trybun.say_something("Twój dzienny limit kalorii wynosi %s" % limit)
                continue
            elif res_semantic_interpretation == '4':
                trybun.say_something("Baj Baj %s bądź silny i napakowany forewer!" % data['name'])
                break
            else:
                trybun.say_something("Endrju Ng, mistrz maszin lerningu byłby bardzo niezadowolony z twoich wyborów.")
                continue
        else:
            trybun.say_something("Podaj swoje dane.")
            trybun.say_something("Jak masz na imię?.")
            name = dictation.dictation_recognize()
            # płeć TO DO sarmata ---------------------------------------------------------------
            trybun.say_something("Podaj płeć.")
            gender = dictation.dictation_recognize()
            # age SAJMATA --------------------------------------------------------------------
            trybun.say_something("Ile masz lat (liczba)?")
            age = dictation.dictation_recognize()
            # weight --------------------------------------------------------------------------
            trybun.say_something("Ile ważysz?")
            weight = dictation.dictation_recognize()
            # height SAJMATA -------------------------------------------------------------------------
            trybun.say_something("Ile masz wzrostu?")
            height = dictation.dictation_recognize()
            # setData
            usrData.set_parameters(name, gender, age, weight, height)
            usrData.write_to_file()


if __name__ == "__main__":
    main()