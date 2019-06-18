import os
x=[ ]
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        fa=node(newNode)
        if self.head is None:
            self.head=fa
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=fa




    def create_list(self):
        with open('abc.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    x.append(word)
                    self.insert(word)
            self.print_list()
                #print(x)
    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end='')
            z=z.next
        print()

    def search(self,d,j):
        for i in (x):
            if(i==d):
               x.remove(i)
        if j not in x:
            x.append(j)
        #print(x)
        for i in (x):
            self.insert(i)
        self.print_list()




l=Linked_list()
l.create_list()
d=input('Enter the element to search-')
j=input('Enter the element you wish to check-')
l.search(d,j)