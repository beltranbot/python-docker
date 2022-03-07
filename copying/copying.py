"""
- shallow copy: one level deep, only references of nested child objects
- deep copy: full independent copy
"""

import copy
# one level deep -> shallow copying
org = [0,1,2,3,4]
cpy = copy.copy(org)
# cpy = org.copy() # will also work
# cpy = list(org) # will also work
# cpy = org[:] # will also work
cpy[0] = -10
print(cpy)
print(org) # the original variable is unmodified
print("### more than one level ###")
# more than one level deep
org = [[0,1,2,3,4], [5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
print(org)
print(cpy)
