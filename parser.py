import ply.yacc as yacc
from lexer import tokens

# Essa estrutura serve para armazenar a forma das classes
classes = {}

# Por enquanto só atende as classes primitivas
# TODO: Adicionar suporte para classes DEFINIDAS

def p_class_declaration(p):
    '''class_declaration : primitive_class_declaration 
                           | defined_class_declaration'''

    p[0] = p[1]

def p_defined_class_declaration(p):
    '''defined_class_declaration : CLASS CLASSNAME equivalentTo_section disjoint_section individual_section'''

    classes[p[2]] = {
        'equivalentTo': p[3],
        'disjoint': p[4],
        'individuals': p[5]
    }

    print(f"Classe definida: {p[2]}")

    p[0] = classes[p[2]]

def p_primitive_class_declaration(p):
    '''primitive_class_declaration : CLASS CLASSNAME subclass_section disjoint_section individual_section'''
    classes[p[2]] = {
        'subclass': p[3],
        'disjoint': p[4],
        'individuals': p[5]
    }
    print(f"Classe definida: {p[2]}")
    p[0] = classes[p[2]]

def p_equivalentTo_section(p):
    '''equivalentTo_section : EQUIVALENTTO CLASSNAME AND LEFTPAREN property_list RIGHTPAREN
                            | empty'''
    if len(p) == 7:
        p[0] = {
            'classname': p[2],
            'properties': p[5]
        }
    else:
        p[0] = []

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF property_list closure_list
                         | SUBCLASSOF property_list
                         | SUBCLASSOF LEFTBRACE class_name_list_comma RIGHTBRACE
                         | SUBCLASSOF class_name_list_or'''
    if len(p) == 4:
        p[0] = {
            'properties': p[2],
            'closures': p[3]
        }
    elif len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = p[2]

def p_disjoint_section(p):
    '''disjoint_section : DISJOINTCLASSES class_list
                         | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_individual_section(p):
    '''individual_section : INDIVIDUALS individual_list
                           | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_property_list(p):
    '''property_list : property_list COMMA property
                     | property'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
        
def p_closure_list(p):
    '''closure_list : closure_list COMMA closure
                    | closure'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
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

def p_property(p):
    '''property : PROPERTY SOME CLASSNAME
                | PROPERTY SOME DATATYPE
                | PROPERTY SOME NAMESPACE DATATYPE
                | PROPERTY SOME NAMESPACE DATATYPE LEFTBRACKET GREATEROREQUAL CARDINALITY RIGHTBRACKET
                | PROPERTY MIN CARDINALITY CLASSNAME
                | PROPERTY MAX CARDINALITY CLASSNAME'''

    if (len(p) == 4):
        p[0] = f"{p[1]} some {p[3]}"
    else: 
        if (p[2] == 'min'):
            p[0] = f"{p[1]} min {p[3]} {p[4]}"
        else: 
            p[0] = f"{p[1]} some {p[3]}{p[4]}"
            
def p_closure(p):
    '''closure : PROPERTY ONLY CLASSNAME
               | PROPERTY ONLY LEFTPAREN class_name_list_or RIGHTPAREN
    '''
    if len(p) == 4:
        p[0] = f"{p[1]} only {p[3]}"
    else:
        p[0] = f"{p[1]} only ({p[4]})"
        
def p_class_name_list_or(p):
    '''class_name_list_or : class_name_list_or OR CLASSNAME
                       | CLASSNAME'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]	

def p_class_name_list_comma(p):
    '''class_name_list_comma : class_name_list_comma COMMA CLASSNAME
                             | CLASSNAME'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe no final da entrada.")

parser = yacc.yacc()

