from Morse_Translate import Morse
import unittest

m = Morse()
m.__init__()
m.input = ["dot", "dot", "dash", "eol", "eow"]
result = m.translate_input()
print(result)
