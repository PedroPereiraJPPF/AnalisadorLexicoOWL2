import ply.yacc as yacc

from lexer import tokens

def s(p):
    """
    s : CLASS CLASSNAME class_type resto
    """
    p[0] = ("Class:", p[2], p[3], p[4])

def class_type(p):
    """
    class_type : primitive
               | defined
    """
    p[0] = p[1]

def primitive(p):
    """
    primitive : SUBCLASSOF CLASSNAME prerequisiteP
              | SUBCLASSOF '{' enum_list '}'
              | SUBCLASSOF coveted_list
    """
    if len(p) == 3:
        p[0] == ("SubClassOf:", p[2])
    elif len(p) == 4:
        p[0] = ("SubClassOf:", p[2], p[3])
    elif len(p) == 5 and p[2] == '{':
        p[0] = ("SubClassOf:", p[3])
        

def prerequisiteP(p):
    """
    prerequisiteP : prerequisiteP ',' constraint closureP
                  | prerequisitePP 
                  | empty
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = (p[1])
    elif len(p) == 5:
        p[0] = p[1] + p[3] + p[4]
        
def prerequisitePP(p):
    """
    prerequisitePP : prerequisitePP ',' constraintP closurePP
                   | empty
    """
    if len(p) == 1:
        p[0] = ()
    elif len(p) == 5:
        p[0] = (p[1], p[3], p[4])
        
def constraint(p):
    """
    constraint : PROPERTY conective id
    """
    p[0] = (p[1], p[2], p[3])

def constraintP(p):
    """
    constraintP : '(' constraint ')' 
                | '(' PROPERTY conective constraintP ')'
                | '(' constraintP ')' 'or' '(' constraintP ')'
    """
    if len(p) == 4:
        p[0] = [p[2]]
    elif len(p) == 6:
        p[0] = p[2] + [p[3]] + [p[4]]
    elif len(p) == 8:
        p[0] = [p[2]] + [p[6]]

def conective(p):
    """
    conective : SOME
              | MIN CARDINALITY
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]

def closureP(p):
    """
    closureP : closureP ',' PROPERTY 'only' CLASSNAME
             | closureP ',' PROPERTY 'only' '(' coveted_list ')'
             | empty
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 6:
        p[0] = [p[1]] + p[3] + p[5]
    elif len(p) == 8:
        p[0] = [p[1]] + p[3] + [p[6]]

def closurePP(p):
    """
    closurePP : ',' '(' PROPERTY 'only' CLASSNAME ')'
              | ',' '(' PROPERTY 'only' '(' coveted_list ')'')'
    """
    if len(p) == 6:
        p[0] = p[2] + p[4]
    elif len(p) == 8:
        p[0] = p[2] + [p[5]]
    
def enum_list(p):
    """
    enum_list : enum_list ',' CLASSNAME
              | CLASSNAME
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def coveted_list(p):
    """
    coveted_list : coveted_list OR CLASSNAME
                 | CLASSNAME
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def defined(p):
    """
    defined : EQUIVALENTTO CLASSNAME AND prerequisiteD
            | EQUIVALENTTO '{' enum_list '}'
            | EQUIVALENTTO coveted_list
    """
    if len(p) == 4:
        p[0] = ("EquivalentTo:", p[3])
    elif len(p) == 5:
        p[0] = ("EquivalentTo:", p[3])

def prerequisiteD(p):
    """
    prerequisiteD : prerequisiteD AND constraintP closureD
                  | prerequisiteDP 
                  | empty
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 5:
        p[0] = [p[1]] + p[2] + [p[3]] + [p[4]]

def closureD(p):
    """
    closureD : closureD AND PROPERTY 'only' CLASSNAME
             | closureD AND PROPERTY 'only' '(' coveted_list ')'
             | empty
    """
    if len(p) == 1:
        p[0] = []
    elif len(p) == 6:
        p[0] = [p[1]] + p[2] + p[3] + p[5]
    elif len(p) == 8:
        p[0] = [p[1]] + p[2] + p[3] + [p[6]]
        
def prerequisiteDP(p):
    """
    prerequisiteDP : prerequisiteDP AND constraintP closurePP
                   | empty
    """
    if len(p) == 1:
        p[0] = ()
    elif len(p) == 5:
        p[0] = [p[1]] + p[2] + [p[3]] + [p[4]]
        
def id(p):
    """
    id : CLASSNAME
       | NAMESPACE DATATYPE
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
        
def resto(p):
    """
    resto : disjoint_classes individuals
    """
    if len(p) == 3:
        p[0] = [p[1]] + [p[2]]

def disjoint_classes(p):
    """
    disjoint_classes : DISJOINTCLASSES class_list
    """
    if len(p) == 3:
        p[0] = ("DisjointClasses:", p[2])

def class_list(p):
    """
    class_list : CLASSNAME
               | class_list ',' CLASSNAME
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
        
def individuals(p):
    """
    individuals : INDIVIDUALS individual_list
    """
    if len(p) == 3:
        p[0] = ("Individuals:", p[2])

def individual_list(p):
    """
    individual_list : INDIVIDUAL
                    | individual_list ',' INDIVIDUAL
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
        
parser = yacc.yacc()