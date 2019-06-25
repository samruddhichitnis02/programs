x=[ ]
y=[ ]
class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None

    def push(self,newnode):
        fa=node(newnode)
        if self.head is None:
            self.head=fa

        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=fa

    def create_list(self,y):
      for i in y:
          self.push(i)
      self.print_list()


    def reverse_list(self,y):
        temp=0
        q=self.head
        for i in range(len(y)):
            while q is not None:
                temp=q.data
                q.data=q.next.data
                q.next.data=temp
            q=q.next



    def print_list(self):
        z=self.head
        while z is not None:
            print(z.data,' ',end=' ')
            z=z.next
        print()




n=1000
for i in range(2,n):
    k=0
    for j in range(2,i//2+1):
        if(i%j==0):
            k=k+1
    if(k<=0):
        x.append(i)

m=','.join(map(str,x))
a=m.split(',')
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(sorted(a[i])==sorted(a[j])):
            y.append(a[i])
            y.append(a[j])
#print(y)
l=linked_list()
l.create_list(y)
l.reverse_list(y)