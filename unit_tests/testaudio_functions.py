import unittest
import struct
import pickle

import main.audio_functions as af

class TestAudioFunctions(unittest.TestCase):


    def test_serialise_data(self):
        data = "This is some data that needs to be serialised"
        data_test = pickle.dumps(data)
        length_test = struct.pack(">I", len(data_test))
        test = length_test + data_test
        assert af.serialise_data(data) == test


    def test_serialise_data_length(self):
        data = "I wonder what the length that this should be"
        s_data = af.serialise_data(data=data)
        length = struct.unpack('>I', s_data[:4])[0]
        assert length == len(s_data) - 4


    def test_deserialise_data(self):
        data = "This is data that is going to be deserialised"
        packet = af.serialise_data(data=data)
        serialised_data = packet[4:]
        assert af.deserialise_data(serialised_data) == data


if __name__ == '__main__':
    unittest.main