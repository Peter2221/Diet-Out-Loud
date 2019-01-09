from run_trybun import *
from VoiceRecording import *
from run_sarmata import *

""" Trybun pracuje na pliku .wav tts_output

TODO: zapis informacji o użytkowniku, jeśli jest 1 raz -> waga, wzrost, wiek -> sarmata
Obsługa błędów, jeśli ktoś powie jakąś głupotę
Wczytywanie danych z pliku, po ponownym otwarciu programu.

Liczenie BMI
Liczenie dziennego zapotrzebowania kalorycznego

"""

def main():
    trybun = Trybun()
    trybun.say_something("Witaj, wybierz jedną z opcji. liczenie kalorii. liczenie BIJEMAJ. lub dzienne zapotrzebowanie. ")

    trybun.playWave()

    sarmata = SarmataVoiceRecognition()
    # 1, 2 lub 3
    res_semantic_interpretation = sarmata.menu_choice_recognition()

    if res_semantic_interpretation == '1':
        trybun.say_something("Wybrałeś opcję. Liczenie Kalorii.")
        trybun.playWave()
    elif res_semantic_interpretation == '2':
        trybun.say_something("Wybrałeś opcje. Liczenie beemi")
        trybun.playWave()
    elif res_semantic_interpretation == '3':
        trybun.say_something("Wybrałeś opcję. Dzienne zapotrzebowanie")
        trybun.playWave()
    else:
        trybun.say_something("Jesteś dzbanem")
        trybun.playWave()



if __name__ == "__main__":
    main()