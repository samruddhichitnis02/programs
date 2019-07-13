class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def insert(self,newnode):
        fa=node(newnode)
        if self.head is None:
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


    def insert_at_end(self,a):
        z=self.head
        while z.next is not None:
            z=z.next
        fa = node(a)
        temp = fa
        z.next=temp
        self.print_list()

    def addNode(self, data):

        temp = self.head
        if temp is None:
            fa = node(data)
            self.head = fa
            return

        if temp.data > data:
            fa = node(data)
            fa.next = temp
            self.head = fa
            return

        while temp.next is not None:
            if temp.next.data > data:
                break
            temp = temp.next
        fa = node(data)
        fa.next = temp.next
        temp.next = fa
        return


    def delete_node(self,a):
        z=self.head
        while z is not None:
            if(z.data==a):
                prev.next=z.next
                z.next=None
                break
            prev=z
            z=z.next
        self.print_list()


    def search(self,a):
        z=self.head
        while z is not None:
            if(z.data==a):
                return True
            z=z.next
        return False

    def write_to_file(self):
        try:
            print( )
            fn=input('Enter the file you entered first-')
            with open(fn,'w') as f:
                z=self.head
                while z is not None:
                    str=' '
                    f.write(z.data+str)
                    z=z.next
            f.close()
        except:
            print('Error!')

    def write_file(self):
        print()
        x=[ ]
        fn=input('Enter the file you entered first-')
        with open(fn,'w') as f:
            z=self.head
            while z is not None:
                x.append(z.data)
                z=z.next
            for i in range(len(x)):
                x[i]=str(x[i])
                stri=' '
                f.write(stri+x[i])
        f.close()




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
class node_angram: #create node to implement stack using linked list
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


    def dequeue(self,x): #to delete the users when their transaction is completed
        if(len(x)>0):
            x.pop()

#Queue Anagram
class node_anagram: #create the node to implement Queue using Linked list
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
def cal(y,m,d):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

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

    return d0


#Hashing Function to search  a Number in slot
class Node_slot:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_slot:
    y=[ ]
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

    def delete_list(self):
        z=self.head
        while z:
            prev=z.next
            del z.data
            z=prev

    def search(self,y):
        q=[ ]
        a=int(input('Enter the element to search-'))
        if a in y:
            y.remove(a)
        elif a not in y:
            y.append(a)

        for i in range(0, len(y)):
            y[i] = str(y[i])
            q.append(y[i])

        with open('numbers.txt', 'w') as f: #enter the new data to the file
            for i in range(len(q)):
                st = ''.join(q[i])#convert list to string
                stri = ' '
                f.write(st + stri)
        return y
