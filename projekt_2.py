from run_dictation import *
from run_trybun import *

# run_dictation
args = DictationArgs("waves/example.wav")
args.mic = True

if args.wave is not None or args.mic:
    with create_audio_stream(args) as stream:
        settings = DictationSettings(args)
        recognizer = StreamingRecognizer(args.address, settings)

        print('Recognizing...')
        results = recognizer.recognize(stream)
        print_results(results)

# run_trybun      
output_wave_file = 'tts_output.wav'
ap = AddressProvider()
address = ap.get("tribune")
sampling_rate = 44100
input_text = "Siema, z tej strony Pioter"

call_synthesize(address, input_text, output_wave_file, sampling_rate)