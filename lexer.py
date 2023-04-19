import re

# Regular expressions for each token type
identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'
keyword = r'if|else|while|for|in|True|False|None'
number = r'0[xX][0-9a-fA-F]+|[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
string = r'\'(\\.|[^\\\'"])*\'|\"(\\.|[^\\\'"])*\"'
operator = r'\+|\-|\*|\/|<|>|==|!=|<=|>=|and|or|=|\+=|\-=|\*=|\/=|\&|\||\^|~|<<|>>|not|\*\*|%'
punctuation = r'\(|\)|\[|\]|\{|\}|,|;|\.|\:|\.\.\.|\@\w+'
comment = r'\#.*'

# Combined regular expression for all tokens
token_exprs = [
    ('NEWLINE', r'\\n'),
    ('SKIP', r'[ \t]+'),
    ('IDENTIFIER', identifier),
    ('KEYWORD', keyword),
    ('NUMBER', number),
    ('STRING', string),
    ('OPERATOR', operator),
    ('PUNCTUATION', punctuation),
    ('COMMENT', comment)
]

# List of keywords
keywords = ['if', 'else', 'while', 'for', 'in']

# List of keywords with special meaning
special_keywords = ['True', 'False', 'None']

# List of built-in functions and constants
builtins = ['abs', 'all', 'any', 'bin', 'bool', 'chr', 'complex', 'dict', 'divmod', 'enumerate', 'filter', 'float',
            'format', 'hex', 'int', 'len', 'list', 'map', 'max', 'min', 'oct', 'ord', 'pow', 'print', 'range',
            'reversed', 'round', 'set', 'slice', 'sorted', 'str', 'sum', 'tuple', '__import__', '__name__']


class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.text = text

    def tokenize(self):
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_exprs)
        line_num = 1
        line_start = 0

        for match in re.finditer(tok_regex, self.text):
            token_type = match.lastgroup
            token_value = match.group(token_type)

            if token_type == "NEWLINE":
                line_num += 1
                line_start = match.end()

            elif token_type == "SKIP" or token_type == "COMMENT":
                pass

            else:
                if token_type == "IDENTIFIER":
                    if token_value in keywords:
                        token_type = "KEYWORD"
                    elif token_value in special_keywords:
                        token_type = token_value.upper()
                    elif token_value in builtins:
                        token_type = "BUILTIN"
                elif token_type == "STRING":
                    # added support for double quotes in addition to single quotes
                    if token_value[0] == "\'":
                        token_value = eval(token_value)
                    elif token_value[0] == "\"":
                        token_value = eval(token_value.replace("'", "\\'"))
                    token_type = "STRING"

                self.tokens.append({
                    'type': token_type,
                    'value': token_value,
                    'line': line_num
                })
        return self.tokens


if __name__ == '__main__':
    text = '''
    # Compute the nth Fibonacci number
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n-1) + fib(n-2)
    '''

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)
