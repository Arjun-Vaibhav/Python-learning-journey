'''
=======================================================================================================
                                        DECORATION
=======================================================================================================\

==> 
'''

def deco (fun):
    def inner():
        fun()
        print('hello welcome to TKA')
        print('hello welcome to TKA')
    return inner
#=======================================================================================================\
def printer():
    print('hello welcome to TKA')
    print('hello welcome to TKA')
    print('hello welcome to TKA')
inner=deco(printer)
inner()

#=======================================================================================================\
#Example 2

def deco(fun):
    def inner():
        total = fun()  # Call the original function to get num1 + num2
        num3 = eval("input('Enter num3: ')")  # Corrected eval syntax
        return total + num3
    return inner
#=======================================================================================================\
@deco
def sum():
    num1 = eval("input('Enter num1: ')")  # Corrected eval syntax
    num2 = eval("input('Enter num2: ')")
    return num1 + num2
print(sum())
#=======================================================================================================

#Example 4

def deco (fun):
    def inner(n1,n2,n3):
        result=fun(n1,n2)
        return result+n3
    return inner
@deco
def add (n1,n2):
    return n1+n2
print(add(10,20,30))

#=======================================================================================================
def login(fun):
    def inner():
        username=input('Username:')
        password=input("Password:")
        if username=='vaibhav' and password=="arjun123":
            fun()
        else:
            print('Invalid username of password')
    return inner

@login
def home():
    print('welcome to home page..')

@login
def dash():
    print('welcome to Your dashboars...')


home()
#=======================================================================================================
student=['kunal','rahul','vijay','sagar','irana']
print(list(enumerate(student,1)))
#=======================================================================================================

student=['kunal','rahul','vijay','sagar','irana']
print('roll   Student_name')
for index,name in enumerate(student,1):
    print(index,'---->',name)
#=======================================================================================================

roll=[1,2,3,4,5]
student=['kunal','rahul','vijay','sagar','irana']
print(list(zip(roll,student)))
#=======================================================================================================

roll=[1,2,3,4,5]
student=['kunal','rahul','vijay','sagar','irana']
for name,mark in zip(roll,student):
    print(roll,'->',mark)
#=======================================================================================================

roll=[1,2,3,4,5]
student=['kunal','rahul','vijay','sagar','irana']
print(dict(zip(roll,student)))

#=======================================================================================================

def sum3(abc):
    def xyz(num1,num2,num3):
        sum = abc(num1,num2) + num3
        return sum
    return xyz
@sum3
def sum(num1,num2):
    sum=num1+num2
    return sum
print(sum(2,4,6)) 

#=======================================================================================================


