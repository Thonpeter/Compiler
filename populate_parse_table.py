import parse_functions

parse_table = {
    'num': parse_functions.parse_num,
    '(': lambda x: None,
    ')': lambda x: None,
    '*': lambda x, y: ('*', x, y),
    '/': lambda x, y: ('/', x, y),
    '+': lambda x, y: ('+', x, y),
    '-': lambda x, y: ('-', x, y),
}

def populate_parse_table():
    for symbol in parse_table:
        if symbol not in ('(', ')'):
            parse_table[symbol] = parse_functions.parse_factor
    parse_table['*'] = parse_functions.parse_mult
    parse_table['/'] = parse_functions.parse_mult
    parse_table['+'] = parse_functions.parse_expr
    parse_table['-'] = parse_functions.parse_expr

populate_parse_table()
