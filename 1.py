import pytest
list1 = [1,25,26,26]
list2 = [1,54,5,1,2]
num = min(len(list1), len(list2))
result = [None]*(num*2)
result[::2] = list1[:num]
result[1::2] = list2[:num]
result.extend(list1[num:])
result.extend(list2[num:])
result
print (result)
