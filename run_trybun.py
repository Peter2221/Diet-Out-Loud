#!/usr/bin/env python3
# coding=utf-8

from tribune.call_synthesize import call_synthesize
from address_provider import AddressProvider
import pyaudio
import wave
import time


class Trybun:
    def say_something(self, text):

        print(text)
        # # Config:
        # output_wave_file = 'tts_output.wav'
        # ap = AddressProvider()
        # address = ap.get("tribune")
        # sampling_rate = 44100
        # input_text = text
        #
        # call_synthesize(address, input_text, output_wave_file, sampling_rate)
        # self.playWave()

    def playWave(self):
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(r"tts_output.wav", "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()
