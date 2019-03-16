class Morse():

    import time

    def __int__(self):
        input = []
        elapsed_time = 0

    def get_input(self, pin_input):
        time_units = 0
        while pin_input == 1:
            start = time.time()
            end = time.time()
            time_units = end - start
            if time_units == 1:
                input.append( dot )
            elif time_units == 3:
                input.append( dash )
        while pin_input == 0:
            start = time.time()
            end = time.time()
            time_units = end - start
            if time_units == 1:
                break
            elif time_units == 3:
                input.append( eol )
            elif time_units == 7:
                input.append( eow )
            elif time_units > 7:
                translate_input

    def translate_input(self):
        pass
