from automata.NDFA import NDFA, EPSILON
from automata.utils import combine_automatas


def comma_op(fa_1, fa_2):
    merged = combine_automatas(fa_1, fa_2)
    for start in fa_1.result_states:
        merged.set_transition(start, EPSILON, fa_1.num_states())
    
    merged.result_states = [state + fa_1.num_states() for state in fa_2.result_states]
    return merged


def semicolon_op(fa_1, fa_2):
    merged = combine_automatas(fa_1, fa_2)
    
    shifted_finals = [f + 1 for f in merged.result_states]
    shifted_table  = {}

    for char, state_list in merged.table.items():
        shifted_table[char] = [[]] + [[state + 1 for state in states] for states in state_list] + [[]]
    
    result = NDFA(table=shifted_table, result_states=[])
    result.set_transition(0, EPSILON, 1)
    result.set_transition(0, EPSILON, fa_1.num_states() + 1)
    
    for f in shifted_finals:
        result.set_transition(f, EPSILON, result.num_states() - 1)
    
    result.result_states = [ result.num_states() - 1 ]

    return result


def star_op(fa_1):
    shifted_finals = [f + 1 for f in fa_1.result_states]
    shifted_table  = {}

    for char, state_list in fa_1.table.items():
        shifted_table[char] = [[]] + [[state + 1 for state in states] for states in state_list] + [[]]
    
    result = NDFA(table=shifted_table, result_states=[])

    for f in shifted_finals:
        result.set_transition(f, EPSILON, 1)
        result.set_transition(f, EPSILON, result.num_states() - 1)

    result.set_transition(0, EPSILON, 1)
    result.set_transition(0, EPSILON, result.num_states() - 1)
    result.result_states = [result.num_states() - 1]

    return result


def plus_op(fa_1):
    return comma_op(fa_1, star_op(fa_1))


def sharp_op(fa_1, fa_2):
    return comma_op( fa_1, star_op(comma_op(fa_2, fa_1)) )


def question_op(fa_1):
    fa_1_copy = fa_1.copy()
    for f in fa_1_copy.result_states:
        fa_1_copy.set_transition(0, EPSILON, f)

    return fa_1_copy