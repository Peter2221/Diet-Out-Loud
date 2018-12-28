from run_dictation import *
from run_trybun import *
import pyaudio
import wave
import time

def record_voice():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RECORD_SECONDS = 3
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "waves\output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("nagrywanie za 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("*** nagrywanie... ***")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("KONIEC NAGRYWANIA")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# record voice
record_voice()

# run_dictation
args = DictationArgs("waves/output.wav")
args.mic = True

if args.wave is not None or args.mic:
    with create_audio_stream(args) as stream:
        settings = DictationSettings(args)
        recognizer = StreamingRecognizer(args.address, settings)

        print('Recognizing...')
        results = recognizer.recognize(stream)
        print_results(results)

# run_trybun
# output_wave_file = 'tts_output.wav'
# ap = AddressProvider()
# address = ap.get("tribune")
# sampling_rate = 44100
# input_text = "Siema, z tej strony Pioter"
#
# call_synthesize(address, input_text, output_wave_file, sampling_rate)