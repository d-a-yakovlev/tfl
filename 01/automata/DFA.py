from .NDFA import NDFA

class DFA:
    '''
    Deterministic finite automata
    '''
    def __init__(self, table, result_states):
        self.table = table
        self.result_states = result_states
        proxy_table = {}

        for char, states in table.items():
            proxy_table[char] = [[state] if state is not None else [] for state in states]
        
        self.proxy = NDFA(proxy_table, result_states)


    def accept(self, input_string):
        return self.proxy.accept(input_string)


    def num_states(self):
        return self.proxy.num_states()


    def keys(self):
        return self.proxy.keys()
