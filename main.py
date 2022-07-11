import sounddevice as sd
import soundfile as sf
import numpy as np
from morse_sound import Sound

new_morse_sound = Sound()

inp = input('Please type in msg you want to convert into Morse Code sound file: \n')
inp = inp.upper()

morse = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '..',
         'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
         'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..',
         '0': '_____', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', '6': '_....', '7': '__...',
         '8': '___..', '9': '____.'}

# space between letters in a word is equal to three dits
next_letter = '   '
# space between words is equal to seven dits
next_word = '       '

for count, value in enumerate(inp):
    # space between words
    if value == ' ':
        print(next_word, end='')
        new_morse_sound.add_long_pause()

    if value in morse:
        print(morse.get(value, 'NO KEY'), end='')
        new_morse_sound.add_char(morse.get(value))

    # print space between letters, unless it is last character
    if count < len(inp)-1 and value != ' ':
        print(next_letter, end='')
        new_morse_sound.add_small_pause()




