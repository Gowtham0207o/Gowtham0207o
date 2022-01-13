# def addition(a,b):
#     return a+b
# def subtraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     if a==0 or b==0:
#         print("invalid operation")
#     else:
#         return a/b
# def modules(a,b):
#     return a%b
# num=int(input("enter the first num"))
# # print("""for addition press 1
# # subtraction press 2
# # multiplication press 3
# # division press 4
# # remainder press 5""")
# operation=input("enter the operation")
# num2=int(input("enter the second num"))
# op={"+":lambda x:addition(num,num2)}



# op={"+":lambda x,y:x+y,
#     "-":lambda x,y:x-y,
#     "*":lambda x,y:x*y,
#     "/":lambda x,y:x/y,
#     "%":lambda x,y:x%y,
#     "//":lambda x,y:x//y,
#     "**":lambda x,y:x**y,}
# num=int(input("enter the first num"))
# operation=input("enter the operation")
# num2 = int(input("enter the second num"))
# print("the operation of {} {} {} is {}".format(num,operation,num2,op[str(operation)](num,num2)))


def factorial(x,y=0):
    num1=0
    c=num1
    num2=1
    while [1]:
        num1=num1+num2
        num2=c
        if num1>=10:
            break
    print(num1, c, num2)
factorial(10)
