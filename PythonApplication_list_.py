
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
for index, i in enumerate(list):
    if index%3==0:
        prod*=i
print('prod', prod)
prod_min_max = 1
min_index = list.index(min(list))
max_index = list.index(max(list))
if min_index > max_index:
    min_index, max_index = max_index, min_index
for i in list[min_index+1:max_index]:
    prod_min_max *= i
print(min_index)
print(max_index)
print("prod_min_max:", prod_min_max)
sum_between_pos = 0
pos_indexes = [i for i in range(len(list)) if list[i] > 0]
if len(pos_indexes) > 1:
    first_pos_index = pos_indexes[0]
    last_pos_index = pos_indexes[-1]
    sum_between_pos = sum(list[first_pos_index+1:last_pos_index])
    print("sum_between_pos:", sum_between_pos)
else:
    print("В масиві немає двох додатніх елементів.")





