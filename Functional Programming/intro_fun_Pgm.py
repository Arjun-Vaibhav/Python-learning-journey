'''
=>functional programing is a functional prandisam
=>function is resuseble block of code used to perfome a block of code
=> def is used to define function and def i a keyword
=> functionname() to used call function 


syntax:-
    def function_name (): ------function create
        block of code
    function_name -----function call    
'''

# def sum():
#     num=eval(input("Enter any number:"))
#     sq=num**2
#     print(sq)



 #WAP to caluculate div of two number
# def div ():
#     num1=5
#     num2=2
#     division=num1/num2
#     print(division)
# div()    


#  # WAP to cal number of char in string
# def string ():
#     name=input("Enter any string:")
#     count=0
#     for i in  name:
#         count+=1
#     print(count)
# string()

#  # WAP to cal per. char in given 
# def string1 ():
#     name=input("Enter any string:")
#     str=input("which char you want to count:")
#     count=0
#     for i in name:
#         if i == str:
#             count+=1
#     print(count) 
# string1()

 # create a fun spaces in string
# def string1 ():
#     name=input("Enter any string:")
#     count=0
#     for i in name:
#         if i == ' ':
#             count+=1
#     print(count) 
# string1()

#WAP 


# def vowel():
#     count = 0
#     name = input("Enter any string: ")
#     for i in name:
#         if i in 'aeiouAEIOU':
#             count += 1
#     print("Number of vowels:", count)

# vowel()


'''
=====================================================================================================
GLOBLE SCOPE AND LOCAL SCOPE
=====================================================================================================
GOBLE SCOPE==> 
                global  scope is define outside the function is called as globe scope
LOCAL SCOPE==> 
           local scope is define inside the function is called as local scope    
'''

# print('welcome to global scope')
# x=10
# y=30

# def fun():
#     print('welcome to local scope')
#     a=100
#     b=200
#     print('local scope variable  a={} and b={}'.format(a,b))
#     print('global scope variable x={} and y={}'.format(x,y))
# fun()
# print('global  scope variable x={} and y={}'.format(x,y))

'''
Action	             Allowed Without global?	Explanation
Reading a global variable	   ✅ Yes	Safe, doesn’t change anything
Modifying a global variable 	❌ No	Python assumes it's a new local variable
Modifying with global	       ✅ Yes	Tells Python to use the global variable



local variable outside the function data direct used not allowed 
'''
# def char_count():
#     name = "vaibhav arjun vaibhav"
#     name=name.split()
#     result = {}
#     for char in name:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     print(result)

# char_count()

# def fun ():
#     string=input("Enter the string:")
#     rev=''
#     for i in string:
#         rev=i+rev
#     print(rev)

# fun()

