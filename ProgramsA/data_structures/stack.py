import sys

sys.path.append('../')
import Utilities
from Utilities import data
try:
    s = data.Stack()
    expression = input('Enter the expression: ')
    if('{' or '[' or '(' in expression):
        balanced = False
        for c in expression:
            if (c == '(' or c == '{' or c == '['):
                s.push(c)
            elif (c == ')'):
                if s.is_empty():
                    balanced = False
                    break
                else:
                    for i in s.items:
                        if (i == '('):
                            continue
                    s.pop()
            elif (c == '}'):
                if s.is_empty():
                    balanced = False
                    break
                else:
                    for i in s.items:
                        if (i == '{'):
                            continue
                    s.pop()
            elif (c == ']'):
                if s.is_empty():
                    balanced = False
                    break
                else:
                    for i in s.items:
                        if (i == '['):
                            continue
                    s.pop()

        else:
            if s.is_empty():
                balanced = True
            else:
                balanced = False
        if balanced:
            print('The expresssion has balanced parentheses')
        else:
            print('The expression does not have balanced parentheses!')
    else:
        print('The expression should include paranthesis also!')
except:
    print('There should be paraenthesis in your expression!')