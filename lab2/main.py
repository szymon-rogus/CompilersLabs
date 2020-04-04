import sys

from Mparser import Parser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    parser = Parser()
    res = parser.parse(text)
    if parser.error:
        sys.exit(1)
    print(res)
