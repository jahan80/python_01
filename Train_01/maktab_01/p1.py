
print('#1')
list_1=[1,2,3,'jahan']
print (list_1)

print (type(list_1))

print(list_1[3])

list_1[3]='mohammad'
print(list_1[3])

print('first val is ',list_1[0]) # is firt
print('last val is ',list_1[-1]) # is last

list_1.append(80)
print(list_1)

list_1.insert(-1,'parsa')
print(list_1)

print('parsa' in list_1)

print(len(list_1))

print(list_1[2:]) # after index 2
print(list_1[:2]) # befor index 2

print(list_1[1:2]) # after 1 to 2


# tuple like  list  but not changeable
tuple_t= tuple(list_1)
print(tuple_t)

print(type((1))) #int

print(type((1,))) #tuple
