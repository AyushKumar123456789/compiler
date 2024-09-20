import re

# Token Specification
token_specification = [
    ('NUMBER', r'\d+'),                 # Integer
    ('ID', r'[A-Za-z_]\w*'),            # Identifiers
    ('ASSIGN', r'='),                   # Assignment operator
    ('PLUS', r'\+'),                    # Plus symbol
    ('MINUS', r'-'),                    # Minus symbol
    ('MUL', r'\*'),                     # Multiplication symbol
    ('DIV', r'/'),                      # Division symbol
    ('SEMICOLON', r';'),                # Statement terminator
    ('SKIP', r'[ \t]+'),                # Skip spaces and tabs
    ('NEWLINE', r'\n'),                 # Line breaks
]

def lexer(code):
    tokens = []
    for tok_regex in token_specification:
        pattern, tag = tok_regex
        regex = re.compile(pattern)
        for match in re.finditer(regex, code):
            tokens.append((tag, match.group()))
    return tokens
