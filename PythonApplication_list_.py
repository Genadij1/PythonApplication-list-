import random
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
print(list[index])





    
