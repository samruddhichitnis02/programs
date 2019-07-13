import sys
sys.path.append('../')
import  Utilities.data
import Utilities.algo_utility
n=1000
z=[ ]
k=[ ]
b=[ ]
a=[ ]
z=Utilities.data.anagram_2D()
k= Utilities.algo_utility.anagrams(n)
b=Utilities.algo_utility.prime_no(n)


for i in range(0, len(k)):
    k[i] = int(k[i])
    a.append(k[i])

for i in a:
    z[0].append(i)

for i in b:
    if(i not in a):
        z[1].append(i)
print(z)