x=[ ]
class node:
    #whenever this node class is called it creates a node
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

    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end='')
            z=z.next
        print()

    def search(self,d):
        if d not in x:
            x.append(d)
        elif d in x:
            x.remove(d)
        for i in range(len(x)):
            self.head=None
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()
        #print(x)
        with open('abc.txt', 'w') as f:
            for i in(x):
                str=''.join(i)
                stri=' '
                f.write(str+stri)



l=Linked_list()
l.create_list()
d=input('Enter the element to search in the list-')
l.search(d)