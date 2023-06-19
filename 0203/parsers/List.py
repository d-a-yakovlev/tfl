class List(list):
    def __init__(self, str):
        self.data = []
        for elem in str.strip('[]').split(','):
            self.data.append(elem)

    def __str__(self):
        out = '['
        for elem in self.data:
            out += str(elem) + ','
        out = out[:-1] + ']'
        return out