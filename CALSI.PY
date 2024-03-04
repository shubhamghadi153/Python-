def add(x, y):
    return x + y
def sub(x, y):
    return x - y 
def mul(x, y):
    return x * y
def div(x, y):
    if y != 0:
        return x/ y
    elif x == 0:
        return 0
    else:
        return 'cannot divide by 0'


num1 = int(input('enter a num1 : '))
l1 = (input('enter a operation : '))
num2 = int(input('enter a num2 : '))

if l1 == '+':
    result =add(num1 , num2)
elif l1 == '-':
    result =sub(num1 , num2)
elif l1 == '*':
    result =mul(num1 , num2)
elif l1 == '/':
    result =div(num1 , num2)
else:
    result ='enter a valid operator'

print('ans :', result)
