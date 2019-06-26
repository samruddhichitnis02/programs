import sys
sys.path.append('../')
import Utilities.algo_utility
from Utilities import data
s=data.Anagram()
q=[ ]
n=1000
q=Utilities.algo_utility.anagrams(n)
s.create_stack(q)
s.pop()