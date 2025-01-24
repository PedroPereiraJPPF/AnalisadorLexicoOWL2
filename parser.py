import ply.yacc as yacc
from lexer import tokens

# Essa estrutura serve para armazenar a forma das classes
classes = {}
class_name = []
class_types = [[]]
n = 0
errors = {}

def p_ontology(p):
    '''ontology : ontology class_declaration 
                | class_declaration'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

    global n, class_types, class_name
    n += 1
    class_types.append([])

def p_class_declaration(p):
    '''class_declaration : primitive_class_declaration 
                           | defined_class_declaration'''
    p[0] = p[1]
    
    # Print e Manutenção
    global class_name, class_types, n

    print(f"{n+1} - Classificação da Classe: {class_name[n]}")

    classificacao = ' '.join(reversed(class_types[n]))
    print(f"{classificacao}\n.")

def p_defined_class_declaration(p):
    '''defined_class_declaration : CLASS CLASSNAME equivalentTo_section subclass_section disjoint_section individual_section
                                   | CLASS CLASSNAME equivalentTo_section disjoint_section individual_section'''   
    if len(p) == 6:
        classes[p[2]] = {
            'equivalentTo': p[3],
            'disjoint': p[4],
            'individuals': p[5]
        }
    else:
        classes[p[2]] = {
            'equivalentTo': p[3],
            'subclassOf': p[4],
            'disjoint': p[5],
            'individuals': p[6]
        }
        
    global class_name, class_types, n
    if p[2] in class_name:
        print(f"Erro: Classe {p[2]} já foi definida")
        exit(1)
    class_name.append(p[2])
    class_types[n].append("Classe Definida")

# def p_defined_class_declaration_error(p):
#     '''defined_class_declaration : CLASS error equivalentTo_section subclass_section disjoint_section individual_section
#     '''

#     global class_name, class_types, n
#     class_name.append(p[2].value)
#     class_types[n].append("Classe Definida")

#     print(f"Erro de sintaxe na linha {p[2].lineno}: Nome de classe não encontrado")

def p_primitive_class_declaration(p):
    '''primitive_class_declaration : CLASS CLASSNAME subclass_section disjoint_section individual_section'''
    classes[p[2]] = {
        'subclass': p[3],
        'disjoint': p[4],
        'individuals': p[5]
    }
    
    global class_name, class_types, n
    if p[2] in class_name:
        print(f"Erro: Classe {p[2]} já foi definida")
        exit(1)
    class_name.append(p[2])
    class_types[n].append("Classe Primitiva")

# def p_primitive_class_declaration_error(p):
#     ''' primitive_class_declaration : CLASS error subclass_section disjoint_section individual_section
#     '''

#     global class_name, class_types, n
#     class_name.append(p[2].value)
#     class_types[n].append("Classe Primitiva")

#     print(f"Erro de sintaxe na linha {p[2].lineno}: Nome de classe não encontrado")

def p_equivalentTo_section(p):
    '''equivalentTo_section : EQUIVALENTTO CLASSNAME AND defined_property_list
                            | EQUIVALENTTO defined_property_list
                            | EQUIVALENTTO individual_list_or
                            | EQUIVALENTTO LEFTBRACE individual_list RIGHTBRACE'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        if p[2] == '{':
            p[0] = p[3]
        else:
            p[0] = p[4]
        

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF CLASSNAME COMMA property_list
                        | SUBCLASSOF property_list
                        | SUBCLASSOF individual_list_or
                        | SUBCLASSOF LEFTBRACE individual_list RIGHTBRACE
                        | SUBCLASSOF CLASSNAME'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        if p[2] == '[':
            p[0] = p[3]
        else:
            p[0] = p[4]
        

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
                     | property'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 6:
        p[0] = p[1] + [p[4]]
    else:
        p[0] = [p[1]]

def p_defined_property_list(p):
    '''defined_property_list : defined_property_list AND LEFTPAREN property RIGHTPAREN
                             | defined_property_list AND property
                             | property'''
            
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 6:
        p[0] = p[1] + [p[4]]
    else:
        p[0] = [p[1]]

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
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
        
    if parser.symstack[-1].value == "{":
        if ", Enumerada" not in class_types[n]:
            class_types[n].append(", Enumerada")

def p_property(p):
    '''property : PROPERTY keyword_property CLASSNAME
                | PROPERTY keyword_property LEFTPAREN class_name_list_or RIGHTPAREN
                | PROPERTY keyword_property datatype_section
                | PROPERTY keyword_property namespace_section
                | PROPERTY keyword_restrict CARDINALITY CLASSNAME
                | PROPERTY keyword_property LEFTPAREN property RIGHTPAREN
                | LEFTPAREN property RIGHTPAREN
                | property OR property
                | property OR LEFTPAREN property RIGHTPAREN
                | property AND LEFTPAREN property RIGHTPAREN
                | property AND property
                | property ONLY property
                | property ONLY LEFTPAREN property RIGHTPAREN
                | PROPERTY PROPERTY keyword_property CLASSNAME 
                | PROPERTY PROPERTY keyword_restrict CARDINALITY CLASSNAME'''
    
    global class_types, n
    
    if len(p) == 9:
        p[0] = f"{p[1]} some {p[3]}{p[4]}[{p[6]}{p[7]}]"
    elif len(p) == 6:
        if (p[3] == "("):
            if ", Aninhada" not in class_types[n]:
                class_types[n].append(", Aninhada")
        p[0] = f"{p[1]} some ({p[4]})"
    elif len(p) == 4:
        if (p[3] == "("):
            if ", Aninhada" not in class_types[n]:
                class_types[n].append(", Aninhada") 
        p[0] = f"{p[1]} some {p[3]}"
    else: 
        if (p[2] == 'min'):
            p[0] = f"{p[1]} min {p[3]} {p[4]}"
        elif (p[2] == 'max'):
            p[0] = f"{p[1]} max {p[3]} {p[4]}"
        else: 
            p[0] = f"{p[1]} some {p[3]}{p[4]}"

def p_namespace_section(p):
    '''namespace_section : XSD XSD_NUM_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET
                        | XSD XSD_NUM_DATATYPES
                        | XSD XSD_OTHER_DATATYPES
                        | RDF RDF_DATATYPES
                        | RDFS RDFS_DATATYPES
                        | OWL OWL_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET'''

def p_datatype_section(p):
    '''datatype_section : XSD_NUM_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET
                        | XSD_NUM_DATATYPES
                        | XSD_OTHER_DATATYPES
                        | RDF_DATATYPES
                        | RDFS_DATATYPES
                        | OWL_DATATYPES LEFTBRACKET comparator_operator CARDINALITY RIGHTBRACKET'''

def p_keyword_restrict(p):
    '''keyword_restrict : MAX
        | MIN
        | EXACTLY
        | SOME'''
    
    p[0] = p[1]

def p_keyword_property(p):
    '''keyword_property : ONLY 
                 | ALL
                 | SOME
                 | VALUE
                 | NOT
                 | THAT
    '''
    global class_types, n
    if p[1] == "only" and parser.symstack[-2].value == '(':
        if ", com Axioma de Fechamento" not in class_types[n]:
            class_types[n].append(", com Axioma de Fechamento")

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
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

    if parser.symstack[-1].value == "SubClassOf:" or parser.symstack[-1].value == "EquivalentTo:":
        if ", Coberta" not in class_types[n]:
            class_types[n].append(", Coberta")
            
def p_individual_list_or(p):
    '''individual_list_or : individual_list_or OR INDIVIDUAL
                          | INDIVIDUAL'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

    if parser.symstack[-1].value == "SubClassOf:" or parser.symstack[-1].value == "EquivalentTo:":
        if ", Coberta" not in class_types[n]:
            class_types[n].append(", Coberta")

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: Símbolo esperado não encontrado")

parser = yacc.yacc()