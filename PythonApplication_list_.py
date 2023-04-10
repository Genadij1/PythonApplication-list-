import random
list = []
for i in range (13):
    list.append(random.randint(-10, 10))
print(list)
for i in list:
    if i%2==0:
        print('paired', i)
print()
for i in list:
    if i>0 and i%2 != 0:
        print('odd', i)
print()
for i in list:
    if i<0:
        print('neg', i)
print()
for i in list:
    if i>0:
        print('pos', i)