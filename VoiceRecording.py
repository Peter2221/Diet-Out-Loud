import pyaudio
import wave
import time

class VoiceRecording:

    def record_voice(self):
        # podstawowe parametry
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RECORD_SECONDS = 4
        RATE = 44100
        WAVE_OUTPUT_FILENAME = "waves\output6.wav"

        # tworzy obiekt pyadio
        p = pyaudio.PyAudio()

        # tworzy stream z parametrami
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        # odlicza do nagrywania
        time.sleep(1)
        print("*** nagrywanie... ***")

        frames = []

        # zczytuje próbki z mikrofonu i dodaje do wektora, 44100/1024 * 3
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("*** koniec nagrywania ***")

        # zatrzymuje stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        # zapisuje do pliku
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


