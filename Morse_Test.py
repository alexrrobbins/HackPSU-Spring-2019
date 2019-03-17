from Morse_Translate import Morse
import unittest

class Morse_Test(unittest.TestCase):
    def test_one_letter(self):
        m = Morse()
        m.__init__()
        m.input = ["dot", "dash", "eol", "eow"]
        m.output = []
        result = m.translate_input()
        self.assertEqual(result,'a')

if __name__ == '__main__':
    unittest.main()
