#type casting 

# name=int(input("enter something:"))
# print(type(name))

# num=34.78
# num=int(num)
# print(type(num))
# print(num)

# num=50
# num=float(num)
# print(type(num))
# print(num)

# # number=int(input("enter the number:"))
# # square=number**2
# # print(square)

# num='90.78'
# num=str(num)
# print(type(num))
# print(num)

# num1 = int (input("Enter the number:"))
# num2 = int(input("Enter the number:"))
# sum=num1 + num2 
# print("sum  of %d and %d is sum" %(num1, num2 ,sum))

# radius=eval(input("Enter the Radius:"))
# area= 3.14 * radius * radius
# print("area of circle=",area)

# import home  
# from main import area
# import home 
# print (area)

# print(home.name)
 
# amount = eval(input("Enter Amount:"))
# rate = eval (input("enter rate:"))
# time = eval (input("enter time into year:"))


# total_intrest= amount * rate * (time/100)
# # print(total_intrest)
# # total_SI=amount + total_intrest
# # print("total amount including intrest:",total_SI)

# # amount = eval(input("Enter Amount:"))
# # rate = eval (input("enter rate:"))
# # time = eval (input("enter time into year:"))
# # n=eval(input("enter how many time compounded"))

# # total_amount=amount*(1+((rate/100)/n))**(n*time)


# # print(total_amount)






# amount=int(input("enter amount:"))
# rate=int(input("enter rate in % :"))
# time=int(input("enter thme in year :"))

# n=eval(input("how dyas ARE YOU COMPOUNDED IN YEAR:"))

# CI= amount * (1 +(rate / 100)/n)**(n * time)
# print(CI)

# from math import pi
# radius=eval(input("Enter the Radius:"))
# area= pi* radius * radius
# print("area of circle=",area)

# '''weight=int(input("Enter Weight in kg"))
# height= eval(input("Enter height in kg"))

# BMI= weight /height**2
# print("body mask index =",BMI)'''

# salary= int(input("Enter salary:"))
# increment= eval(input("enter increment %:"))

# increment=salary * increment/100

# Net_salary=salary + increment
# print("total increment=",increment)
# print("total net salary",Net_salary)

# Principle=int(input("Enter the amount"))
# Rate=eval(input("Enter Rate in %"))
# time=int(input("enter the time in year"))
# SI=Principle * Rate/100 *time
# print("Simple interest=",SI)

n=23
if n%2!=0:
    print('Weird')
elif n % 2==0 and 2<= n <=5:
    print('Not Weird')
elif n % 2==0 and 6<= n <=20: 
    print('Weird')
elif n%2==0 and n>=20:
    print('Not Weird')