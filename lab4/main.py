import sys
import TreePrinter

from Mparser import Parser
from TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "opers.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    parser = Parser()
    ast = parser.parse(text)

    typeChecker = TypeChecker()
    typeChecker.visit(ast)

    if parser.error:
        sys.exit(1)
    print(ast.printTree())
