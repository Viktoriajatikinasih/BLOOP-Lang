 #######################################
# IMPORTS
#######################################

from sly import Lexer


class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN,
              ELSE, FOR, FUN, TO, ARROW, EQEQ, PRINT}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Mendefinisikan token
    IF = r'IDZA'
    THEN = r'IDZAN'
    ELSE = r'AKHAR'
    FOR = r'LI'
    FUN = r'WAZIFA'
    TO = r'ILA'
    PRINT = r'TOBAA'
    ARROW = r'->'
    NAME = r'[A-Za-z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'
    
     
    def error (self, t) :
        print ("illegal character '%s'" % t.value[0])
        self.index += 1
        
    if __name__ == '__main__':
        lexer = BasicLexer()
        env   = {}
        while True:
            try:
                text = input('basic > ')
            except EOFError:
                break
            if text:
                lex = lexer.tokenize(text)
                for token in lex:
                    print(token)
    
