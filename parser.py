import ply.yacc as yacc
from lexer import tokens

# Essa estrutura serve para armazenar a forma das classes
classes = {}

# Por enquanto só atende as classes primitivas
# TODO: Adicionar suporte para classes DEFINIDAS

def p_class_declaration(p):
    '''class_declaration : CLASS CLASSNAME subclass_section disjoint_section individual_section'''
    classes[p[2]] = {
        'subclass': p[3],
        'disjoint': p[4],
        'individuals': p[5]
    }
    print(f"Classe definida: {p[2]}")
    p[0] = classes[p[2]]

def p_subclass_section(p):
    '''subclass_section : SUBCLASSOF property_list
                         | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_disjoint_section(p):
    '''disjoint_section : DISJOINTCLASSES class_list
                         | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_individual_section(p):
    '''individual_section : INDIVIDUALS individual_list
                           | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_property_list(p):
    '''property_list : property_list Comma property
                     | property'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_class_list(p):
    '''class_list : class_list Comma CLASSNAME
                  | CLASSNAME'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_individual_list(p):
    '''individual_list : individual_list Comma INDIVIDUAL
                       | INDIVIDUAL'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_property(p):
    '''property : PROPERTY SOME CLASSNAME
                | PROPERTY SOME DATATYPE
                | PROPERTY SOME NAMESPACE DATATYPE
                | PROPERTY MIN CARDINALITY CLASSNAME
                | PROPERTY MAX CARDINALITY CLASSNAME'''

    if (len(p) == 4):
        p[0] = f"{p[1]} some {p[3]}"
    else: 
        if (p[2] == 'min'):
            p[0] = f"{p[1]} min {p[3]} {p[4]}"
        else: 
            p[0] = f"{p[1]} some {p[3]}{p[4]}"

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe no final da entrada.")

parser = yacc.yacc()

