
import random

list = [random.randint(-10,10) for i in range(12)]
print(list)
paired=0
for i in list:
    if i>0 and i%2==0:
        paired=i
        print('paired', paired)
print()
odd=0
for i in list:
    if i>0 and i%2 != 0:
        odd=i
        print('odd', odd)
print()
neg=0
for i in list:
    if i<0:
        neg=i
        print('neg', neg)
print()
pos=0
for i in list:
    if i>0:
        pos=i
        print('pos', pos)
