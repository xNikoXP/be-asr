import unittest
from unittest.mock import patch

from main.application import Application

class TestApplication(unittest.TestCase):

    @unittest.skip("Not finished")
    def test_audio_stream(self):
        with patch.object(Application, "__init__", return_value=None):
            app = Application()

if __name__ == '__main__':
    unittest.main