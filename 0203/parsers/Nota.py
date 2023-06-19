class Nota:
    def __init__(self, str, has_octave=True):
        self.has_octave = has_octave

        self.nota = ''
        self.octave = None

        if ( len(str) == 2 and has_octave ) \
            or ( len(str) == 1 and not has_octave ):
            self.nota = str[0].lower()
            self.octave = int(str[1]) if has_octave else None
        elif ( len(str) == 3 and has_octave ) \
            or ( len(str) == 2 and not has_octave ):
            if str[0].lower() == 'e' or str[0].lower() == 'b':
                raise Exception("E# or B# is ILLEGAL")
            self.nota = str[0].lower() + str[1].lower()
            self.octave = int(str[2]) if has_octave else None

    def __str__(self):
        return f'{self.nota.lower()}{self.octave}'

    def __add__(self, tone):
        if int(tone * 10) % 10 == 5:
            nota_code = ord(self.nota[0])
            nota_code -= ord('a')

            if ( len(str(self)) == 2 and self.has_octave ) \
                or ( len(str(self)) == 1 and not self.has_octave ):
                nota_code += int(tone)
            else:
                nota_code += int(tone) + 1
            
            if self.has_octave:
                self.octave += nota_code // 7
            nota_code %= 7
            nota_code += ord('a')
            self.nota = chr(nota_code) + self.nota[1:]

            if ( len(str(self)) == 2 and self.has_octave) \
                or ( len(str(self)) == 1 and not self.has_octave):
                self.nota += '#'
                if self.nota[0] in ['e', 'b']:
                    self.nota = chr(ord(self.nota[0]) + 1)
                    
                return str(self)
            
            elif ( len(str(self)) == 3 and self.has_octave) \
                or ( len(str(self)) == 2 and not self.has_octave):
                self.nota = self.nota[0]
                return str(self)
            
        elif int(tone * 10) % 10 == 0:
            nota_code = ord(self.nota[0])
            nota_code -= ord('a')

            nota_code += int(tone)
            if self.has_octave:
                self.octave += nota_code // 7
            nota_code %= 7
            nota_code += ord('a')
            self.nota = chr(nota_code) + self.nota[1:]

            return str(self)
        else:
            return f'Tone could be : 0, 0.5, 1, 1.5 and so on. Got : {tone}'
        
    def __sub__(self, tone):
        return self + (-float(tone))