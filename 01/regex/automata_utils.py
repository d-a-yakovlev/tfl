from automata.utils import *
from .operations import *


operations = {
    '*': star_op,
    '+': plus_op,
    ';': semicolon_op,
    ',': comma_op,
    '#': sharp_op,
    '?': question_op
}

priorities = {
    ';': 0,
    '#': 1,
    ',': 1,
    '*': 2,
    '+': 2,
    '?': 2
}

binary = [';', '#', ',']
unary  = ['*', '+', '?']


def is_character(char):
    return char not in {*operations.keys(), '(', ')'}

def construct_ndfa(regex_str):
    data       = ""
    op_stack   = []
    eval_stack = []

    def process_operators(priority=-1):
        while ( len(op_stack) != 0
                and op_stack[-1] != '('
                and (op_stack[-1] not in operations.keys() 
                     or priorities[op_stack[-1]] > priority)):
            
            op = op_stack[-1]
            if op in unary:
                eval_stack.append(operations[op](eval_stack[-1]))
                eval_stack.pop(-2)
                op_stack.pop()
       
            elif op in binary:
                eval_stack.append(operations[op](eval_stack[-2], eval_stack[-1]))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
                op_stack.pop()
            
        if priority == -1 and len(op_stack) != 0 and op_stack[-1] == '(':
            op_stack.pop()


    regex_str = preprocess_regex_str(regex_str)
    for char in regex_str:
        if char in list(operations.keys()) + ['(', ')']:
            if data != "":
                eval_stack.append(get_naive_ndfa(data))
            data = ""

        if char in operations:
            if len(op_stack) == 0 or op_stack[-1] in ['(', ')'] or priorities[op_stack[-1]] < priorities[char]:
                op_stack.append(char)
            else:
                process_operators(priorities[char])
                op_stack.append(char)
        elif char == '(':
            op_stack.append('(')
        elif char == ')':
            process_operators()
        else:
            data += char

    if data != "":
        eval_stack.append(get_naive_ndfa(data))

    process_operators()
    return eval_stack[-1]


def preprocess_regex_str(regex_str):
    if len(regex_str) == 0:
        return ""
    
    result, prev = [], None
    for char in regex_str:
        if prev is None:
            prev = char
            result.append(char)
            continue
        
        if (prev in unary and char == '(' 
            or prev in unary and is_character(char) 
            or is_character(prev) and is_character(char) 
            or prev == ')' and is_character(char) 
            or is_character(prev) and char == '('):
            result.append(',')
        
        result.append(char)
        prev = char
    
    return "".join(result)