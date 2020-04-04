import ply.yacc as yacc
import scanner

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("right", 'ASSIGN'),
    ("left", 'PLUS', 'MINUS'),
    # ("left", '.+', '.-'),
    ("left", 'TIMES', 'DIVIDE'),
    # ("left", '.*', './'),
    # to fill ...
)

symbols_dict = {}


def p_error(p):
    if p:
        print("Syntax error at line %d: LexToken(%s, '%s')" % (p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

def p_expression_relational(p):
    """ comparison_operator : LESSER
                            | GREATER
                            | LESSER_EQUALS
                            | GREATER_EQUALS
                            | NOT_EQUALS
                            | EQUALS"""
    p[0] = p[1]

#def p_unary_negation(p):
    """unary_negation : """




# def p_instructions_1(p):
#     """instructions : instructions instruction """
#
#
# def p_instructions_2(p):
#     """instructions : instruction """


# to finish the grammar
# ....


parser = yacc.yacc()
