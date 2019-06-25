class Deque:
    def __init__(self):
        self.x=[]


    def addrear(self,a):
        for i in range(len(a)):
            self.x.append(a[i])



    def addfront(self,b):
        for i in range(len(b)):
            self.x.insert(i,b[i])
        print(self.x)


    def check(self):
        k=len(self.x)//2
        if(self.x[:k]==self.x[k:]): #slicing  of list in python is iterative
            print('palindrome')
        else:
            print('Not a Palindrome')





a=input('Enter a String-')
b=a[: :-1]
n=Deque()
n.addrear(a)
n.addfront(b)
n.check()

