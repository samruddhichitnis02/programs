from array import *

class Merge_Sort():

    @staticmethod
    def Merge(L,R,A):
        n1=len(L)
        n2=len(R)
        
            while(i<n1 and j<n2):
                if(L[i]<=R[j]):
                    A[k]=L[i]
                else:
                    A[k]=R[j]
                    j=j+1
                k = k + 1
        while(i<n1):
            A[k]=L[i]
            k=k+1
            i=i+1
        while(j<n2):
            A[k]=R[j]
            k=k+1
            j=j+1





    @staticmethod
    def Sort(A,n):
        m=n//2
        L = array('i', [])
        R = array('i', [])
        if(n<2):
            return
        else:
            for i in range(0,m):
                L.append(A[i])
            for j in range(m,n):
                R.append(A[j])
        Merge_Sort.Sort(L,m)
        Merge_Sort.Sort(R,m)
        Merge_Sort.Merge(L,R,A)
        print(A)






A=array('i',[ ])
n=int(input('Enter the number of elements-'))
for i in range(n):
    x=int(input('Enter the elements-'))
    A.append(x)
Merge_Sort.Sort(A,n)


