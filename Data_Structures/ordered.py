import os
x=[ ]
y=[ ]
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self, newNode):
        fa = node(newNode)
        if self.head is None:
            self.head = fa
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = fa


    def create_list(self):
        with open('pqr.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    x.append(word)
                    self.insert(word)
            self.print_list()



    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end='')
            z=z.next
        print()



    def sort_list(self):
        for i  in range(len(x)):
            for j in range(i+1,len(x)):
                if(x[i]>x[j]):
                    t=x[i]
                    x[i]=x[j]
                    x[j]=t
        print(x)
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()

        with open('pqr.txt', 'w') as f:
            for i in(x):
                str=''.join(i)
                stri=' '
                f.write(str+stri)



l=Linked_list()
l.create_list()
l.sort_list()