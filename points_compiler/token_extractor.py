import re
from operator import indexOf


#### DEFINITIONS #####
declarator = r":[_A-Za-z][A-Za-z0-9]*:"
literals = r"\"[A-Za-z0-9\;\,\.\-\:\^\*\ ]*\""
variables = r"[A-Za-z][A-Za-z0-9_]*"
functional_symbols = [
    {
        "name":"open_parentheses",
        "matcher":r"\("
    },
    {
        "name":"close_parentheses",
        "matcher":r"\)"
    },
    {
        "name":"open_curly",
        "matcher":r"\{"
    },
    {
        "name":"close_curly",
        "matcher":r"\}"
    },
    {
        "name":"equals_assign",
        "matcher":r" :=: "
    },
        {
        "name": "string",
        "converts_to":str,
        "matcher":r"string "
    },
    {
        "name": "int",
        "converts_to": int,
        "matcher": r"int "
    },
    {
        "name": "float",
        "converts_to": float,
        "matcher": r"float "
    },
    {
        "name": "semicolon",
        "converts_to": '\n',
        "matcher": r";"
    }
]
variable_types = [
    {
        "name": "string",
        "converts_to":str,
        "matcher":r"string "
    },
    {
        "name": "int",
        "converts_to": int,
        "matcher": r"int "
    },
    {
        "name": "float",
        "converts_to": float,
        "matcher": r"float "
    }
]
################################################################
def filler_inLine(found_group, line, lines):
    filler = ""
    indexToReplace = indexOf(lines,line)
    for i in range(0,len(found_group)):
        filler+=" "
    line = line.replace(found_group,filler)
    lines[indexToReplace] = line
    return line, lines

def token_extractor(lines):
    
    stack = []
    for index in range(0,len(lines)):
        #* Define a linha a ser analisada
        line = lines[index]
        #* Encontra comentários de uma linha
        #found_comment = re.search(comment, line)
        #if found_comment:
        #   line, lines = filler_inLine(found_comment.group(),line,lines)
        #   print(line)
        #* Encontra um literal
        found_literal = re.search(literals,line)
        if found_literal:
            stack.append(
                {
                    'line': indexOf(lines,line),
                    'position': found_literal.span(),
                    'match': found_literal.group()
                }
            )
            line, lines = filler_inLine(found_literal.group(), line, lines)
        
        #* Encontra um declarador
        found_declarator = re.search(declarator,line)
        if found_declarator:
            stack.append(
                {
                    'line': indexOf(lines,line),
                    'position': found_declarator.span(),
                    'match': found_declarator.group()
                }
            )
            line, lines = filler_inLine(found_declarator.group(),line,lines)
        
        #* Simbolos Funcionais
        for functional_symbol in functional_symbols:
            found_functional_symbol = re.search(functional_symbol["matcher"], line)
            if found_functional_symbol:
                stack.append(            {
                    'line': indexOf(lines,line),
                    'position': found_functional_symbol.span(),
                    'match': found_functional_symbol.group()
                })
                line, lines = filler_inLine(found_functional_symbol.group(),line,lines)
                
        #* Encontra uma variavel
        found_variable = re.search(variables,line)
        if found_variable:
            stack.append(            {
                'line': indexOf(lines,line),
                'position': found_variable.span(),
                'match': found_variable.group()
            })
            line, lines = filler_inLine(found_variable.group(),line,lines)
            
    for line_number in range(0,len(lines)):
        if len(lines[line_number].strip()) != 0:
            raise SyntaxError(f"Error at line {line_number}")
    return stack

def token_extractor_from_file(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    tokens = token_extractor(lines)
    print('=====TOKENS======')
    print(tokens)
    print('=================')