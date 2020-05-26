str1=input("Enter a string: ")
from itertools import permutations
perms = [''.join(p) for p in permutations(str1)]
newperms=set(perms)
print("Permutations: ",newperms)