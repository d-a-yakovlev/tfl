from .Nota import Nota
from .Chord import Chord

class Stave:
    def __init__(self, str):
        self.data = []
        for mus_sym in str.strip('~').split('_'):
            if mus_sym[-1].isnumeric():
                self.data.append(Nota(mus_sym.strip()))
            else:
                self.data.append(Chord(mus_sym.strip()))

    def __str__(self):
        out = '~'
        for obj in self.data:
            out += str(obj) + '_'
        
        out = out[:-1] + '~'
        return out
    
    def __add__(self, tone):
        for i in range(len(self.data)):
            self.data[i] = self.data[i] + tone

        return str(self)