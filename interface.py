import lexer
import parser

from lexer import errors
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

    # for category, items in symbol_table.items():
    #     print(f"\n{CYAN}{category.capitalize()}:{RESET}")
    #     print(CYAN + "-" * (len(category) + 10) + RESET)

    #     if items:
    #         for lexeme, count in items.items():
    #             print(f"{PURPLE}\tLexema: {RESET}{lexeme}")
    #             print(f"{CYAN}\t\tOcorrências: {count}{RESET}")
    #         print(YELLOW + "\t" + "-" * 30 + RESET)
    #     else:
    #         print(f"{RED}\tNenhum lexema encontrado para esta categoria.{RESET}")
    
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
    # try:
    #     result = lexer.analyze_file(file_path)
    #     display_symbol_table(result)
    #     display_errors()
    # except FileNotFoundError:
    #     print(RED + f"Arquivo '{file_path}' não encontrado." + RESET)
    entrada = """
    Class: CheesyPizza
    EquivalentTo:
    Pizza and (hasTopping some CheeseTopping)
    Individuals:
    CheesyPizza1

    Class: HighCaloriePizza
    EquivalentTo:
    Pizza and (hasCaloricContent some xsd:integer)
    """
    
    result = parser.parse(entrada, lexer=lexer)

if __name__ == '__main__':
    file_path = 'files/input.txt'
    main(file_path)
