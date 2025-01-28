import ply.yacc as yacc
from lexer import lexer 
from parser import parser
from colorama import Fore, Back, Style, init
j = 0
from parser import property_type

def test_parser(input_data, expected_output):
    
    result = parser.parse(input_data, lexer=lexer)

    print(property_type)

    # for classItem in result:
    #     for key, value in classItem.items():
    #         print(f"{Fore.GREEN}Class: {key}")
            
    #         for internalKey in value:
    #             print(f"{Fore.BLUE}    {internalKey}")


# Teste Unitarios para classes primitivas
# Exemplo 1: Declaração de uma classe primitiva

input_data_1 = """
Class: Pizza 
 
     SubClassOf:
        hasBase some PizzaBase,
        hasCaloricContent some xsd:integer[>=0],
        hasBase only PizzaBase
             
     DisjointClasses:  
        PizzaBase, PizzaTopping 
     
      Individuals:  
        CustomPizza1, 
        CustomPizza2 
        
Class: Activity
    EquivalentTo: 
        Event
         and (participatedIn some Activity)
         and participatedIn some Resource
         and participatedIn min 1 DataCustomer
         and participatedIn min 1 DataSupplier
         and participatedIn min 2 Actor
         and composedBy exactly 1 CounterpartContribution
         and composedBy exactly 1 OfferedContribution
    SubClassOf: 
        {Class1, Class2, Class3}

Class: Actor
  
    SubClassOf: Class1 or Class2 or Class3
"""

test_parser(input_data_1, "")

# print(classes_tree)
