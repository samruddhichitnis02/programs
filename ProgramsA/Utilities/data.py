# Unordered List
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        fa = node(newNode)
        if self.head is None:
            self.head = fa
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = fa

    def print_list(self):
        z = self.head
        while z is not None:
            print(z.data, ' ', end='')
            z = z.next
        print()

    def search(self, x, d):
        if d not in x:
            x.append(d)
        elif d in x:
            x.remove(d)
        for i in range(len(x)):
            self.head = None
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()
        # print(x)
        with open('abc.txt', 'w') as f:
            for i in (x):
                str = ''.join(i)
                stri = ' '
                f.write(str + stri)


# Ordered List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Link_list:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        fa = Node(newNode)
        if self.head is None:
            self.head = fa
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = fa



    def print_list(self):
        z = self.head
        while z is not None:
            print(z.data, ' ', end='')
            z = z.next
        print()

    def order(self, x, b):
        for i in range(len(x)):
            self.head = None
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if (x[i] > x[j]):
                    t = x[i]
                    x[i] = x[j]
                    x[j] = t
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()

        d = int(input('Enter the element to search in the list-'))
        if d not in x:
            x.append(d)
        elif d in x:
            x.remove(d)
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if (x[i] > x[j]):
                    t = x[i]
                    x[i] = x[j]
                    x[j] = t
        for i in range(len(x)):
            self.head = None
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()
        for i in range(0, len(x)):
            x[i] = str(x[i])
            b.append(x[i])

        with open('pqr.txt', 'w') as f:
            for i in range(len(b)):
                st = ''.join(b[i])
                stri = ' '
                f.write(st + stri)


# Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()


# Palindrome Deque
class Deque:
    def __init__(self):
        self.x = []

    def addrear(self, a):
        for i in range(len(a)):
            self.x.append(a[i])

    def addfront(self, b):
        for i in range(len(b)):
            self.x.insert(i, b[i])
        print(self.x)

    def check(self):
        k = len(self.x) // 2
        if (self.x[:k] == self.x[k:]):  # slicing  of list in python is iterative
            print('palindrome')
        else:
            print('Not a Palindrome')


# Stack Anagrams
class node_angram:
    def __init__(self, data):
        self.data = data
        self.next = None


class Anagram:
    def __init__(self):
        self.head = None

    def push(self, newnode):
        fa = node(newnode)
        if self.head is None:
            self.head = fa
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = fa

    def create_stack(self, q):
        for i in q:
            self.push(i)
        self.print_stack()

    def print_stack(self):
        z = self.head
        while z is not None:
            print(z.data, ' ', end='')
            z = z.next
        print()

    def pop(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        print()
        print('Anagrams in reverse order are-')
        self.print_stack()

#Banking_cash_Counter
class Queue:
    def __init__(self):
       pass

    def enqueue(self,users,x):
        for i in range(users):
            x.append(i)


    def dequeue(self,x):
        if(len(x)>0):
            x.pop()

#Queue Anagram
class node_anagram:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue_anagram:
    def __init__(self):
        self.head=None

    def enqueue(self,newnode):
        fa=node(newnode)
        if self.head is None:
            self.head=fa

        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=fa

    def create_queue(self,x):
      for i in x:
          self.enqueue(i)
      self.dequeue()

    def dequeue(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end=' ')
            z=z.next
        print()

#prime 2D array
def prime_2D():
    a = []
    for i in range(0, 19):
        a.append([])
    k = 100
    for i in range(0, 20):
        if (i % 2 == 0):
            a[i].append(k)
            k = k + 100
    return a


