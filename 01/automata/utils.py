from .NDFA import NDFA, EPSILON
from .DFA import DFA


def get_naive_ndfa(actual_string):
    table = {}
    for i, c in enumerate(actual_string):
        if c not in table:
            table[c] = [[] for _ in range(len(actual_string) + 1)]

        table[c][i].append(i + 1)
    
    table=table
    result_states=[len(actual_string)]

    return NDFA(table, result_states)


def combine_automatas(fa_1, fa_2):
    merged_keys = set( list(fa_1.table.keys()) + list(fa_2.table.keys()) )

    result = [state + fa_1.num_states() for state in fa_2.result_states]
    result.extend(fa_1.result_states)

    new_table = {}
    for key in merged_keys:
        new_row = []
        if key in fa_1.table:
            new_row.extend(fa_1.table[key])
        else:
            new_row.extend([[] for _ in range(fa_1.num_states())])
        
        if key in fa_2.table:
            new_row.extend([ [state + fa_1.num_states() for state in states]
                             for states in fa_2.table[key]])
        else:
            new_row.extend([[] for _ in range(fa_2.num_states())])
        
        new_table[key] = new_row
    
    return NDFA(new_table, result)


def convert_to_dfa(ndfa):
    links = []

    new_states     = [set(ndfa.eps_closure(0))]
    visited_states = []
    keys           = [x for x in list(ndfa.table.keys()) if x != EPSILON]

    while len(new_states) > 0:
        tmp = new_states.pop()
        if tmp in visited_states:
            continue

        visited_states.append(tmp)
        for char in keys:
            new_tmp = set(ndfa.step(tmp, char))
            if len(new_tmp) != 0:
                new_states.append(new_tmp)
                links.append((tmp, char, new_tmp))

    formatted_links = []
    for link in links:
        formatted_links.append( (visited_states.index(link[0]), 
                                 link[1], 
                                 visited_states.index(link[2])) )

    old_final = set(ndfa.result_states)
    result = [i for i, s in enumerate(visited_states) if s.intersection(old_final)]
    new_table = {}

    for k in keys:
        new_table[k] = [None for _ in enumerate(visited_states)]

    for link in formatted_links:
        new_table[link[1]][link[0]] = link[2]

    return DFA(new_table, result)


def minimize_dfa(dfa):
    def split_set(target, splitter, split_char):
        set_1, set_2 = set(), set()
        for condition in target:
            if dfa.table[split_char][condition] in splitter:
                set_1.add(condition)
            else:
                set_2.add(condition)

        return set_1, set_2

    sets = [ { *dfa.result_states } ]
    non_final = { *list(range(dfa.num_states())) }.difference(dfa.result_states)
    if len(non_final) > 0:
        sets.append(non_final)

    queue = []
    for symbol in dfa.keys():
        for elem in sets:
            queue.append((elem, symbol))

    while len(queue) > 0:
        splitter, char = queue.pop(0)
        for elem in sets:
            set_1, set_2 = split_set(elem, splitter, char)
            
            if len(set_1) > 0 and len(set_2) > 0:
                sets.remove(elem)
                sets.extend([set_1, set_2])

                if (elem, char) in queue:
                    queue.remove((elem, char))
                    queue.append((set_1, char))
                    queue.append((set_2, char))
                else:
                    if len(set_1) < len(set_2):
                        queue.append((set_1, char))
                    else:
                        queue.append((set_2, char))

    first_state_index = [ sets.index(elem) for elem in sets if 0 in elem ][0]
    first_state       =   sets.pop(first_state_index)
    
    sets.insert(0, first_state)
    states = len(sets)
    new_table = { k: [None] * states for k in dfa.keys() }
    
    for i, elem in enumerate(sets):
        for condition in elem:
            for symbol in dfa.keys():
                new_indexes = [sets.index(elem) for elem in sets if dfa.table[symbol][condition] in elem]
                new_table[symbol][i] = None if len(new_indexes) == 0 else new_indexes[0]

    result = [sets.index(elem) for elem in sets if elem.intersection(dfa.result_states)]
    
    return DFA(new_table, result)