# Unordered List

class node:      #creation of node
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, newNode): #Linking of all the nodes created
        fa = node(newNode)
        if self.head is None:
            self.head = fa
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = fa

    def print_list(self): #printing the nodes
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

    def order(self, x, b): #sort the nodes
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

        with open('pqr.txt', 'w') as f: #enter the new data to the file
            for i in range(len(b)):
                st = ''.join(b[i])
                stri = ' '
                f.write(st + stri)


# Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self): #returns True if items is empty
        return self.items == []

    def push(self, data): #creates the stack by pushing the data at the end
        self.items.append(data)

    def pop(self): #removes the last element from the stack when called
        self.items.pop()


# Palindrome Deque
class Deque:
    def __init__(self):
        self.x = []

    def addrear(self, a): #adds the data from the back side of the queue
        for i in range(len(a)):
            self.x.append(a[i])

    def addfront(self, b): #adds the data to the front side of the queue
        for i in range(len(b)):
            self.x.insert(i, b[i])
        print(self.x)

    def check(self): #checks for the front side and back side of the queue
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

    def pop(self): #Reversing the linked list so that it can print anagrams in reverse order
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

    def enqueue(self,users,x): #To store the number of users
        for i in range(users):
            x.append(i)


    def dequeue(self,x): #to delete teh users when their transaction is completed
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

    def enqueue(self,newnode): #append all the anagrams in to the queue
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

    def dequeue(self): #dequeue the elements from the queue in the order they were entered
        z=self.head
        while z is not None:
            print(z.data,' ',end=' ')
            z=z.next
        print()

#prime 2D array
def prime_2D():
    a = []
    for i in range(0, 20):
        a.append([]) #create a main array in which other arrays will be stored
    k = 100
    for i in range(0, 20):
        if (i % 2 == 0): #Use all the even position to give the range
            a[i].append(k)
            k = k + 100
    return a

#Anagram 2D array
def anagram_2D():
    a=[]
    for i in range(0,2):
        a.append([]) #append the array inside the array
    return a

#Calender
def cal(y,m):
    a=[ ]
    for i in range(0, 7):
        a.append([])
    b = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    for i in range(0, len(b)):
        a[i].append(b[i])

    if(((y%4==0)and(y%100!=0)) or (y%400==0)): #For leap year
        p = 1
        d =[6, 9, 3, 6, 1, 4, 6, 2, 5, 7, 3, 5]
        d0 = int((y + y / 4 - y / 100 + y / 400 + d[m - 1] + p) % 7)
    else:
        p=1
        d = [0, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        d0 = int((y + y / 4 - y / 100 + y / 400 + d[m - 1] + p) % 7)

    if (d0 == 0):
        j = 0
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        elif (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif(m==2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


    elif (d0 == 1):
        j = 1
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        if (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0



    elif (d0 == 2):
        j = 2
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        if (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

    elif (d0 == 3):
        j = 3
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        if (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


    elif (d0 == 4):
        j = 4
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        elif (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


    elif (d0 == 5):
        j = 5
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        elif (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0

        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


    elif (d0 == 6):
        j = 6
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            for k in range(1, 32):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0
        elif (m == 11 or m == 4 or m == 6 or m == 9):
            for k in range(1, 31):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


        elif (m == 2):
            for k in range(1, 29):
                a[j].append(k)
                j = j + 1
                if (j == 7):
                    j = 0


    if (m == 1):
        print('January', y)
    elif (m == 2):
        print('February', y)
    elif (m == 3):
        print('March', y)
    elif (m == 4):
        print('April', y)
    elif (m == 5):
        print('May', y)
    elif (m == 6):
        print('June', y)
    elif (m == 7):
        print('July', y)
    elif (m == 8):
        print('August', y)
    elif (m == 9):
        print('September', y)
    elif (m == 10):
        print('October', y)
    elif (m == 11):
        print('November', y)
    else:
        print('December', y)
    return a


#Hashing Function to search  a Number in slot
class Node_slot:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_slot:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        fa=Node_slot(newnode)
        if self.head is  None:
            self.head=fa
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=fa

    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,end=' ')
            z=z.next
        print()

    def delete_list(self,l):
        for i in range(len(l)):
            self.head=None

    def search(self):
        a=int(input('Enter the element to search-'))