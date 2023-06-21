import regex.utils as utils

import re

def match_test(regex_list, test_cases):

    bool_cases = { regex : [ bool(re.match(regex, case)) for case in test_cases]
    for regex in regex_list}


    for regex_str in regex_list:
        for test_case in test_cases:
            res    = utils.match(regex_str, test_case)
            actual = bool_cases[regex_str][test_cases.index(test_case)]
            passed = actual == res

            print(f"regex : {regex_str}, str : {test_case}\n\t=> {res}\nTest - "
                   + ("passed" if passed else "failed"))
            assert passed

        print("-" * 22)