"""PyAudio Example: Play a WAVE file."""

#import pyaudio
import wave
import sys

#CHUNK = 1024

if len(sys.argv) < 2:
    print("Shows info about a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf_name = sys.argv[1]
