import Ast as AST
FORK = u'\u251c\u2500\u2500 '
LAST = u'\u2514\u2500\u2500 '
VERTICAL = u'\u2502   '


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


def sep(ind):
    return VERTICAL * (ind - 1) + FORK * (1 if ind else 0)


def printTreeElement(element, indent):
    return element.printTree(indent) if hasattr(element, 'printTree') else sep(indent) + str(element)

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        return self.withoutLeaf(indent) if self.leaf is None else self.withLeaf(indent)

    @addToClass(AST.Node)
    def printChildren(self, children, indent):
        return map(lambda child: printTreeElement(child, indent), children)

    @addToClass(AST.Node)
    def withoutLeaf(self, indent):
        res = []
        res += self.printChildren(self.children, indent)
        return '\n'.join(res)

    @addToClass(AST.Node)
    def withLeaf(self, indent):
        res = [self.printLeaf(self.leaf, indent)]
        res += self.printChildren(self.children, indent + 1)
        return '\n'.join(res)

    @addToClass(AST.Node)
    def printLeaf(self, leaf, indent):
        return printTreeElement(leaf, indent)

    @addToClass(AST.Node)
    def printLeaves(self, indent):
        return list(map(lambda leaf: self.printLeaf(leaf, indent), self.leaf))

    @addToClass(AST.If)
    def printTree(self, indent=0):
        res = list(zip(self.printLeaves(indent), self.printChildren(self.children, indent + 1)))

        return '\n'.join(map(lambda x: '\n'.join(x), res))

    @addToClass(AST.Sequence)
    def printTree(self, indent=0):
        return self.withLeaf(indent) if len(self.children) > 1 else self.withoutLeaf(indent)


