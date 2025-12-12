num1= float(input("enter the number 1:"))
num2= float(input("enter the number 2:"))
num3= float(input("enter the number 3:"))

if (num1>num2 and num1>num3):
    print("number 1 is greatest")
elif(num2>num3 and num2>num1):
    print("number 2 is greatest")
elif(num1==num2==num3):
    print('all numbers are equal')
else:
    print('number3 is greatest')

    