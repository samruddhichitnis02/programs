def i_i(a,n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while (j >= 0 and key < a[j]):
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    print(a)


def b_i(a,n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)


def binary_search(a,low,high,y):
    if(high>=low):
        mid=low+((high-low)//2)
        if(a[mid]==y):
            return mid
        elif (a[mid]>y):
            return binary_search(a,low,mid-1,y)
        else:
            return binary_search(a,mid+1,high,y)
    else:
        return -1






def bi_s(x):
    x.sort()
    m = ''.join(x)
    print(m)



def i_s(x):
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while(j>=0 and key<x[j]):
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
    m=''.join(x)
    print(m)


def b_s(a, low, high, y):
    if (high >= low):
        mid = low + ((high - low) // 2)
        if (a[mid] == y):
            return mid
        elif (a[mid] > y):
            return b_s(a, low, mid - 1, y)
        else:
            return b_s(a, mid + 1, high, y)
    else:
        return -1