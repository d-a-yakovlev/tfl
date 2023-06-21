import copy
EPSILON = 'EPSILON'

class NDFA:
    '''
    Non-deterministic finite automata
    '''
    def __init__(self, table, result_states):
        self.table = table
        self.result_states = result_states
        self.states = None


    def eps_closure(self, state):
        if EPSILON not in self.table.keys():
            return [state]
        
        visited = []
        active  = [state]

        while len(active) != 0:
            new_active = []
            for state in active:
                new_active.extend(self.table[EPSILON][state])
            
            visited = list(set(visited + active))
            active  = list(set(new_active).difference(visited))
        
        return visited
    

    def next_state(self, state, char):
        if char not in self.table:
            raise ValueError("Char can't be accepted")
        
        return self.table[char][state] if char in self.table else None
    

    def step(self, old_state, char):
        litera_step = set()

        for state in old_state:
            litera_step.update(self.next_state(state, char))

            if EPSILON in self.table.keys():
                litera_step.update( sum([self.eps_closure(state) for state in litera_step], []) )

        return list(litera_step) if litera_step else []


    def accept(self, input_string):
        self.states = self.eps_closure(0)
        try:
            for char in input_string:
                self.states = self.step(self.states, char)
            
            for state in self.states:
                if set(self.eps_closure(state)).intersection(self.result_states):
                    return True
            
            return False
        
        except ValueError:
            return False


    def num_states(self):
        return len(list(self.table.values())[0])


    def keys(self):
        return list(self.table.keys())


    def set_transition(self, start, char, finish):
        if char not in self.table:
            self.table[char] = [[] for _ in range(self.num_states())]
        
        self.table[char][start].append(finish)


    def copy(self):
        copied_table         = copy.deepcopy(self.table)
        copied_result_states = copy.deepcopy(self.result_states)
        copied_instance      = NDFA(copied_table, copied_result_states)

        return copied_instance