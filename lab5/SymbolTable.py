class VariableSymbol(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Type:
    def __eq__(self, obj):
        return type(self) is type(obj)


class String(Type):
    def __repr__(self):
        return "String"


class Numeric(Type):
    pass


class Boolean(Type):
    def __repr__(self):
        return "Boolean"


class Scalar(Numeric):
    pass


class Integer(Scalar):
    def __repr__(self):
        return "Integer"

    pass


class Float(Scalar):
    def __repr__(self):
        return "Float"

    pass


class Matrix(Numeric):
    def __init__(self, n, m, type):
        self.type = type
        self.n = n
        self.m = m

    def __repr__(self):
        return "Matrix({n}, {m}, {type})".format(n=self.n, m=self.m, type=self.type)

    def equals(self, other):
        return isinstance(other, Matrix) and self.n == other.n and self.m == other.m

    def getCommonType(self, other):
        if isinstance(other, Matrix):
            return Float() if self.type == Float() or other.type == Float() else Integer()


class Range(Type):
    def __repr__(self):
        return "Range"


class SymbolTable(object):

    def __init__(self):
        self.parent = None
        self.scope = {}

    def put(self, symbol):
        self.scope[symbol.name] = symbol

    def get(self, name):
        if self.scope.__contains__(name):
            return self.scope[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None

    def getType(self, name):
        return self.get(name).type if self.get(name) else None
