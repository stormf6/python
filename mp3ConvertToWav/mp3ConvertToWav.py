# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import array
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pydub.utils import get_array_type


def read_mp3(filename):
    sound = AudioSegment.from_mp3(filename)
    left = sound.split_to_mono()[0]
    right = sound.split_to_mono()[1]

    bit_depth = left.sample_width * 8
    array_type = get_array_type(bit_depth)
    left_numeric_array = array.array(array_type, left._data)
    right_numeric_array = array.array(array_type,right._data)
    left_channel = np.array(left_numeric_array) / 32768
    right_channel = np.array(right_numeric_array) / 32768
    wave_data = np.vstack([left_channel,right_channel])
    sf.write('Testb.wav', wave_data.T, 44100)
    return left_channel, right_channel


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_path = 'd:\\py_project\\test.mp3'
    data = read_mp3(test_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
