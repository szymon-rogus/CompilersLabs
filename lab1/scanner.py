import ply.lex as lex


BINARY_OPERATORS = ['PLUS',  'MINUS',  'TIMES',  'DIVIDE']
binary_literals = ['+', '-', '*', '/']
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'


MATRICES_OPERATORS = ['MPLUS',  'MMINUS',  'MTIMES',  'MDIVIDE']
t_MPLUS = r'.+'
t_MMINUS = r'.-'
t_MTIMES = r'.*'
t_MDIVIDE = r'./'


BRACKETS = ['LBRACKET', 'RBRACKET', 'LSQUARE', 'RSQUARE', 'LBRACE', 'RBRACE']
bracket_literals = ['(', ')', '[', ']', '{', '}']
# t_LBRACKET = r'\('
# t_BRACKET = r'\)'
# t_LSQUARE = r'\['
# t_rSQUARE = r'\]'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'


RANGE_OPERATOR = ['RANGE']
t_RANGE = r':'


TRANSPOSITION_OPERATOR = ['TRANSPOSITION']
t_TRANSPOSITION = r'\''


COMMA_SEMICOLON_OPERATORS = ['COMMA', 'SEMICOLON']
t_COMMA = r','
t_SEMICOLON = r';'


def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = '  \t \n'
