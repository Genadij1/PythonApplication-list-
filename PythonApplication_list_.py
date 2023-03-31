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
prod = 1
for i in list:
    if i%3 == 0:
        prod *= i
print("prod", prod)
prod_min_max=1
min_num = min(list)
max_num = max(list)
for i in list:
    if i > min_num and i < max_num:
        prod_min_max *= i
print("prod_min_max", prod_min_max)



    
