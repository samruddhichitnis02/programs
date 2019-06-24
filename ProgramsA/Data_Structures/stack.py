class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()


s = Stack()
expression = input('Please enter the expression: ')
balanced=False
for c in expression:
    if (c == '(' or c=='{' or c=='['):
        s.push(c)
    elif (c == ')' or c=='}' or c==']'):
        if s.is_empty():
            balanced=False
            break
        s.pop()
else:
    if s.is_empty():
        balanced=True
    else:
        balanced=False
if balanced:
    print('The expresssion has balanced parentheses')
else:
    print('The expression does not have balanced parentheses!')