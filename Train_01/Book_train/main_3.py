print('#1')


def say_hello():
    print('Hello world')


say_hello()

print('#2')


def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# directly pass literal values
print_max(3, 4)
x = 5
y = 5
# pass variables as arguments
print_max(x, y)

print('#3')
x = 50


def func_local_var(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func_local_var(x)
print('x is still', x)


def func_global_var():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)


func_global_var()
print('Value of x is', x)

print('#4')

def say(message, times=1):
    print(message * times)


say('jahan_')
say('jahan_', 5)

print('#5')
def func(a, b=5, c=10):
 print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)

print('#6')
