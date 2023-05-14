class Stos:
    def __init__(self, max_size):
        self.stack = list()
        self.max_size = max_size

    def __str__(self):
        return str(self.stack) + "," + str(self.max_size)

    def push(self, element):
        if len(self.stack) < self.max_size:
            self.stack.append(element)

    def pop(self):
        if self.stack:
            return self.stack.pop()