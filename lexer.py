# lexer.py
import ply.lex as lex
from ply.lex import TOKEN
import Error as Error

errors = []

# Palavras reservadas
reserved = {
    'some': 'SOME',
    'all': 'ALL',
    'value': 'VALUE',
    'min': 'MIN',
    'max': 'MAX',
    'exactly': 'EXACTLY',
    'that': 'THAT',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'only' : 'ONLY',
    'class:': 'CLASS',
    'equivalentto:': 'EQUIVALENTTO',
    'individuals:': 'INDIVIDUALS',
    'subclassof:': 'SUBCLASSOF',
    'disjointclasses:': 'DISJOINTCLASSES',
    'disjointwith:' : 'DISJOINTWITH'
}

# Regex para identificar palavras reservadas
reserved_regex = r'\b([sS][oO][mM][eE])\b|' \
                 r'([aA][lL][lL])\b|' \
                 r'([vV][aA][lL][uU][eE])\b|' \
                 r'([mM][iI][nN])\b|' \
                 r'([mM][aA][xX])\b|' \
                 r'([eE][xX][aA][cC][tT][lL][yY])\b|' \
                 r'([tT][hH][aA][tT])\b|' \
                 r'([nN][oO][tT])\b|' \
                 r'([aA][nN][dD])\b|' \
                 r'([oO][rR])\b|' \
                 r'([oO][nN][lL][yY])\b|' \
                 r'(Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:|DisjointWith:)'

# Símbolos especiais
special_symbols = {
    '(': 'LEFTPAREN',
    ')': 'RIGHTPAREN',
    '[': 'LEFTBRACKET',
    ']': 'RIGHTBRACKET',
    '{': 'LEFTBRACE',
    '}': 'RIGHTBRACE',
    ',': 'COMMA',
    '>': 'GREATERTHAN',
    '<': 'LESSTHAN',
    '=': 'EQUAL',
    '>=': 'GREATEROREQUAL',
    '<=': 'LESSOREQUAL',
}

# Tokens
tokens = [
    'CLASSNAME', 'PROPERTY', 'INDIVIDUAL', 'NAMESPACE',
    'DATATYPE', 'CARDINALITY', 'SPECIALSYMBOL', 'KEYWORD'
] + list(reserved.values()) + list(special_symbols.values())

# tokens = [
#     'CLASSNAME',   
#     'PROPERTY',   
#     'INDIVIDUAL',
#     'DATATYPE',
#     'EQUIVALENTTO',
    
#     # Palavras reservadas
#     'SOME',
#     'CLASS',       
#     'INDIVIDUALS', 
#     'SUBCLASSOF',
#     'DISJOINTCLASSES',
#     'COMMA',
#     'NAMESPACE',
#     'MIN',
#     'MAX',
#     'CARDINALITY',
#     'AND',
#     'OR',
#     'ONLY',
#     'LEFTPAREN',
#     'RIGHTPAREN',
#     'LEFTBRACKET',
#     'RIGHTBRACKET',
#     'LEFTBRACE',
#     'RIGHTBRACE',
#     'GREATEROREQUAL',
#     'LESSOREQUAL',
#     'LESSTHAN',
#     'GREATERTHAN',
#     'EQUAL',
#     'EXACTLY',
#     'ALL',
#     'VALUE',
#     'NOT',
#     'THAT',
#     'DISJOINTWITH'
# ]


# Ignorar espaços em branco
t_ignore = ' \t\r'

@TOKEN(reserved_regex)
def t_reserved_variant(t):
    t.type = reserved.get(t.value.lower(), 'KEYWORD')
    return t

def t_NAMESPACE(t):
    r'(owl:|rdf:|xsd:|rdfs:)'
    t.type='NAMESPACE'
    return t

def t_DATATYPE(t):
    r'(anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|gDay|gMonth|gMonthDay|gYear|gYearMonth|hexBinary|integer|int|language|long|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort)'
    return t

def t_special_symbols(t):
    r'>=|<=|[<>\[\]{}(),=]'
    t.type = reserved.get(t.value.lower(), special_symbols.get(t.value.lower()))
    return t

def t_INDIVIDUAL(t):
    r'[A-Z][a-zA-Z0-9]*[0-9]'
    t.type="INDIVIDUAL"
    return t

def t_CLASSNAME(t):
    r'[A-Z][a-zA-Z]*_?[A-Za-z]*'
    
    return t

def t_PROPERTY(t):
    r'[a-z][a-zA-Z]*'
    return t

def t_CARDINALITY(t):
    r'[0-9]+'
    return t

# Tratar quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_COMMENT_LINE(p):
    r'\#.*'
    pass

def t_COMMENT_BLOCK(p):
    r'/\*.*?\*/'
    pass

# Tratamento de erros
def t_error(t):
    error = Error.Error(t.value[0], t.lineno, find_column(t.lexer.lexdata, t))
    errors.append(error)
    t.lexer.skip(1)

lexer = lex.lex()