print('#1')
print('first Code')
print ("say 'hello'") 


print('#2')
age=38 
name='JAHAN'
print('{0} was years old and my name is {1} ...'.format(age,name))   
#or 
print('{age} was years old and my name is {name} ...'.format(age=age,name=name))   


print('#3')
print('{0:.5f}'.format(100/3)) 
print('{0:_^11}'.format('JAHAN'))

print('#4')  # next line front 
print('a',end='')
print('b',end='')
print('/// and')
print('a',end=' ')
print('b',end=' ')
print('c')

print('#5')
s = '''This is a multi-line string.
This is the second line.'''
print(s)
#cahr \ next line front
s = 'This is a string. \
This continues the string.'
print(s)


print('#6')
i = 5
# Error below! Notice a single space at the start of the line
print('Value is', i)
print('I repeat, the value is', i)



    
