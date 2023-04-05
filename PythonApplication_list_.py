
from pydoc import importfile
import random
from re import I
list = []
for i in range (13):
    list.append(random.randint(-10, 10))
print(list)
s = 0
for i in list:
    if i < 0:
        s += i
print("sum negative", s)
s_2 = 0
for i in list :
    if i%2 == 0:
        s_2 += i
print("sum pair", s_2)
n=0
for i in list :
    if i%2 != 0:
        n += i
print("sum unpaired", n)
prod = 1
for index, i in enumerate(list):
    if index%3==0:
        prod*=i
        print(i)
print('prod', prod)
prod_min_max=1
min_n = min(list)
max_n = max(list)
print(min_n)
print(max_n)
while min_n < i:
    print(i)
    break


