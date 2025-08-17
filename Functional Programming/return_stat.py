
#========================================================================================
num=100
def fun():
    x=10
    return x
print('x value is:',fun())

#========================================================================================

x=10
def fun():
    y=20
    print('welcome')
    print('hello')
    return y
print(fun())
print("coding...")
a=fun()
print(a)
#========================================================================================

def  iseven(num):
    if num%2==0:
        return True
    else:
        return False
#========================================================================================

def ispositive(num):
    if num>=0:
        return True
    else:
        return False
#========================================================================================

#WAP to check number is prime or not

def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(isprime(6))
#========================================================================================


add=[]
adds=[]
def isprime(num):
    add=[]
    adds=[]
    for i in num:
        for i in range(2,num):       
            if num%i==0:
                add.append(i)
        adds.append(i)
print(isprime([1,2,3,4,5]))
#========================================================================================

def is_prime(lst):
    prime_numbers=[]

    for i in lst:
        for num in range(2,i):
            if i%num==0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers
print(is_prime([1,2,3,4,5,6,7,8]))
#========================================================================================


'''
===============================================================================================
Nested function
===============================================================================================
'''

def f1():
    print("welcome to function1.......")
    def f2():
        print("welcome to function f2")
    return f2
f2=f1()
f2()
#========================================================================================


def f1():
    print("welcome to function1.......")
    a=10
    def f2():
        print("welcome to function f2")
    return f2,a**2
f2,sq=f1()
print(sq)
f2()
#========================================================================================

def st_details(name,city):
    st_d=f'my name is {name} and I am from {city}'
    def inst_details(in_name,branch):
        int_d=f'''
        institute Name:{in_name}
        branch:{branch}
            '''
        return int_d
    return st_d,inst_details
st_d,inst_details=st_details('harish','nagpur')
int_d=inst_details('kiran academy','karve nagar')
print(st_d)
print(int_d)
#========================================================================================


def student(name,city,age):
    student_informaton=f'my name is {name} I am from {city} i am {age} year old'
    def teacher(name,department):
        teacher_inforamtion=f'my name is {name} I am wroking as a {department} department '
        return teacher_inforamtion
    teacher_info=teacher('mr vaibhav sir','CSIT')
    return student_informaton,teacher_info
#========================================================================================

    
stdudent_info,teacher_info=student('vaibhav','pune',21)
print(stdudent_info)
print(teacher_info)
#========================================================================================


#Write a function to calculate the factorial of a number (use loop).
def fact(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
        return fact
print(fact(5))
#========================================================================================

#Define a function that accepts a list and returns the sum of all elements.
def sum_list(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum
print(sum_list([2,4]))
#========================================================================================


#Create a function that takes a string and returns the number of vowels in it.

def vowel(string):
    vowels=[]
    for i in  string:
        if i in 'aeiouAEIOU':
          vowels.append(i)
    return vowels
string=input('enter any string:')
print('this vowel found in exiting strig=',vowel(string))
#========================================================================================
