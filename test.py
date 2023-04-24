#from parser import  parser
import lexer
lex = lexer("x = 1 + 2 * (3 - 4)")
parser = Parser(lexer)
parse_tree = parser.parse()
print(parse_tree)
