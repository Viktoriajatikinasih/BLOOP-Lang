from src.lexer import BloopLexer
from src.parser import BloopParser
from src.interpreter import BloopExecute
from sys import *


def open_file(filename):
    data = open(filename, "r").read()
    return data


if __name__ == '__main__':
    lexer = BloopLexer()
    parser = BloopParser()
    #interpreter = basicinterpreter
    env = {}
    if len(argv) > 1:
        data = open(argv[1])
        text = data.readlines()
        for line in text:
            #lex = lexer.tokenize(line)
            tree = parser.parse(lexer.tokenize(line))
            BloopExecute(tree, env)
    else:
        while True:
            try:
                text = input('bloop -> ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                BloopExecute(tree, env)
