class Morse():
    import time

    def __int__(self,input=[],output=[]):
        self.input = input
        self.output = result

    def translate_input(self):
        temp_letter = []
        temp_word = []
        letters = {
        ("dot", "dash") : "a",
        ("dash", "dot", "dot", "dot") : "b",
        ("dash", "dot", "dash", "dot") : "c",
        ("dash", "dot", "dot") : "d",
        ("dot",) : "e",
        ("dot", "dot", "dash", "dot") : "f",
        ("dash", "dash", "dot") : "g",
        ("dot", "dot", "dot", "dot") : "h",
        ("dot", "dot") : "i",
        ("dot", "dash", "dash", "dash") : "j",
        ("dash", "dot", "dash") : "k",
        ("dot", "dash", "dot", "dot") : "l",
        ("dash", "dash") : "m",
        ("dash", "dot") : "n",
        ("dash", "dash", "dash") : "o",
        ("dot", "dash", "dash", "dot") : "p",
        ("dash", "dash", "dot", "dash") : "q",
        ("dot", "dash", "dot") : "r",
        ("dot", "dot", "dot") : "s",
        ("dash") : "t",
        ("dot", "dot", "dash") : "u",
        ("dot", "dot", "dot", "dash") : "v",
        ("dot", "dash", "dash") : "w",
        ("dash", "dot", "dot", "dash") : "x",
        ("dash", "dot", "dash", "dash") : "y",
        ("dash", "dash", "dot", "dot") : "z"
        }

        while len(self.input) > 0:
            while not self.input[0] == "eow" and len(self.input) > 0:
                if not self.input[0] == "eol":
                    temp_letter.append(self.input.pop(0))
                else:
                    temp_letter_tuple = tuple(temp_letter)
                    temp_word.append(letters[temp_letter_tuple])
                    self.input.pop(0)
                    temp_letter = []
            word = ''.join(temp_word)
            temp_word = []
            self.output.append(word)
            self.input.pop(0)
        return word

    def output_result(self):
        import sys
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        import Language_Translate
        english_text = ' '.join(self.output)
        final_output = Language_Translate.translate_text(english_text)
        return final_output

    def get_letter_input(self, time_units):
        if time_units == 1:
            input.append( "dot" )
        elif time_units == 3:
            input.append( "dash" )

    def get_space_input(self, time_units):
        if time_units == 3:
            input.append( "eol" )
        elif time_units == 7:
            input.append( "eow" )
