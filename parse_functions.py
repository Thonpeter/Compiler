def parse_num(token):
    return int(token)

def parse_factor(tokens, get_next_token):
    if tokens[0] == '(':
        tokens.pop(0)  # Remove '('
        expr_val = parse_expr(tokens, get_next_token)
        if tokens[0] != ')':
            raise ValueError("Expected closing parenthesis ')'")
        tokens.pop(0)  # Remove ')'
        return expr_val
    else:
        return parse_num(tokens.pop(0))

def parse_mult(tokens, get_next_token):
    left = parse_factor(tokens, get_next_token)

    while tokens and tokens[0] in ('*', '/'):
        op = tokens.pop(0)
        right = parse_factor(tokens, get_next_token)
        left = (op, left, right)

    return left

def parse_expr(tokens, get_next_token):
    left = parse_mult(tokens, get_next_token)

    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        right = parse_mult(tokens, get_next_token)
        left = (op, left, right)

    return left

def parse(tokens):
    return parse_expr(tokens, iter(tokens).__next__)
