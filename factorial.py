num1=0
num2=1
def factorial(x,y=0):
    for i in range(0,x+1):
        c = num1
        num1=num1+num2
        num2=c
        print(num1,c,num2)
factorial(10)