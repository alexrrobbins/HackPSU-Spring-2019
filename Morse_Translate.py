class Morse():

    import time

    def __int__(self):
        self.input = []
        self.result = []


    def get_input(self, pin_input):
        time_units = 0
        while pin_input == 1:
            start = time.time()
            end = time.time()
            time_units = end - start
            if time_units == 1:
                input.append( "dot" )
            elif time_units == 3:
                input.append( "dash" )
        while pin_input == 0:
            start = time.time()
            end = time.time()
            time_units = end - start
            if time_units == 1:
                break
            elif time_units == 3:
                input.append( "eol" )
            elif time_units == 7:
                input.append( "eow" )
            elif time_units > 7:
                translate_input

    def translate_input(self):
        temp_letter = []
        temp_word = []
        word_index = 0
        letters = {
        ("dot", "dash") : "a",
        ("dash", "dot", "dot", "dot") : "b",
        ("dash", "dot", "dash", "dot") : "c",
        ("dash", "dot", "dot") : "d",
        ("dot") : "e",
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
            while not self.input[0] == "eow":
                while not self.input[0] == "eol":
                    temp_letter.append(self.input.pop(0))
                temp_letter_tuple = tuple(temp_letter)
                print(temp_letter_tuple)
                temp_word[word_index] = letters[temp_letter_tuple]
                word_index += 1
                self.input.pop(0)
            word = temp_word.join(" ")
            temp_word = []
            word_index = 0
            result.append( word )
            self.input.pop(0)
