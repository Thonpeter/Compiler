from populate_parse_table import parse_table
from parse_functions import parse

# List of input tokens to parse
input_tokens = [
    "5 + 6 * 7",
    "( 3 + 4 ) * 5",
    "2 + ( 3 + 4 ) * 5",
    "1 - 2 - 3",
    "1 - ( 2 - 3 )",
    "1 + 2 + 3 + 4",
    "1 * 2 * 3 * 4",
    "1 + 2 * 3 + 4",
    "1 * 2 + 3 * 4",
    "( 1 + 2 ) * ( 3 + 4 )",
    "( 1 + 2 * 3 ) * 4",
]

# Call the parse function with each input token
for i, token in enumerate(input_tokens):
    tokens = token.split()
    print(f"Test {i+1}: {tokens}")
    result = parse(tokens)
    print(f"Result: {result}\n")
