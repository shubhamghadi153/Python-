num1 = int(input('enter a num1 : '))
#l1 = ['+','-','*','/']
l1 = (input('enter a operation : '))
num2 = int(input('enter a num2 : '))

if l1 == '+':
    print(num1 + num2 )
elif l1 =='-':
    print(num1 - num2 )
elif l1 =='*':
    print(num1 * num2 )
elif l1 =='/':
    print(num1 / num2 )
else :
    print('Enter a valid operator ')




