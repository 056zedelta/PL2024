import ply.lex as lex
# Select id, nome, salario From empregados Where salario >= 820

tokens = (
    "NUM",
    "VAR",
    "ATRIB",
    "OP",
    "COMA"
)

t_NUM = r"\d+"
t_VAR = r"[a-zA-Z_]\w*"
t_ATRIB = r">=|>|<|<=|==|!="
t_OP = r"SELECT|FROM|WHERE"
t_COMA = r","

t_ignore  = ' \t'

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = """
SELECT id,nome,salarios
FROM empregados
WHERE salario >= 820"""

lexer.input(data)

while tok  := lexer.token():
    #print(tok)
    print(tok)
