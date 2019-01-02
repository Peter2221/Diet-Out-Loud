from run_dictation import *
from run_trybun import *
from morfeusz2_usage import Morfeusz2_usage
from ExcelHandler import ExcelHandler
from VoiceRecording import VoiceRecording


def main():
    # obiekt klasy VoiceRecording
    # nagrywa 5 sekund z mikrofonu w kompie
    # vr = VoiceRecording()
    # vr.record_voice()

    # run_dictation
    # pisze w konsoli co wykryło
    # nie trzeba zamieniać żadnych śniezek do pliku
    args = DictationArgs("waves/output3.wav")
    args.mic = True

    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)

            print('Recognizing...')
            results = recognizer.recognize(stream)
            # printuje to co wykrył
            print_results(results)

    word = results[0]
    # print słowo ponade przez mówcę
    word = word['transcript']
    # tworzę obiekt klasy morfeusza, ma funkcję która zwraca słowo w mianowniku
    morf = Morfeusz2_usage()
    product_inifinitive = morf.infinitive_of_word(word)

    # słowo w mianowniku
    print(product_inifinitive)

    # ExcelHandler
    exl = ExcelHandler()
    wb = exl.open_workbook("products.xlsx")
    exl.assign_sheets(wb)
    # wypisuje co zjadłem + kalorie
    exl.what_you_ate(product_inifinitive)

if __name__ == "__main__":
    main()