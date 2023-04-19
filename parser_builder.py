# Define the production rules for the mini language
productions = {
    "<program>": [("id", "<statement>", "<program>"),
                  ("if", "<statement>", "<program>"),
                  ("while", "<statement>", "<program>"),
                  ("EPSILON",)],
    "<statement>": [("id", "<assignment>"),
                    ("if", "<conditional>"),
                    ("while", "<loop>")],
    "<assignment>": [("id", "=", "<expression>")],
    "<conditional>": [("if", "<expression>", ":", "<program>", "else", ":", "<program>")],
    "<loop>": [("while", "<expression>", ":", "<program>")],
    "<expression>": [("id", "<arith_expr>"),
                     ("number", "<arith_expr>"),
                     ("(", "<arith_expr>"),
                     ("-", "<arith_expr>"),
                     ("not", "<log_expr>")],
    "<arith_expr>": [("id", "<term>", "<add_op>", "<arith_expr>"),
                     ("number", "<term>", "<add_op>", "<arith_expr>"),
                     ("(", "<term>", "<add_op>", "<arith_expr>"),
                     ("-", "<term>", "<add_op>", "<arith_expr>")],
    "<term>": [("id", "<factor>", "<mul_op>", "<term>"),
               ("number", "<factor>", "<mul_op>", "<term>"),
               ("(", "<factor>", "<mul_op>", "<term>"),
               ("-", "<factor>", "<mul_op>", "<term>")],
    "<factor>": [("id",),
                 ("number",),
                 ("(", "<expression>", ")"),
                 ("-", "<factor>")],
    "<log_expr>": [("id", "<relation>"),
                   ("number", "<relation>"),
                   ("(", "<relation>"),
                   ("-", "<relation>"),
                   ("not", "<log_expr>")],
    "<relation>": [("<expression>", "<rel_op>", "<expression>")],
}

# Define the first and follow sets for the nonterminals
first_sets = {
    "<program>": {"id", "if", "while", "EPSILON"},
    "<statement>": {"id", "if", "while"},
    "<assignment>": {"id"},
    "<conditional>": {"if"},
    "<loop>": {"while"},
    "<expression>": {"id", "number", "(", "-", "not"},
    "<arith_expr>": {"id", "number", "(", "-", "not"},
    "<term>": {"id", "number", "(", "-", "not"},
    "<factor>": {"id", "number", "(", "-", "not"},
    "<log_expr>": {"id", "number", "(", "-", "not"},
    "<relation>": {"id", "number", "(", "-", "not"}
}

follow_sets = {
    "<program>": {"$"},
    "<statement>": {"id", "if", "while", "$"},
    "<assignment>": {"id", "if", "while", "$"},
    "<conditional>": {"id", "if", "while", "$"},
    "<loop>": {"id", "if", "while", "$"},
    "<expression>": {"<rel_op>", ")", "and", "or", ":", ",", "$"},
    "<arith_expr>": {"<add_op>", "<rel_op>", ")", "and", "or", ":", ",", "$"},
    "<term>": {"<mul_op>", "<add_op>", "<rel_op>", ")", "and", "or", ":", ",", "$"},
    "<factor>": {"<mul_op>", "<add_op>", "<rel_op>", ")", "and", "or", ":", ",", "$"},
    "<log_expr>": {"and", "or", ")", ":", ",", "$"},
    "<relation>": {"<add_op>", "<rel_op>", ")", "and", "or", ":", ",", "$"}
}
# Populate the parse table based on the first and follow sets
for nonterminal in productions:
    for terminal in first_sets[nonterminal]:
        if terminal != "EPSILON":
            parse_table[(nonterminal, terminal)] = productions[nonterminal]
    if "EPSILON" in first_sets[nonterminal]:
        for terminal in follow_sets[nonterminal]:
            parse_table[(nonterminal, terminal)] = productions[nonterminal]