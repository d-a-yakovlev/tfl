from .Stave import Stave

class Songs(dict):
    def __init__(self, str):
        super().__init__()
        for stave in str.strip('{}').split(','):
            k, v = stave.split('=>')
            k, v = k.strip(), v.strip()
            self.__setitem__(k, v)

    def __setitem__(self, key, value):
        super().__setitem__(key, Stave(value))

    def __str__(self):
        out = '{}'
        for k, v in self.items():
            if k:
                out = out[:-1] + '\n'
                out += '\t' + k + ' => ' + str(v) + '\n'
        
        out += '}'
        return out
