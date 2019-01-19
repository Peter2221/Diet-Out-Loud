from run_trybun import *
from VoiceRecording import *
from run_sarmata import *
from UserData import UserData
from run_dictation import *
from DietManager import DietManager

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
    #usrData.remove_data_from_file()
    dm = DietManager()
    sarmata = SarmataVoiceRecognition()

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
                    waga = dictation.dictation_recognize()
                    waga = int(waga)
                    dm.what_you_ate_today(produkt, waga, usrData, trybun)
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
                trybun.say_something("Baj Baj %s bądź silny i napakowany forewer!" % data['name'])
                break
            else:
                trybun.say_something("Endrju Ng, mistrz maszin lerningu byłby bardzo niezadowolony z twoich wyborów.")
                continue
        else:
            sarmata_numbers = SarmataVoiceRecognitionNumbers()

            trybun.say_something("Podaj swoje dane.")

            trybun.say_something("Jak masz na imię?.")
            name = dictation.dictation_recognize()

            trybun.say_something("Podaj płeć.")
            res_semantic_interpretation_gender = sarmata.menu_choice_recognition("grammars/gender.abnf")
            gender = res_semantic_interpretation_gender

            trybun.say_something("Ile masz lat (liczba)?")
            age = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")

            trybun.say_something("Ile ważysz?")
            weight = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")

            trybun.say_something("Ile masz wzrostu?")
            height = sarmata_numbers.menu_choice_recognition("grammars/numbers.abnf")
            # setData
            usrData.set_parameters(name, gender, age, weight, height)
            usrData.write_to_file()


if __name__ == "__main__":
    main()