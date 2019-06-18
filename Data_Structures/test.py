import os
class Node:

    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        fn= input("Enter the file name-")
        if (os.path.isfile(fn)):
            f = open(fn)
            data = f.read()
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node

    def print(self):
        print_list = self.head
        while print_list:
            print(print_list.data)
            print_list = print_list.next


    def search(self,x):
        pos=0
        p=self.head
        while p is not None:
            if(p.data==x):
                re
                return True
            pos=pos+1
            p=p.next
        else:
            print(x,'Not found in the list!')
            return False

    def size(self):
        i = 0
        head = self.head
        while head:
            i += 1
            head = head.next
        print(i)


MyList = LinkedList()

while True:
    print("1. Add an element")
    print("2. Print the list")
    print("3. Size of the list")
    print("4. Search an element in the list")
    menu = int(input("Choose an action:"))

    if menu == 1:
        MyList.insert(1)
    elif menu == 2:
        MyList.print()
    elif menu == 3:
        MyList.size()
    elif menu == 4:
        b=input('Enter the element you want to search-')
        MyList.search(b)