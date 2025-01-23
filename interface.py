import lexer
import parser

from lexer import errors
from parser import parser
from lexer import lexer

# Cores para o terminal
RESET = "\u001B[0m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
CYAN = "\u001B[36m"
PURPLE = "\u001B[35m"
BOLD = "\u001B[1m"

separator = "========================================="

def display_symbol_table(symbol_table):
    print(BLUE + separator + RESET)
    print(GREEN + "Tabela de Símbolos:" + RESET)
    print(BLUE + separator + RESET)
    
    for items in symbol_table:
        print(items)

def display_errors():
    if errors:
        print(BLUE + separator + RESET)
        print(RED + "Erros Lexicos encontrados:" + RESET)
        print(BLUE + separator + RESET)
        for error in errors:
            print(f"\n{RED}Erro no caractere '{error.value}' na linha {error.line}, coluna {error.column}.{RESET}")
        print("\n" + BLUE + separator + RESET)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(RED + f"Arquivo '{file_path}' não encontrado." + RESET)
        return ""

def main(file_path):
    entrada = read_file(file_path)
    result = parser.parse(entrada, lexer=lexer)

if __name__ == '__main__':
    file_path = 'files/input.txt'
    main(file_path)
