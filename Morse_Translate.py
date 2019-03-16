class Morse():

    import time
    letters = {a : ["dot", "dash"],
    b : ["dash", "dot", "dot", "dot"],
    c : ["dash", "dot", "dash", "dot"],
    d : ["dash", "dot", "dot"],
    e : ["dot"],
    f : ["dot", "dot", "dash", "dot"],
    g : ["dash", "dash", "dot"],
    h : ["dot", "dot", "dot", "dot"],
    i : ["dot", "dot"],
    j : ["dot", "dash", "dash", "dash"],
    k : ["dash", "dot", "dash"],
    l : ["dot", "dash", "dot", "dot"],
    m : ["dash", "dash"],
    n : ["dash", "dot"],
    o : ["dash", "dash", "dash"]
    p : ["dot", "dash", "dash", "dot"]
    q : ["dash", "dash", "dot", "dash"]
    r : ["dot", "dash", "dot"]
    s : ["dot", "dot", "dot"]
    t : ["dash"]
    u : ["dot", "dot", "dash"]
    v : ["dot", "dot", "dot", "dash"]
    w : ["dot", "dash", "dash"]
    x : ["dash", "dot", "dot", "dash"]
    y : ["dash", "dot", "dash", "dash"]
    z : ["dash", "dash", "dot", "dot"]}


    def __int__(self):
        input = []
        result = []

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
        while not self.input == "eol":
            while not self.input == "eow":
