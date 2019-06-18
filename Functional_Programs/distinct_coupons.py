import random
from array import *
class Distinct():
    @staticmethod
    def coupon(n):
        return random.randrange(0,n)
    @staticmethod
    def collect_coupon(n):
        a=array('i',[ ])
        dc=0
        while(dc<n):
            cp=Distinct.coupon(n)
            if cp not in(a):
                a.append(cp)
                dc=dc+1
        print(a)
        return dc
n=int(input('Enter a  coupon number-'))
cc=Distinct.collect_coupon(n)
print(cc)