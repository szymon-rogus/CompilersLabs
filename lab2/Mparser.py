import scanner
import ply.yacc as yacc

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


def p_program(p):
    """PROGRAM : EXPRESSION"""
    print("RESULT =", p[1])


def p_expression_number(p):
    """EXPRESSION : INT
                  | FLOAT"""
    p[0] = p[1]


def p_expression_id(p):
    """EXPRESSION : ID"""
    p[0] = p[1]
    value = symbols_dict.get(p[1])
    if value:
        p[0] = value
    else:
        p[0] = 0
        print("'%s' not used\n" % p[1])


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION PLUS EXPRESSION
                  | EXPRESSION MINUS EXPRESSION"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_assignment(p):
    """EXPRESSION : EXPRESSION ASSIGN EXPRESSION"""
    p[0] = p[3]
    symbols_dict[p[1]] = p[3]


# def p_instructions_1(p):
#     """instructions : instructions instruction """
#
#
# def p_instructions_2(p):
#     """instructions : instruction """


# to finish the grammar
# ....


parser = yacc.yacc()
