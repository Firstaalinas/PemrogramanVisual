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


stack = Stack()
string = "tata"
for i in string:
    stack.push(i)

reversed_string = ""
for i in range(len(string)):
    reversed_string += stack.pop()

if string == reversed_string:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')
