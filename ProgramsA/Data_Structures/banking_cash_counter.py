x = []
y=[ ]
b=[ ]

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
            self.head=fa
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=fa



    def print_list(self):
        z = self.head
        while z is not None:
            print(z.data, ' ', end=' ')
            z = z.next
        print()

    def create_list(self):
        with open('pqr.txt','r') as f:
            for line in f:
                for word in line.split():
                    x.append(word)
                    for i in range(0, len(x)):
                        x[i] = int(x[i])
                    self.insert(word)
            self.print_list()


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

        d = int(input('Enter the element to search in the list-'))
        j = int(input('Enter the element you wish to check and append to the list if not found-'))
        for i in (y):
            if(i==d):
               y.remove(i)
        if j not in y:
            y.append(j)
        for i in range(len(y)):
            for j in range(i+1,len(y)):
                if(y[i]>y[j]):
                    t=y[i]
                    y[i]=y[j]
                    y[j]=t
        for i in range(len(y)):
            self.insert(y[i])
        self.print_list()

        for i in range(0, len(y)):
            y[i] = str(y[i])
            b.append(x[i])

        with open('pqr.txt', 'w') as f:
            for i in(b):
                st=''.join(i)
                stri=' '
                f.write(st+stri)




l=Linked_list()
l.create_list()
l.order()

