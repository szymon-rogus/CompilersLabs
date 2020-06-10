class Memory:

    def __init__(self, name): # memory name
        self.symbol_table = {}

    def has_key(self, name):  # variable name
        return name in self.symbol_table.keys()

    def get(self, name):         # gets from memory current value of variable <name>
        return self.symbol_table.get(name)

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.symbol_table.update({name: value})

class MemoryStack:
                                                                             
    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        if memory is not None:
            self.memory_stack = [memory]
        else:
            self.memory_stack = [Memory()]

    def get(self, name): # gets from memory stack current value of variable <name>
        for m in self.memory_stack:
            value = m.get(name)
            if value is not None:
                return value
            else:
                raise Exception("Empty memory stack!")

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        if len(self.memory_stack) >= 1:
            self.memory_stack[0].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        v = self.get(name)
        if v is None:
            self.insert(name, value)
        else:
            for m in self.memory_stack:
                new_value = m.get(name)
                if name in m.symbol_table.keys():
                    m.put(name, value)
                    break

    def push(self, memory): # pushes memory <memory> onto the stack
        self.memory_stack.insert(0, memory)

    def pop(self):          # pops the top memory from the stack
        return self.memory_stack.pop(0)

