import ply.yacc as yacc
from lexer import tokens

RESET = "\u001B[0m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
CYAN = "\u001B[36m"
PURPLE = "\u001B[35m"
BOLD = "\u001B[1m"

# Essa estrutura serve para armazenar a forma das classes
classes = {}
class_name = []
class_types = [[]]
current_class_name = ""
property_state = {
    'open': None,
    'closed': []
}
property_type = {
    'dataproperty': [],
    'objectproperty': []
}

n = 0
errors = {}

def p_ontology(p):
    '''ontology : ontology class_declaration 
                | class_declaration'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

    global n, class_types, class_name, property_state
    n += 1
    class_types.append([])
    property_state = {
        'open': None,
        'closed': []
    }

def p_class_declaration(p):
    '''class_declaration : primitive_class_declaration 
                           | defined_class_declaration'''
    p[0] = p[1]

    global class_name, class_types, n, property_type

    print(BLUE + f"{n+1} - Classe: {class_name[n]}" + RESET)

    classificacao = ''.join(reversed(class_types[n]))
    print(f"Tipos:{GREEN} {classificacao} {RESET}")
    print(f"{BLUE}Propriedades: {RESET}")
    print(f"{PURPLE}     Data properties: {RESET}\n         {property_type['dataproperty']}")
    print(f"{PURPLE}     Object properties: {RESET}\n         {property_type['objectproperty']} {RESET}")

    print()

    property_type = {
        'dataproperty': [],
        'objectproperty': []
    }

def p_defined_class_declaration(p):
    '''defined_class_declaration : CLASS CLASSNAME equivalentTo_section subclass_section disjoint_section individual_section
                                   | CLASS CLASSNAME equivalentTo_section disjoint_section individual_section'''   
    
    if len(p) == 6:
        classes[p[2]] = {
            'equivalentTo': p[3],
            'disjoint': p[4],
            'individuals': p[5]
        }

        p[0] = {p[2]: [
            p[3],
            p[4],
            p[5]
        ]}
    else:
        classes[p[2]] = {
            'equivalentTo': p[3],
            'subclassOf': p[4],
            'disjoint': p[5],
            'individuals': p[6]
        }

        p[0] = {p[2]: [
            p[3],
            p[4],
            p[5],
            p[6]
        ]}

    global class_name, class_types, n
    if p[2] in class_name:
        print(RED + f"Erro: Classe {p[2]} já foi definida" + RESET)
    class_name.append(p[2])
    class_types[n].append("Classe Definida")

def p_primitive_class_declaration(p):
    '''primitive_class_declaration : CLASS CLASSNAME subclass_section disjoint_section individual_section'''
    
    classes[p[2]] = {
        'subclass': p[3],
        'disjoint': p[4],
        'individuals': p[5]
    }

    p[0] = {p[2]: [
        {"Subclass:": p[3]},
        {"Disjoint:": p[4]},
        {"Individual:": p[5]}
    ]}

    global class_name, class_types, n
    if p[2] in class_name:
        print(RED + f"Erro: Classe {p[2]} já foi definida" + RESET)
    class_name.append(p[2])
    class_types[n].append("Classe Primitiva")

def p_equivalentTo_section(p):
    '''equivalentTo_section : EQUIVALENTTO CLASSNAME AND defined_property_list
                            | EQUIVALENTTO defined_property_list
                            | EQUIVALENTTO individual_list_or
                            | EQUIVALENTTO LEFTBRACE individual_list RIGHTBRACE'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        if isinstance(p[4], list):
            p[0] =  [p[2], p[3]] + p[4]
        else:
            p[0] = [p[2]] + p[3] + [p[4]]

def p_equivalentTo_section_error(p):
    '''equivalentTo_section : EQUIVALENTTO CLASSNAME CLASSNAME'''

    print(RED + f"Erro: O EquivalentTo deve ter individuos não classes no corpo" + RESET)
        

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF CLASSNAME COMMA property_list
                        | SUBCLASSOF property_list
                        | SUBCLASSOF individual_list_or
                        | SUBCLASSOF LEFTBRACE individual_list RIGHTBRACE
                        | SUBCLASSOF CLASSNAME'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        if isinstance(p[3], list):
            p[0] = [p[2]] + p[3] + [p[4]]
        else:
            p[0] = [p[2], p[3]] + p[4]
    
        

def p_disjoint_section(p):
    '''disjoint_section : DISJOINTCLASSES class_list
                         | DISJOINTWITH class_list 
                         | '''
    p[0] = p[2] if len(p) > 2 else []

def p_individual_section(p):
    '''individual_section : INDIVIDUALS individual_list
                           | '''
    p[0] = p[2] if len(p) > 2 else []

def p_property_list(p):
    '''property_list : property_list COMMA LEFTPAREN property RIGHTPAREN
                     | property_list COMMA property
                     | property_list COMMA closure_section
                     | property_list COMMA LEFTPAREN closure_section RIGHTPAREN
                     | property'''
    if len(p) == 6:
        p[0] = p[1] + [p[2]] + [p[3]] + [p[4]] + [p[5]]
    elif len(p) == 4:
        p[0] = p[1] + [p[2]] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_defined_property_list(p):
    '''defined_property_list : defined_property_list AND LEFTPAREN property RIGHTPAREN
                             | defined_property_list AND property
                             | defined_property_list AND closure_section
                             | defined_property_list AND LEFTPAREN closure_section RIGHTPAREN
                             | property''' 
    if len(p) == 6:
        p[0] = p[1] + [p[2]] + [p[3]] + [p[4]] + [p[5]]
    elif len(p) == 4:
        p[0] = p[1] + [p[2]] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_closure_section(p):
    '''closure_section : PROPERTY ONLY CLASSNAME
                       | PROPERTY ONLY LEFTPAREN class_name_list_or RIGHTPAREN
    '''
                       
    global class_types, n, property_state
    
    if ", com Axioma de Fechamento" not in class_types[n]:
        class_types[n].append(", com Axioma de Fechamento")
    
    if p[1] == property_state["open"]:
        property_state["closed"].append(property_state["open"])
        property_state["open"] = None
    elif p[1] in property_state["closed"]:
        print(RED + f"Erro: Propriedade {p[1]} já foi fechada" + RESET)
    elif property_state["open"] == None:
        print(RED + f"Erro: Nenhuma propriedade aberta no momento" + RESET)
    elif p[1] != property_state["open"]:
        print(RED + f"Erro: Propriedade {property_state['open']} está aberta, o fechamento deve se destinar primeiramente a ela" + RESET)
        
    if len(p) == 6:
        p[0] = [p[1], p[2], p[3]] + p[4] + [p[5]]
    else:
        p[0] = [p[1], p[2], p[3]]
        

def p_class_list(p):
    '''class_list : class_list COMMA CLASSNAME
                  | CLASSNAME'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_individual_list(p):
    '''individual_list : individual_list COMMA INDIVIDUAL
                       | INDIVIDUAL'''    
    if len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[2], p[3]]
        else:
            p[0] = [p[1], p[2], p[3]]
    else:
        p[0] = [p[1]]
        
    if parser.symstack[-1].value == "{":
        if ", Enumerada" not in class_types[n]:
            class_types[n].append(", Enumerada")

def p_property(p):
    '''property : PROPERTY keyword_property CLASSNAME
                | PROPERTY keyword_property datatype_section
                | PROPERTY keyword_property namespace_section
                | LEFTPAREN property RIGHTPAREN
                | PROPERTY keyword_restrict CARDINALITY CLASSNAME
                | PROPERTY keyword_property LEFTPAREN property RIGHTPAREN
                | PROPERTY keyword_property LEFTPAREN class_name_list_or RIGHTPAREN
                | property OR property
                | property AND property
                | closure_section
    '''
    
    global class_types, n, property_type, property_state
    
    if p[1] not in property_state["closed"]:
        if type(p[1]) == str and p[1] != '(':
            property_state["open"] = p[1]
    elif p[1] in property_state["closed"]:
        print(RED + f"Erro: Propriedade {p[1]} já foi fechada" + RESET)

    if len(p) == 6:
        p[0] = [p[1], p[2], p[3]] + p[4] + [p[5]]

        if (p[3] == "("):
            if ", Aninhada" not in class_types[n]:
                class_types[n].append(", Aninhada")
    if len(p) == 5:
        p[0] = [p[1], p[2], p[3], p[4]]

        if (not (getFirstWord(p[0]) in property_type['objectproperty'])
            and not getFirstWord(p[0]) in property_type['dataproperty']):
            property_type["objectproperty"].append(getFirstWord(p[0]))
    elif len(p) == 4:
        if isinstance(p[3], list):
            p[0] = [p[1], p[2]] + p[3]
        else:
            p[0] = [p[1], p[2], p[3]]

        if getLastWord(p[0])[0].isupper():
            if (not (getFirstWord(p[0]) in property_type['objectproperty'])
                and not getFirstWord(p[0]) in property_type['dataproperty']):

                property_type['objectproperty'].append(getFirstWord(p[0]))
        else:
            if (not getFirstWord(p[0]) in property_type['objectproperty']
                and not getFirstWord(p[0]) in property_type['dataproperty']):

                property_type['dataproperty'].append(getFirstWord(p[0]))

        if (p[3] == "("):
            if ", Aninhada" not in class_types[n]:
                class_types[n].append(", Aninhada") 
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = [p[1], p[2], p[3], p[4]]

def p_namespace_section(p):
    '''namespace_section : XSD XSD_NUM_DATATYPES
                        | XSD XSD_OTHER_DATATYPES
                        | RDF RDF_DATATYPES
                        | RDFS RDFS_DATATYPES
                        | XSD XSD_NUM_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET
                        | OWL OWL_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET'''
    
    if len(p) == 3:
        p[0] = [p[1], p[2]]
    else:
        p[0] = [p[1], p[2], p[3], p[4], p[5], p[6]]

def p_datatype_section(p):
    '''datatype_section : XSD_NUM_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET
                        | XSD_NUM_DATATYPES
                        | XSD_OTHER_DATATYPES
                        | RDF_DATATYPES
                        | RDFS_DATATYPES
                        | OWL_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET'''
    
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = [p[1], p[2], p[3], p[4], p[5]]

def p_keyword_restrict(p):
    '''keyword_restrict : MAX
        | MIN
        | EXACTLY
        | SOME'''
    
    p[0] = p[1]

def p_keyword_property(p):
    '''keyword_property :  ALL
                 | SOME
                 | VALUE
                 | NOT
                 | THAT
    '''

    p[0] = p[1]

    # global class_types, n
    # if p[1] == "only" and parser.symstack[-2].value == '(':
    #     if ", com Axioma de Fechamento" not in class_types[n]:
    #         class_types[n].append(", com Axioma de Fechamento")

def p_comparator_operator(p):
    '''comparator_operator : GREATEROREQUAL
                           | LESSOREQUAL
                           | LESSTHAN
                           | GREATERTHAN
                           | EQUAL
    '''
    p[0] = p[1]

def p_class_name_list_or(p):
    '''class_name_list_or : class_name_list_or OR CLASSNAME
                          | CLASSNAME'''
    if len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[2], p[3]]
        else:
            p[0] = [p[1], p[2], p[3]]
    else:
        p[0] = p[1]

    if parser.symstack[-1].value == "SubClassOf:" or parser.symstack[-1].value == "EquivalentTo:":
        if ", Coberta" not in class_types[n]:
            class_types[n].append(", Coberta")
            
def p_individual_list_or(p):
    '''individual_list_or : individual_list_or OR INDIVIDUAL
                          | INDIVIDUAL'''
    if len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[2], p[3]]
        else:
            p[0] = [p[1], p[2], p[3]]
    else:
        p[0] = [p[1]]

    if parser.symstack[-1].value == "SubClassOf:" or parser.symstack[-1].value == "EquivalentTo:":
        if ", Coberta" not in class_types[n]:
            class_types[n].append(", Coberta")

def p_error(p):
    if p:
        print(f"{RED} Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}' {RESET}")
    else:
        print("{RED} Erro de sintaxe: Símbolo esperado não encontrado {RESET}")


def getLastWord(propertyList: list):
    i = len(propertyList) - 1

    while propertyList[i] == ")" or propertyList[i] == "]":
        i -= 1

    if isinstance(propertyList[i], list):
        return getLastWord(propertyList[i])

    return propertyList[i]

def getFirstWord(propertyList: list):
    i = 0

    while propertyList[i] == "(" or propertyList[i] == "[":
        i += 1

    if isinstance(propertyList[i], list):
        return getFirstWord(propertyList[i])

    return propertyList[i]

parser = yacc.yacc()