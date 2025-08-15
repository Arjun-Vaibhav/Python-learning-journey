# num=int(input("Enter the number:"))
# if num >0:
#     print("num is positive")
# else:
#     print("Num is not positive")

#==============================================================================================
# num=int(input("Enter number"))
# if num % 5  ==0:
#     print("number is divisible by 5")
# else:
#     print("Number is not divisible by 5")
#==============================================================================================

#WAP to check number is odd or not
# num=(int(input("Enter number:")))
# if num % 2 ==1:
#     print("Number  is ODD")
# else:
#     print("number is NOT ODD")
#==============================================================================================

#WAP to check number is Negative or not
# num=(int(input("Enter the  number:")))
# if num < 0:
#     print("Number is NEGATIVE.")
# else:
#     print("Number is NOT NEGATIVE")

#==============================================================================================

#WAP to check pass or fail
# mark= int(input("Enter studentt marks:"))
# if mark >=35:
#     print("studdent is pass")
# else:
#     print("student is fail")

#==============================================================================================


# plst=[]
# nlst=[]
# numbers=[-1,2,-3,4,-5,6,-7,8,-9,10]
# for i in  numbers:
#     if i > 0:
#         plst.append(i)
#     else:
#         nlst.append(i)
# print(plst)
# print(nlst)

#==============================================================================================
# plst=[]
# nlst=[]
# numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
# for i in  numbers:
#     if i%2==0:
#         plst.append(i)
#     else:
#         nlst.append(i)
# print(plst)
# print(nlst)
#==============================================================================================
#WAP to print dict of square of numbers
# dict={}
# num=[1,5,8,9]
# for i in num:
#     square=i**2
#     dict[i]=square
# print(dict)
#==============================================================================================
# dict={}
# lst=[1,2,3,4,5]
# for i in  lst:
#     if i%2==0:
#       cube=i**2
#       dict[i]= cube
#     else:
#        square=i**3
#        dict[i]=square
# print(dict)

#==============================================================================================    

user=input("Enter any elements a to z or A to Z:")
if user in 'aeiouAEIOU':
    print("elements is vowel")
else:
    print("elements is consonant")

#==============================================================================================    

year=int(input("enter the year:"))
if (year %4==0 and year %100!=0) or year %400==0:
    print(year," is a leap year")
else:
      print(year,"is not a leap year")
#==============================================================================================