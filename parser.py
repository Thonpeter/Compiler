from typing import List, Tuple


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, expected_token_type):
        raise Exception(f"Syntax Error: Invalid syntax. Expected token type {expected_token_type}, but got {self.current_token.type} instead.")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_type)

    def program(self):
        statements = []
        while self.current_token.type != EOF:
            statement = self.statement()
            statements.append(statement)
        return ("program", statements)

    def statement(self):
        token = self.current_token
        if token.type == IDENTIFIER:
            self.eat(IDENTIFIER)
            self.eat(ASSIGN)
            expr = self.expression()
            return ("assignment", token.value, expr)
        elif token.type == IF:
            conditional = self.conditional()
            return ("conditional", conditional)
        elif token.type == WHILE:
            loop = self.loop()
            return ("loop", loop)
        else:
            self.error("statement")

    def conditional(self):
        self.eat(IF)
        expr = self.expression()
        self.eat(COLON)
        program = self.program()
        else_clause = self.else_clause()
        return ("conditional", expr, program, else_clause)

    def else_clause(self):
        if self.current_token.type == ELSE:
            self.eat(ELSE)
            return self.program()
        else:
            return None

    def loop(self):
        self.eat(WHILE)
        expr = self.expression()
        self.eat(COLON)
        program = self.program()
        return ("loop", expr, program)

    def expression(self):
        arith_expr = self.arith_expr()
        if self.current_token.type in (LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUALS, NOT_EQUALS):
            rel_op = self.rel_op()
            arith_expr2 = self.arith_expr()
            return ("rel_expr", arith_expr, rel_op, arith_expr2)
        else:
            return arith_expr

    def arith_expr(self):
        term = self.term()
        while self.current_token.type in (PLUS, MINUS):
            add_op = self.add_op()
            term2 = self.term()
            term = ("arith_expr", term, add_op, term2)
        return term

    def term(self):
        factor = self.factor()
        while self.current_token.type in (TIMES, DIVIDE):
            mul_op = self.mul_op()
            factor2 = self.factor()
            factor = ("term", factor, mul_op, factor2)
        return factor

    def factor(self):
        token = self.current_token
        if token.type == IDENTIFIER:
            self.eat(IDENTIFIER)
            return ("identifier", token.value)
        elif token.type == NUMBER:
            self.eat(NUMBER)
            return ("number", token.value)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            expr = self.expression()
            self.eat(RPAREN)
            return expr
        elif token.type == MINUS:
            self.eat(MINUS)
            factor = self.factor()
            return ("negation", factor)
        else:
            self.error("factor")

    def rel_op(self):
        token = self.current_token
        if token.type == LESS_THAN:
            self.eat(LESS_THAN)

    def program(self):
        ast = []
        while self.current_token.type in [IF, WHILE, IDENTIFIER]:
            ast.append(self.statement())
        return ast

    def parse(self):
        ast = self.program()
        if self.current_token.type != EOF:
            self.error()
        return ast

