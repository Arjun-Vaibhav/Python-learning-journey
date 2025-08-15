'''
==================================================================================================================
                                    LIST COMPREHENSION
==================================================================================================================
'''
#Write a Python list comprehension to generate a list containing the squares of all elements in the list number
number=[1,2,3,4,5]
square=[num**2 for num in number]
print(square)
#=================================================================================================================
#Write a Python list comprehension to convert each name in the list to uppercase.
student=['vaibhav','pavan','ajay','raj']
uppercase=[ i.upper() for i in student]
print(uppercase)
#=================================================================================================================
#You are given a dictionary containing student names and their marks:
result={'vaibhav':45,'pavan':90,'ajay':40,'raj':85}
uppercase=[name.upper() for name,marks in result.items()]
print(uppercase)
#=================================================================================================================
#Write a list comprehension to create a new list containing the squares of only even numbers from the list.
number=[1,2,3,4,5,6]
square=[i**2 for i in number if i%2==0]
print(square)
#=================================================================================================================
#Write a list comprehension to extract the names that end with 'jay'
student=['vijay','pavan','sujay','varun','ajay','vaibhav']
new=[i for i in student if i[-3:]=='jay']
print(new)
#=================================================================================================================
#Write a set comprehension to create a set of names of students who passed, assuming passing marks are 35 or above.
student={'vijay':60,'pavan':21,'sujay':90,'varun':34}
passstd={name for name,marks  in  student.items() if marks >=35 }
print(passstd)

#=================================================================================================================
'''
syntax=>
var=[exp1 if cond else exp2 for loop]
'''
#Write a list comprehension to generate a new list where:Square the number if it is even,
# Cube the number if it is odd
l=[1,2,3,4,5,6]
new_list=[i**2 if i%2==0 else i**3 for i in l]
print(new_list)
#=================================================================================================================
#Write a list comprehension to create a list where:
# The name is converted to uppercase if the student has 35 or more marks
# Otherwise, the name is converted to lowercase
result={'vaibhav':10,'pavan':90,'ajay':30,'raj':85}
up=[name.upper() if marks>=35 else name.lower() for name,marks in result.items() ]
print(up)

'''
=================================================================================================================
                                     SET COMPREHENSION
=================================================================================================================
'''
'''
ns={exp for var in iterable}
ns= {exp for in iterable if cond}
ns={exp1 if cond else exp2 for loop}
'''

#Write a set comprehension to create a set of the squares of all numbers, ensuring that each 
# square appears only once in the result.
number=[1,2,3,4,5,5,6,3]
square={num**2 for num in number}
print(square)
#=================================================================================================================
#Write a set comprehension to generate a set containing the cube of each number in the list.
num=[2,5,6,8,3]
cube={num**3 for num in number}
print(cube)
#=================================================================================================================
#Write a set comprehension to create a set of all student names converted to lowercase.
result={'VAIBHAV':45,'PAVAN':90,'AJAY':40,'RAJ':85}
lowercase={name.lower() for name,marks in result.items()}
print(lowercase)
#=================================================================================================================
#Write a set comprehension to generate a set containing the cubes of only the odd numbers from the list.
number=[1,2,3,4,5,6]
cube={i**3 for i in number if i%2!=0}
print(cube)
#=================================================================================================================
#Write a set comprehension to create a set where:For non-negative numbers (≥ 0), store their squares
#For negative numbers, store their cubes
l=[1,-2,3,-4,-5,6]
new_list={i**2 if i >=0 else i**3 for i in l}
print(new_list)
#=================================================================================================================
#Write a set comprehension to create a set of names such that:If the student has 35 or more marks, their name is converted to lowercase.If the student has less than 35 marks, their name is converted to uppercase
result={'vaibhav':10,'pavan':90,'ajay':30,'raj':85}
up={name.lower() if marks>=35 else name.upper() for name,marks in result.items() }
print(up)
#=================================================================================================================
'''
==================================================================================================================
                                     Dict COMPREHENSION
==================================================================================================================
'''
#Write a dictionary comprehension to create a dictionary where:The key is formed by concatenating the first and 
# last letter of each state name.The value is the full state name
state=['maharshtra','panjab','rajsthan','bilhar']
result={i[0]+ i[-1]:i for i in state}
print(result)
#=================================================================================================================
#Write a dictionary comprehension to create a dictionary where:Each key is a state name Each value is the number
#  of characters (length) in that state name
state=['maharshtra','panjab','rajsthan','bilhar']
result={i:len(i) for i in state}
print(result)
#=================================================================================================================
'''
syntax==> 2
nd={k:v for loop if cond}

'''
#Write a dictionary comprehension to create a dictionary where:The key is an even number from the list The value
#  is the cube of that even number
number=[1,2,3,4,5,6,7]
result={i:i**3 for i in number if i%2==0}
print(result)
#=================================================================================================================
#Write a dictionary comprehension to create a new dictionary where:Each employee’s salary is increased by 5% The
#  key remains the employee name The value is the updated salary after adding 5%
empolyee={'VAIBHAV':45000,'PAVAN':900000,'AJAY':400000,'RAJ':85000}
emp={name:salary+salary *5/100 for name,salary in empolyee.items()}
print(emp)
#=================================================================================================================
#Write a dictionary comprehension to:Increase the salary by 10% only for employees whose salary is less than or
#  equal to ₹50,000.Keep the employee name as key Use the updated salary as the value
empolyee={'VAIBHAV':45000,'PAVAN':90000,'AJAY':40000,'RAJ':85000}
emp={name:salary+salary *10/100 for name,salary in empolyee.items() if salary<=50000}
print(emp)

'''
syntax==> 3
nd={k:v   if cond else value for loop }

'''
#Write a dictionary comprehension to create a dictionary where:Each key is the number itself If the number is even, 
# the value is its square If the number is odd, the value is its cube
num=[1,2,3,4,5,6]
new={i:i**2  if i%2==0 else i**3 for i in num}
print(new)
#=================================================================================================================
#Write a dictionary comprehension to create a new dictionary where: If the salary is ₹500,000 or more, increase it 
# by 5% Otherwise, increase the salary by 10%  The key remains the employee name, and the value is the updated salary

empolyee={'VAIBHAV':45000,'PAVAN':900000,'AJAY':400000,'RAJ':85000}
new={name:salary+salary*5/100  if salary >= 500000 else salary+salary*10/100 for name,salary in empolyee.items()}
print(new)
#=================================================================================================================