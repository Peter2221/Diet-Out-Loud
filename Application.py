from run_trybun import *
from VoiceRecording import *
from run_sarmata import *
from UserData import UserData
from run_dictation import *
from DietManager import DietManager
import datetime

""" 
"""

def main():
    # Menu
    trybun = Trybun()
    dictation = Dictation()
    trybun.say_something("Witaj w Dajet. Aut. Laud.")
    usrData = UserData()
    usrData.remove_data_from_file()
    dm = DietManager()
    sarmata = SarmataVoiceRecognition()
    sarmata_numbers = SarmataVoiceRecognitionNumbers()

    open_date = datetime.datetime.now().strftime("%Y-%m-%d")
    dm.fm.write_date_to_file(open_date, "open_date.txt")

    while True:
        data, is_something = usrData.read_from_file()

        if is_something == True:
            usrData.set_params_from_file(data)

            trybun.say_something("Witaj, %s. wybierz jedną z opcji. liczenie kalorii. liczenie BEEMI. dzienne zapotrzebowanie. ile już zjadłeś. lub wyjście z programu" % data['name'])
            # 1, 2 lub 3
            res_semantic_interpretation = sarmata.menu_choice_recognition("grammars/menu.abnf")
            #res_semantic_interpretation = '5'

            if res_semantic_interpretation == '1':
                trybun.say_something("Wybrałeś opcję. Liczenie Kalorii.")
                while True:
                    # podawanie produktu
                    trybun.say_something("podaj nazwę produktu")
                    produkt = dictation.dictation_recognize()
                    trybun.say_something("podaj wagę produktu w gramach")
                    waga = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")
                    waga = int(waga)
                    if waga == -1:
                        trybun.say_something("Spróbuj jeszcze raz.")
                        continue
                    error_result = dm.what_you_ate_today(produkt, waga, usrData, trybun)
                    if error_result == -1:
                        trybun.say_something("Spróbuj jeszcze raz.")
                        continue
                    # dodawanie kolejnego produktu albo wracanie, na tak lub nie ----------------------
                    trybun.say_something("Chcesz dodać kolejny produkt, czy wrócić do menu głownego?")
                    res_semantic_interpretation = sarmata.menu_choice_recognition("grammars/next_product.abnf")
                    if res_semantic_interpretation == '1':
                        continue
                    # jak ktoś powie głupotę to i tak do menu
                    elif res_semantic_interpretation == '2':
                        break
                    else:
                        break

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
                dm.get_today(trybun, usrData)
                continue

            elif res_semantic_interpretation == '5':
                trybun.say_something("Do widzenia %s" % data['name'])
                break
            else:
                trybun.say_something("Spróbuj jeszcze raz!")
                continue
        else:
            trybun.say_something("Podaj swoje dane.")

            while True:
                trybun.say_something("Jak masz na imię?.")
                reco = dictation.dictation_recognize()
                if reco == -1:
                    continue
                    trybun.say_something("Spróbuj jeszcze raz")
                else:
                    name = reco
                    break

            while True:
                trybun.say_something("Podaj płeć.")
                res_semantic_interpretation_gender = sarmata.menu_choice_recognition("grammars/gender.abnf")
                if res_semantic_interpretation_gender == -1:
                    trybun.say_something("Spróbuj jeszcze raz")
                    continue
                else:
                    gender = res_semantic_interpretation_gender
                    break

            while True:
                trybun.say_something("Ile masz lat?")
                reco = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")
                if reco == -1:
                    trybun.say_something("Spróbuj jeszcze raz")
                    continue
                else:
                    age = reco
                    break

            while True:
                trybun.say_something("Ile ważysz?")
                reco = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")
                if reco == -1:
                    trybun.say_something("Spróbuj jeszcze raz")
                    continue
                else:
                    weight = reco
                    break

            while True:
                trybun.say_something("Ile masz wzrostu w centymetrach?")
                reco = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")
                if reco == -1:
                    trybun.say_something("Spróbuj jeszcze raz")
                    continue
                else:
                    height = reco
                    break

            # setData
            usrData.set_parameters(name, gender, age, weight, height)
            usrData.write_to_file()

if __name__ == "__main__":
    main()