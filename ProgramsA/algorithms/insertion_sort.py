import Utilities.algo_utility
x = []
try:
    n = int(input('Enter the number of elements-'))
    for i in range(n):
        m=input('Enter the elements-')
        x.append(m)

    Utilities.algo_utility.i_s(x)
except:
    print('Please Enter valid inputs!')