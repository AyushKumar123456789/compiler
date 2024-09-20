class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

def parser(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token_type, token_value = tokens[i]
        
        if token_type == 'ID':
            if tokens[i+1][0] == 'ASSIGN':
                # Simple assignment node: ID = NUMBER
                ast.append(ASTNode(
                    'assignment', 
                    children=[ASTNode('variable', value=tokens[i][1]), 
                              ASTNode('constant', value=tokens[i+2][1])]
                ))
                i += 4  # Skip over 'ID', '=', 'NUMBER', 'SEMICOLON'
        i += 1
    return ast
