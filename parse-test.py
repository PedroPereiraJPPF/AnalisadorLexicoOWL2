from lexer import lexer 
from parser import parser
j = 0

def test_parser(input_data, expected_output):
    
    result = parser.parse(input_data, lexer=lexer)

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
hasCaloricContent some xsd:integer
DisjointClasses:
Pizza, PizzaBase, PizzaTopping
Individuals:
CustomPizza1,
CustomPizza2

Class: CheesyPizza
EquivalentTo:
Pizza and (hasTopping some CheeseTopping)
Individuals:
CheesyPizza1
Class: HighCaloriePizza
EquivalentTo:
Pizza and (hasCaloricContent some xsd:integer[>= 400])

Class: MargheritaPizza
SubClassOf:
NamedPizza,
hasTopping some MozzarellaTopping,
hasTopping some TomatoTopping,
hasTopping only (MozzarellaTopping or TomatoTopping)

Class: SpicyPizza
EquivalentTo:
Pizza
and (hasTopping some (hasSpiciness value Hot))

Class: Spiciness
EquivalentTo: {Hot1 , Medium1 , Mild1}

Class: Spiciness
EquivalentTo: Hot or Medium or Mild

Class: RegulatoryActivity
    EquivalentTo: ValueActivity
        and ((bundles some
                (CnAObject or CoreObject or PoPObject)) or
             (consumes some CounterObject))
        and ((grants some CnAObject) or
             (transfers some
                (CoreObject or PoPObject)))
        and (isAuthorityOf some Regulator)
        and (hasTransaction some ValueTransaction)
        and (bundles only
                (CnAObject or CoreObject or PoPObject))
        and (consumes only CounterObject)
        and (grants only CnAObject)
        and (isAuthorityOf only Regulator)
        and (transfers only
                (CoreObject or PoPObject))
"""

test_parser(input_data_1, "")

# print(classes_tree)
