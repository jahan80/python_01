
print("#1")
try:
    print('before')
    print(7/0)
    print('after')
except:
    print('Error')

print("#2")
try:
    print('before')
    print(7 / 0)
    print('after')
except ZeroDivisionError:
    print('ZeroDivisionError')

finally:
    print("END")

