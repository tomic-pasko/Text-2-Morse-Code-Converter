import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write

class Sound:

    def __init__(self):
        self.sound_array = []
        # sequence of dits and dahs is Morse Code symbol
        self.dit = 'beep-short.wav'
        self.dah = 'beep-long.wav'
        self.small_pause = np.zeros([10000, 2], dtype='float32')
        self.long_pause = np.zeros([50000, 2], dtype='float32')

    def add_char(self, value):

        for i in range(len(value)):
            if value[i] == '.':
                data, fs = sf.read(self.dit, dtype='float32')
            else:
                data, fs = sf.read(self.dah, dtype='float32')

            self.sound_array.append(sd.playrec(data, fs, channels=2, dtype='float32', blocking=True))

    def add_small_pause(self):
        self.sound_array.append(sd.playrec(self.small_pause, 44100, channels=2))

    def add_long_pause(self):
        self.sound_array.append(sd.playrec(self.long_pause, 44100, channels=2))


