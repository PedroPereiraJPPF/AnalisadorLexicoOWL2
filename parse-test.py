import ply.yacc as yacc
from lexer import lexer 
from parser import parser
from colorama import Fore, Back, Style, init

def test_parser(input_data, expected_output):
    
    result = parser.parse(input_data, lexer=lexer)
    
    if result == expected_output:
        print(f"{Fore.GREEN + Back.BLACK}TEST PASSED!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Entrada:{Style.RESET_ALL}\n{input_data}")
        print(f"{Fore.CYAN}Resultado Esperado:{Style.RESET_ALL}\n{expected_output}")
        print(f"{Fore.CYAN}Resultado Obtido:{Style.RESET_ALL}\n{result}")
        print(f"\n{Fore.GREEN}Entrada analisada com sucesso!{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.RED + Back.BLACK}TEST FAILED!{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Entrada:{Style.RESET_ALL}\n{input_data}")
        print(f"{Fore.MAGENTA}Resultado Esperado:{Style.RESET_ALL}\n{expected_output}")
        print(f"{Fore.MAGENTA}Resultado Obtido:{Style.RESET_ALL}\n{result}")
        print(f"\n{Fore.RED}Erro na análise!{Style.RESET_ALL}\n")


# Teste Unitarios para classes primitivas

# Exemplo 1: Declaração de uma classe primitiva
input_data_1 = """
Class: Pizza
SubClassOf:
    (hasBase some (hasIngredient some TomatoSauce))
"""
expected_output_1 = {
    'subclass': [
        'hasBase some (hasIngredient some TomatoSauce)'
    ],
    'disjoint': [],
    'individuals': []
}

test_parser(input_data_1, expected_output_1)

input_data_2 = """
Class: Burger
SubClassOf:
    FastFood,
    hasBase some BurgerBase,
    hasCaloricContent some xsd:integer[>=200],
    hasTopping min 3 BurgerTopping,
    hasTopping max 5 BurgerTopping
DisjointClasses:
    Burger, BurgerBase, BurgerTopping
Individuals:
    ClassicBurger1
"""
expected_output_2 = {
    'subclass': [
        'FastFood',
        'hasBase some BurgerBase',
        'hasCaloricContent some xsd:integer[>=200]',
        'hasTopping min 3 BurgerTopping',
        'hasTopping max 5 BurgerTopping'
    ],
    'disjoint': ['Burger', 'BurgerBase', 'BurgerTopping'],
    'individuals': ['ClassicBurger1']
}

test_parser(input_data_2, expected_output_2)

# Exemplo 3: Declaração de classe com restrições de cardinalidade
input_data_3 = """
Class: PizzaTopping
SubClassOf:
    TomatoTopping or CheeseTopping or VeggieTopping
DisjointClasses: 
    PizzaTopping, Topping
Individuals:
    TomatoTopping1,
    CheeseTopping1,
    VeggieTopping1
"""
expected_output_3 = {
    'subclass': [
        'TomatoTopping',
        'CheeseTopping',
        'VeggieTopping'
    ],
    'disjoint': ['PizzaTopping', 'Topping'],
    'individuals': ['TomatoTopping1','CheeseTopping1', 'VeggieTopping1']
}

test_parser(input_data_3, expected_output_3)

# Exemplo 4: Teste de falha de sintaxe (para garantir que erros sejam capturados)
# Teste da falha de sintaxe, os topicos de subclassOf não estão separados por vírgula
input_data_4 = """
Class: InvalidPizza
SubClassOf:
    hasBase some PizzaBase
    hasCaloricContent some xsd:integer
"""
test_parser(input_data_4, None)

# Teste de classes definidas

input_data_5 = """
Class: CheesyPizza
 EquivalentTo:
    Pizza and (hasTopping some CheeseTopping)
 Individuals:
    CheesyPizza1"""

expected_output5 = {
    'equivalentTo': 
        {'classname': 'Pizza', 'properties': ['hasTopping some CheeseTopping']},
        'disjoint': [], 'individuals': ['CheesyPizza1']
    }

test_parser(input_data_5, expected_output5)

input_data_6 = """
Class: CheesyPizza
 EquivalentTo:
    Pizza and (hasTopping some CheeseTopping)
 DisjointClasses: 
    PizzaTopping, Topping
 Individuals:
    CheesyPizza1"""

expected_output6 = {
    'equivalentTo': 
        {'classname': 'Pizza', 'properties': ['hasTopping some CheeseTopping']},
        'disjoint': ['PizzaTopping', 'Topping'], 
        'individuals': ['CheesyPizza1']
    }

test_parser(input_data_6, expected_output6)
