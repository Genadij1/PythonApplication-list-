
import random
list = []
for i in range (13):
    list.append(random.randint(-10, 10))
print(list)
par=0
for i in list:
    if i%2==0:
        par+=i
print('par', par)

odd=0
for i in list:
    if i%2!=0:
        odd+=i
print('odd', odd)

