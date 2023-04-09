"""PyAudio Example: Play a WAVE file."""

#import pyaudio
import wave
import sys

#CHUNK = 1024

if len(sys.argv) < 2:
    print("Shows info about a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf_name = sys.argv[1]

wf = wave.open(wf_name, 'rb')

#p = pyaudio.PyAudio()

#stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                channels=wf.getnchannels(),
#                rate=wf.getframerate(),
#                output=True)

#format = p.get_format_from_width(wf.getsampwidth())
width = wf.getsampwidth()
channels = wf.getnchannels()
rate = wf.getframerate()

print(f"wave file '{wf_name}', width {width}, channels {channels}, rate {rate}\n")

wf.close()

#data = wf.readframes(CHUNK)

#while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

#stream.stop_stream()
#stream.close()

#p.terminate()
