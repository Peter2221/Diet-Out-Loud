from run_dictation import *
from run_trybun import *
from morfeusz2_usage import Morfeusz2_usage
from ExcelHandler import ExcelHandler, NoProductException
from VoiceRecording import VoiceRecording


def main():
    # obiekt klasy VoiceRecording
    # nagrywa 5 sekund z mikrofonu w kompie
    #vr = VoiceRecording()
    #vr.record_voice()

    # run_dictation
    # pisze w konsoli co wykryło
    # nie trzeba zamieniać żadnych śniezek do pliku
    args = DictationArgs("waves/output5.wav")
    args.mic = True

    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)

            print('Recognizing...')
            results = recognizer.recognize(stream)
            # printuje to co wykrył
            print_results(results)

    words = results[0]
    # print słowo ponade przez mówcę
    words = words['transcript']
    words = words.split()
    other_words = []
    # petla dla kazdego słowa
    for word in words:
        if word.isdigit() == True:
            what_weight = word
        else:
            if word == "gram" or word == "gramów":
                continue
            other_words.append(word)

    # tworzę obiekt klasy morfeusza, ma funkcję która zwraca słowo w mianowniku
    morf = Morfeusz2_usage()
    # ExcelHandler
    exl = ExcelHandler()
    wb = exl.open_workbook("products.xlsx")
    exl.assign_sheets(wb)

    try:
        for word in other_words:
            product_inifinitive = morf.infinitive_of_word(word)
            print(product_inifinitive)
            # wypisuje co zjadłem + kalorie
            exl.what_you_ate(product_inifinitive)
    except NoProductException as exception:
        print(exception.args[0])

if __name__ == "__main__":
    main()