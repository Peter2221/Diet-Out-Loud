from run_trybun import *
from VoiceRecording import *
from run_sarmata import *
from UserData import UserData
from run_dictation import *

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

    while True:
        data, is_something = usrData.read_from_file()

        if is_something == True:
            trybun.say_something("Witaj, %s. wybierz jedną z opcji. liczenie kalorii. liczenie BIJEMAJ. lub dzienne zapotrzebowanie. " % data['name'])

            sarmata = SarmataVoiceRecognition()
            # 1, 2 lub 3
            res_semantic_interpretation = sarmata.menu_choice_recognition()

            if res_semantic_interpretation == '1':
                trybun.say_something("Wybrałeś opcję. Liczenie Kalorii.")
            elif res_semantic_interpretation == '2':
                trybun.say_something("Wybrałeś opcje. Liczenie beemi")
            elif res_semantic_interpretation == '3':
                trybun.say_something("Wybrałeś opcję. Dzienne zapotrzebowanie")
            else:
                trybun.say_something("Jesteś dzbanem")
        else:
            trybun.say_something("Podaj swoje dane.")
            trybun.say_something("Jak masz na imię?.")
            name = dictation.dictation_recognize()
            # age
            trybun.say_something("Ile masz lat (liczba)?")
            age = dictation.dictation_recognize()
            # weight
            trybun.say_something("Ile ważysz?")
            weight = dictation.dictation_recognize()
            # height
            trybun.say_something("Ile masz wzrostu?")
            height = dictation.dictation_recognize()
            # setData
            usrData.set_parameters(name, age, weight, height)
            usrData.write_to_file()



if __name__ == "__main__":
    main()