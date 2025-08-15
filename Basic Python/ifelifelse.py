'''
if elif else statement  
'''
vaibhav=int(input("Enter Vaibhav age:"))
Arjun=int(input("Enter arjun age:"))
Tushar=int(input("Enter Tushar age:"))
if vaibhav > Arjun and vaibhav > Tushar:
    print("vaibhav id begger than arjun and tushar")
elif Arjun > vaibhav and Arjun > Tushar:
    print("tushar")
else:
    print("tushar is bigger than vaibha and arjun")
#==============================================================================================

number=int(input("Enter any number:"))
if number==0:
    print("number is zero")
elif number >0 :
    print("number is positive")
else:
    print("number is negative")
#==============================================================================================
age=int(input("Enter age:"))
if age > 60:
    print("senior citizenn:")
elif age > 35:
    print("adult")
else:
    print("child")    
#==============================================================================================
mark=int(input("Enter your:"))
if mark >=90:
    print("O")
elif mark >= 80:
    print("A+")
elif mark >= 70:
    print("A")
elif mark >=60:
    print("B+")
elif mark >=60:
    print("B")
else:
    print("C")
#==============================================================================================
data=['VAIBHAV PATIL','tejas kambale','Gauri khomane','MAYUR BORSE','mayur kamble','Saniya pathan','Rahul savant']
upperrcase=[]
lowercase=[]
titlecase=[]
cap=[]
for name in data:
    if name.isupper():
        upperrcase.append(name)
    elif name.islower():
        lowercase.append(name)
#==============================================================================================
data={'VAIBHAV PATIL':90000,'tejas kambale':30000,'Gauri khomane':80000,'MAYUR BORSE':20000,'mayur kamble':60000,
      'Saniya pathan':40000,'Rahul savant':10000}
for name,salary in data.items():
    if salary > 750000:
       increment=salary * 5/100
    elif salary >  50000:
           increment=salary * 10/100
    else:
           increment=salary * 15/100
    data[name]=salary + increment
print(data)
#==============================================================================================
operator=input("enter operator:")
num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
if operator=='+':
    result=num1 + num2
    print(result)
elif operator=='-':
    result=num1 - num2
    print(result)
elif operator=='*':
     result=num1 * num2
     print(result)
elif operator=='/':
     result=num1 / num2
     print(result)
else:
     print("invalid operator")

#==============================================================================================

    

