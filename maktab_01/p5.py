
print('#1')

p1_name = 'mohammad'
p1_lastname='jahangiri'

p2_name='parsa'
p2_lastname='jahangiri'

print(p1_name)


print('#2')

class person:
    pass

p1=person()
print(p1)

print('#3')
p1.name='mohammad'
p1.lastname='jahangiri'
print(p1.name)

try:
    print(p1.email)
except :
    print('error')