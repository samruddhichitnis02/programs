import Utilities.data
import Utilities.algo_utility
n=1000
z=[ ]
k=[ ]
z=Utilities.data.prime_2D()
k= Utilities.algo_utility.prime_no(n)

for i in k:
    if(i>=0 and i<100):
       z[1].append(i)

    elif(i>=100 and i<200):
        z[3].append(i)

    elif (i >= 300 and i < 400):
        z[5].append(i)

    elif (i >= 400 and i < 500):
        z[7].append(i)

    elif (i >= 500 and i < 600):
        z[9].append(i)

    elif (i >= 600 and i < 700):
        z[11].append(i)

    elif (i >= 700 and i < 800):
        z[13].append(i)

    elif (i >= 800 and i < 900):
        z[15].append(i)

    elif (i >= 900 and i <= 1000):
        z[17].append(i)

print(z)

