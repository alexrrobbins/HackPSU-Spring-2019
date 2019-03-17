#
# This is the main test class for the program
#
from Morse_Translate import Morse
import Language_Translate as lang
import unittest

class Morse_Test(unittest.TestCase):
    def test_one_letter(self):
        m = Morse()
        m.__init__()
        m.input = ["dot", "dash", "eol", "eow"]
        m.output = []
        result = m.translate_input()
        self.assertEqual(result,'a')

    def test_one_word(self):
        m = Morse()
        m.__init__()
        m.input = ["dot", "dash", "eol", "dot", "dash", "dot", "dot", "eol", "dot", "eol", "dash", "dot", "dot", "dash", "eol", "eow"]
        m.output = []
        result = m.translate_input()
        self.assertEqual(result,'alex')

    def test_sentence(self):
        m = Morse()
        m.__init__()
        m.input = ["dot", "dash", "eol", "dot", "dash", "dot", "dot", "eol", "dot", "eol",
            "dash", "dot", "dot", "dash", "eol", "eow", "dot", "dash", "eol", "dot", "dash", "dot", "dot", "eol", "dot", "eol",
            "dash", "dot", "dot", "dash", "eol", "eow", "dot", "dash", "eol", "dot", "dash", "dot", "dot", "eol", "dot", "eol",
            "dash", "dot", "dot", "dash", "eol", "eow"]
        m.output = []
        result1 = m.translate_input()
        result2 = m.output_result()
        self.assertEqual(result2,'alex alex alex')

    def test_language_translation(self):
        import sys
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        print("Please type 'en' and hit enter when prompted.")
        result = lang.translate_text("Hola")
        self.assertEqual(result,"Hello")

if __name__ == '__main__':
    unittest.main()
