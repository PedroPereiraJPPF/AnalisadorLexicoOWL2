import ply.yacc as yacc
from lexer import lexer 
from parser import parser
from colorama import Fore, Back, Style, init
j = 0
from parser import property_type

def test_parser(input_data, expected_output):
    
    result = parser.parse(input_data, lexer=lexer)
    
    # if result == expected_output:
    #     print(f"{Fore.GREEN + Back.BLACK}TEST PASSED!{Style.RESET_ALL}")
    #     print(f"{Fore.CYAN}Entrada:{Style.RESET_ALL}\n{input_data}")
    #     print(f"{Fore.CYAN}Resultado Esperado:{Style.RESET_ALL}\n{expected_output}")
    #     print(f"{Fore.CYAN}Resultado Obtido:{Style.RESET_ALL}\n{result}")
    #     print(f"\n{Fore.GREEN}Entrada analisada com sucesso!{Style.RESET_ALL}\n")
    # else:
    #     print(f"{Fore.RED + Back.BLACK}TEST FAILED!{Style.RESET_ALL}")
    #     print(f"{Fore.MAGENTA}Entrada:{Style.RESET_ALL}\n{input_data}")
    #     print(f"{Fore.MAGENTA}Resultado Esperado:{Style.RESET_ALL}\n{expected_output}")
    #     print(f"{Fore.MAGENTA}Resultado Obtido:{Style.RESET_ALL}\n{result}")
    #     print(f"\n{Fore.RED}Erro na análise!{Style.RESET_ALL}\n")


# Teste Unitarios para classes primitivas
# Exemplo 1: Declaração de uma classe primitiva
input_data_1 = """
Class: Pizza 
 
     SubClassOf:
        hasBase some PizzaBase, 
        hasCaloricContent some xsd:integer[>=0]
             
     DisjointClasses:  
        PizzaBase, PizzaTopping 
     
      Individuals:  
        CustomPizza1, 
        CustomPizza2 
        
Class: Activity
   
    SubClassOf: 
        {Class1, Class2, Class3}

Class: Actor
  
    SubClassOf: Class1 or Class2 or Class3
"""

test_parser(input_data_1, "")

print(property_type)
