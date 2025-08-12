
print('#1')
number=20
guess = int(input('Enter number:'))
if guess==number :
    print('''U Win !!! 
          but i not have prize!''')
elif guess<number:
    print('input num lower the target num ! so U lose')
else:
     print('input num higher er the target num ! so U lose')
print('Done')

print('#2')
if True:
    print( 'yes is true' )

print('#3')
number=22
running= True
while running :
    guess =int(input ('Enter num'))
    if guess==number:
        print('u win!!')
        running=False
    elif guess<number :
        print('input<number')
    else :
        print('input>number')
else :
    print('The while loop is over.')

print('Done')


print('#4')
for i in range(1,3):
    print(i)
else :
    print('loop is over')


print('#5')
while True:
 s = input('Enter something : ')
 if s == 'quit':
    break 
 print('Length of the string is', len(s))
print('Done')

print('#6')
while True:
 s = input('Enter something : ')
 if s == 'quit':
    break
 if len(s) < 3:
    print('Too small')
    continue  # this code is seperate up code 
 print('Input is of sufficient length')

    