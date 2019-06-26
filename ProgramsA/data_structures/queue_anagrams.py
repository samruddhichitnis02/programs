import sys
sys.path.append('../')
import Utilities.algo_utility
from Utilities import data
x=[]
n=1000
x=Utilities.algo_utility.anagrams(n)
s=data.Queue_anagram()
s.create_queue(x)
