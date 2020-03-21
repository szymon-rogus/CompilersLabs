import ply.lex as lex
from itertools import chain

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

ASSIGN_OPERATORS = ['ASSIGN', 'ADD_ASSIGN',
                    'SUBSTRACT_ASSIGN', 'MULTIPLY_ASSIGN', 'DIVIDE_ASSIGN']
RELATIONAL_OPERATORS = ['LESSER', 'GREATER', 'LESSER_EQUALS',
                        'GREATER_EQUALS', 'NOT_EQUALS', 'EQUALS']

t_ASSIGN = r'\='
t_ADD_ADDIGN = r'\+='
t_SUBSTRACT_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='

t_LESSER = r'<'
t_GREATER = r'>'
t_LESSER_EQUALS = r'<='
t_GREATER_EQUALS = r'>='
t_NOT_EQUALS = r'!='
t_EQUALS = r'=='


reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT',
}


FUNCTIONS = ['ID', 'INT', 'FLOAT', 'STRING']


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_STRING(t):
    r'\'[\w\W]*\''  # case => ""
    t.value = str(t.value)
    return t


list_of_tokenlist = [BINARY_OPERATORS, MATRICES_OPERATORS, BRACKETS, RANGE_OPERATOR,
                     TRANSPOSITION_OPERATOR, COMMA_SEMICOLON_OPERATORS, ASSIGN_OPERATORS, RELATIONAL_OPERATORS]
chain_object = chain.from_iterable(list_of_tokenlist)
tokens = list(chain_object) + list(reserved.keys())
t_ignore = '  \t\n'  # case => #


lexer = lex.lex()
