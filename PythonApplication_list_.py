
import random
from re import I

list = [random.randint(-20,20) for i in range (12)]
print(list)
par=0
for i in list:
    if i%2==0:
        par+=i
        print('par', par)
print()
odd=0
for i in list:
    if i%2!=0:
        odd+=i
        print('odd', odd)

