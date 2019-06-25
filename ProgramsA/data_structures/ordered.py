x=[ ]
b=[ ]
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
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

    def create_list(self):
        with open('pqr.txt','r') as f:
            for line in f:
                for word in line.split():
                    x.append(word)
                    for i in range(0, len(x)):
                        x[i] = int(x[i])
                    self.insert(word)
            self.print_list()

    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end='')
            z=z.next
        print()


    def order(self):
        for i in range(len(x)):
            self.head = None

        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if(x[i]>x[j]):
                    t=x[i]
                    x[i]=x[j]
                    x[j]=t

        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()

        d=int(input('Enter the element to search in the list-'))


        if d not in x:
            x.append(d)
        elif d in x:
            x.remove(d)

        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if(x[i]>x[j]):
                    t=x[i]
                    x[i]=x[j]
                    x[j]=t

        for i in range(len(x)):
            self.head = None
        for i in range(len(x)):
            self.insert(x[i])
        self.print_list()

        for i in range(0, len(x)):
            x[i] = str(x[i])
            b.append(x[i])

        with open('pqr.txt', 'w') as f:
            for i in  range(len(b)):
                st = ''.join(b[i])
                stri = ' '
                f.write(st + stri)


l=linked_list()
l.create_list()
l.order()