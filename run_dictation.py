#!/usr/bin/env python3
# coding=utf-8
from dictation.dictation_client import create_audio_stream, print_results2
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
from VoiceRecording import VoiceRecording
from morfeusz2_usage import Morfeusz2_usage

class DictationArgs:
    address = None                      # IP address and port (address:port) of a service the client will connect to.
    interim_results = False             # If set - messages with temporal results will be shown.
    max_alternatives = 3                # Maximum number of recognition hypotheses to be returned.
    mic = False                         # Use microphone as an audio source (instead of wave file).
    no_input_timeout = 5000             # MRCP v2 no input timeout [ms].
    recognition_timeout = 15000         # MRCP v2 recognition timeout [ms].
    session_id = None                   # Session ID to be passed to the service. If not specified, the service will generate a default session ID itself.
    single_utterance = False            # If set - the recognizer will detect a single spoken utterance.
    speech_complete_timeout = 5000      # MRCP v2 speech complete timeout [ms].
    speech_incomplete_timeout = 6000    # MRCP v2 speech incomplete timeout [ms].
    time_offsets = False                # If set - the recognizer will return also word time offsets.
    wave = None                         # Path to wave file with speech to be recognized. Should be mono, 8kHz or 16kHz.

    def __init__(self, wav_filepath=None):
        ap = AddressProvider()
        if wav_filepath:
            self.wave = opjoin(wav_filepath)
        self.address = ap.get("dictation")

class Dictation:
    def dictation_recognize(self):
        morf = Morfeusz2_usage()
        vr = VoiceRecording()
        vr.record_voice()
        args = DictationArgs("waves/output6.wav")
        args.mic = True

        if args.wave is not None or args.mic:
            with create_audio_stream(args) as stream:
                settings = DictationSettings(args)
                recognizer = StreamingRecognizer(args.address, settings)

                print('Recognizing...')
                results = recognizer.recognize(stream)
                # printuje to co wykrył
                print_results2(results)

        words = results[0]
        # print słowo ponade przez mówcę
        words = words['transcript']
        words = words.split()
        other_words = []
        what_weight = 0
        # petla dla kazdego słowa
        for word in words:
            # jakbysmy potrzebowali wagi
            if word.isdigit() == True:
                what_weight = int(word)
                return what_weight
            else:
                if word == "gram" or word == "gramów" or word == "gramy":
                    continue
                other_words.append(word)

        product_inifinitive = morf.infinitive_of_word(other_words[0])
        print(product_inifinitive)
        return product_inifinitive

    def dictation_recognize_numbers(self):
        morf = Morfeusz2_usage()
        vr = VoiceRecording()
        #vr.record_voice()
        args = DictationArgs("waves/output6.wav")
        args.mic = True

        if args.wave is not None or args.mic:
            with create_audio_stream(args) as stream:
                settings = DictationSettings(args)
                recognizer = StreamingRecognizer(args.address, settings)

                print('Recognizing...')
                results = recognizer.recognize(stream)
                # printuje to co wykrył
                print_results2(results)

        words = results[0]
        # print słowo ponade przez mówcę
        words = words['transcript']
        words = words.split()
        other_words = []
        what_weight = 0
        # petla dla kazdego słowa
        for word in words:
            # jakbysmy potrzebowali wagi
            if word.isdigit() == True:
                what_weight = int(word)
                return what_weight
            else:
                if word == "gram" or word == "gramów" or word == "gramy":
                    continue
                other_words.append(word)

        product_inifinitive = morf.infinitive_of_word(other_words[0])
        print(product_inifinitive)
        return product_inifinitive



if __name__ == '__main__':

    args = DictationArgs("waves/example.wav")
    args.mic = True

    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)

            print('Recognizing...')
            results = recognizer.recognize(stream)
            print_results2(results)
