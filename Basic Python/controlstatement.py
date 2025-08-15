'''
Conditional statement
    if statement
    if else statement
    if elif else statement
'''
#==============================================================================================    

#WAP to check number is even

num=eval(input("enter the number:"))
if num %2==0:
    print(num,"enter num is evven")
else:
    print(num,"NUM is odd")
#==============================================================================================    

#WAP to check any person is eligible for voting

age=int(input("Enter the Age:"))

if age >= 18:
    print("YES, this  Person is eligible")
else:
    print("NO, this  Person Not eligible")
#==============================================================================================    

#WAP  given list which number is even

number=[11,22,33,44,55,66,77,88]
for i in number:
    if i%2==0:
        print(i)
#==============================================================================================    

#WAP is divisible 3 nadd 4

number=[11,22,12,36,89,48,13,60,9,8]
for i in number:
    if i %4==0 and i%3==0:
        print(i)
#==============================================================================================    

#WAP to check which name  have <=5 characters        

student=['shubham','prathamesh','prem','sanket','avinash','vijay','jay','om','kunal','sujay']
for i in student:
 if len(i)<=5:
  print(i)
#==============================================================================================    

#WAP to check which name start with 's'

student=['shubham','prathamesh','prem','sanket','avinash','vijay','jay','om','kunal','sujay']

for i in student:
    if i.startswith('s'):
      print(i)
#==============================================================================================    

#WAP to check which name have at last 'jay'  

student=['shubham','prathamesh','prem','sanket','avinash','vijay','jay','om','kunal','sujay']
for name in student:
    if name[-3:]=="jay":
        print(name)
#==============================================================================================    

#WAP to check which student have mark >=40 show with both mark and name
student={'shubham':78,'prathamesh':45,'prem':21,'sanket':31}
for i,j in student.items():
 if j>=40:
  print(i,'==>',j)
#==============================================================================================    

#WAP to check which empaloye salary is >=50000 show with name and salary
emp={'avinash':90000, 'vijay':40000, 'ajay':30000, 'om':60000, 'kunal':35000,'sujay':80000}
for name,salary in emp.items():
    if salary >=50000:
        print(name,'-->',salary) 
#==============================================================================================    

#WAP to check salary >50000 and add in data on list 
emp={'avinash':90000, 'vijay':40000, 'ajay':30000, 'om':60000, 'kunal':35000,'sujay':80000}
lists=[]
for name,salary in emp.items():
    if salary<=50000:
        lists.append(name)
print(lists)
#==============================================================================================    

#WAP check employee salary is <=50000 if this condition is true,that employee salary increase by 20% on it 

emp={'avinash':90000, 'vijay':40000, 'ajay':30000, 'om':60000, 'kunal':35000,'sujay':80000}

for name,salary in emp.items():
    if salary <=50000:
        salary=salary+salary * 20 /100
        print(salary)
#==============================================================================================    

