
import random
list = []
for i in range (12):
    list.append(random.randint(-10, 10))
print(list)
par=0
for i in list:
    if i%2==0:
        par+=1
print('par', par)

odd=0
for i in list:
    if i%2!=0:
        odd+=1
print('odd', odd)

