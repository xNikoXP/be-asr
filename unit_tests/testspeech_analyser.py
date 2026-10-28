import unittest
import main.speech_analyser as sa

class TestSpeechAnalyser(unittest.TestCase):


    def test_find_ban_words(self):
        bad_words = "Uh something is probably wrong here"
        self.assertTrue(sa.ban_check(bad_words))
        

    def test_no_ban_words(self):
        good_words = "Hello there my name is peter"
        self.assertFalse(sa.ban_check(good_words))


if __name__ == '__main__':
    unittest.main()