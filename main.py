#! /usr/bin/env python

import numpy as np
import scipy.io.wavfile as wav

def main():
    sample_rate = 44100
    # f is the frequency in hertz
    f = 440
    # t is time in seconds (can be int or float)
    t = 3
    # waveform holds the function (this time, sine)
    waveform = np.sin

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = waveform(2.0 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

if __name__ == '__main__':
    main()
