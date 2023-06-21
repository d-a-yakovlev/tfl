from automata.utils import *
from .automata_utils import *

def match(regex, input_string):
    ndfa = construct_ndfa(regex)
    dfa  = convert_to_dfa(ndfa)

    minimized_dfa = minimize_dfa(dfa)
    current_state = 0

    for char in input_string:
        if char not in minimized_dfa.keys():
            return False
    
        next_state = minimized_dfa.table[char][current_state]
        if next_state is None:
            return False

        current_state = next_state
    
    return current_state in minimized_dfa.result_states