# Nama  : Firsta Alina S
# NIM   : 20051397085
# Kelas : 2020 A - D4 Manajemen Informatika

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


string = "Hello World"
stack = Stack()
stack2 = Stack()

for i in string:
    stack.push(i)

for i in range(len(string)):
    stack2.push(stack.pop())
print(stack2.items)
