# lexer.py
import ply.lex as lex
from ply.lex import TOKEN
import Error as Error

errors = []

# Cores para o terminal
RESET = "\u001B[0m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
CYAN = "\u001B[36m"
PURPLE = "\u001B[35m"
BOLD = "\u001B[1m"

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
    'class:': 'CLASS',
    'equivalentto:': 'EQUIVALENTTO',
    'individuals:': 'INDIVIDUALS',
    'subclassof:': 'SUBCLASSOF',
    'disjointclasses:': 'DISJOINTCLASSES',
}

# Regex para identificar palavras reservadas
reserved_regex = r'\b([sS][oO][mM][eE])|' \
                 r'([aA][lL][lL])|' \
                 r'([vV][aA][lL][uU][eE])|' \
                 r'([mM][iI][nN])|' \
                 r'([mM][aA][xX])|' \
                 r'([eE][xX][aA][cC][tT][lL][yY])|' \
                 r'([tT][hH][aA][tT])|' \
                 r'([nN][oO][tT])|' \
                 r'([aA][nN][dD])|' \
                 r'([oO][rR])\b|' \
                 r'(Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:)'

# Símbolos especiais
special_symbols = {
    '(': 'LeftParen',
    ')': 'RightParen',
    '[': 'LeftBracket',
    ']': 'RightBracket',
    '{': 'LeftBrace',
    '}': 'RightBrace',
    ',': 'Comma',
    '>': 'GreaterThan',
    '<': 'LessThan',
    '=': 'Equal',
    '>=': 'GreaterOrEqual',
    '<=': 'LessOrEqual',
}

# Tokens
tokens = [
    'CLASSNAME', 'PROPERTY', 'INDIVIDUAL', 'NAMESPACE',
    'DATATYPE', 'CARDINALITY', 'SPECIALSYMBOL', 'KEYWORD'
] + list(reserved.values())

# Ignorar espaços em branco
t_ignore = ' \t\r'

@TOKEN(reserved_regex)
def t_reserved_variant(t):
    t.type = reserved.get(t.value.lower(), 'KEYWORD')
    return t

def t_NAMESPACE(t):
    r'(owl:|rdf:|xsd:|rdfs:)'
    return t

def t_DATATYPE(t):
    r'(anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|gDay|gMonth|gMonthDay|gYear|gYearMonth|hexBinary|integer|int|language|long|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort)'
    return t

def t_especial_symbols(t):
    r'[<>\[\]{}(),=]|>=|<='
    t.type = reserved.get(t.value.lower(), 'SPECIALSYMBOL')
    return t

def t_INDIVIDUAL(t):
    r'[A-Z][a-zA-Z0-9]*[0-9]'
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

# Tratamento de erros
def t_error(t):
    error = Error.Error(t.value[0], t.lineno, find_column(t.lexer.lexdata, t))
    errors.append(error)
    t.lexer.skip(1)

lexer = lex.lex()

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    lexer.input(data)
    symbol_table = {
        "keywords": {},
        "classnames": {},
        "properties": {},
        "individuals": {},
        "namespaces": {},
        "datatypes": {},
        "cardinalities": {},
        "specialsymbols": {}
    }

    for token in lexer:
        token_type = token.type.lower()
        value = token.value.lower()
        if token_type == 'keyword' or reserved.get(value) != None:
            symbol_table['keywords'][value] = symbol_table['keywords'].get(value, 0) + 1
        elif token_type == 'classname':
            symbol_table['classnames'][value] = symbol_table['classnames'].get(value, 0) + 1
        elif token_type == 'property':
            symbol_table['properties'][value] = symbol_table['properties'].get(value, 0) + 1
        elif token_type == 'individual':
            symbol_table['individuals'][value] = symbol_table['individuals'].get(value, 0) + 1
        elif token_type == 'namespace':
            symbol_table['namespaces'][value] = symbol_table['namespaces'].get(value, 0) + 1
        elif token_type == 'datatype':
            symbol_table['datatypes'][value] = symbol_table['datatypes'].get(value, 0) + 1
        elif token_type == 'cardinality':
            symbol_table['cardinalities'][value] = symbol_table['cardinalities'].get(value, 0) + 1
        elif token_type == 'specialsymbol':
            symbol_table['specialsymbols'][value] = symbol_table['specialsymbols'].get(value, 0) + 1

    return symbol_table
