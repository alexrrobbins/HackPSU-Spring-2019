from Morse_Translate import Morse
import unittest

m = Morse()
m.__init__()
m.input = ["dot", "dash", "eol", "eow"]
result = m.translate_input()
print(result)
m.add_word(result)
