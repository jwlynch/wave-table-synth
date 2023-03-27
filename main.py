#! /usr/bin/env python

import numpy as np
import scipy.io.wavfile as wav

def main():
    sample_rate = 44100
    f = 440
    t = 3
    waveform = np.sin

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))


if __name__ == '__main__':
    main()
