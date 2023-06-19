from .Nota import Nota

class Chord(Nota):
    def __init__(self, str):
        self.minor = ''
        if str[-1] == 'm':
            self.minor = str[-1]
            str = str[:-1]
        super().__init__(str, has_octave=False)

    def __str__(self):
        return f'{self.nota.capitalize()}{self.minor}'