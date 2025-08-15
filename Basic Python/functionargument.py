# def iseven():
#     num=eval(input("ENTER ANY NUMBER:"))
#     if num%2==0:
#         print('Even')
#     else:
#         print('not even')
# iseven()
#==============================================================================================    

def square(num):
    sq=num**2
    print(sq)
square(4)
#==============================================================================================    

#prameters==> python in parameters 
#An argument is the acual value to we give parameter when we call the function
#==============================================================================================    

#WAP to check positive or negative

# def nums(num):
#     if num>=0:
#         print('number is positive')
#     else:
#         print('number is negative')
# nums(-5)
#==============================================================================================    

#create a function to check  number1 to number2 is divisible by other number

# def number(num1,num2):
#     if num1/num2==0:
#         print('nummber is divisible.')
#     else:
#         print('nummber not is divisible.')

# number(4,3)        
#==============================================================================================    

'''
1) Positional Argument
Arguments passed in the correct order; 
the position of values matters.
#==============================================================================================
2) Keyword Argument
Arguments are passed using parameter names; 
order does not matter.
#==============================================================================================
3) Default Argument
A parameter has a default value, used if no value is passed.
#==============================================================================================
4) Positional Arbitrary Argument (*args)
Used to pass a variable number of positional arguments as a tuple.
#==============================================================================================
5) Keyword Arbitrary Argument (**kwargs)
Used to pass a variable number of keyword arguments as a dictionary.

'''

def detail(nm,ag,ct):
    print(f'My name is {nm} i am {ag} year old and i am from {ct}')
detail('vaibhav arjun',20,'pune')
#==============================================================================================
def detail(nm,ag,ct):
    print(f'My name is {nm} i am {ag} year old and i am from {ct}')
detail(ag=20,nm='rajkumar',ct='dubai')

#==============================================================================================
#create a function to count number of alphabet only given in string

def count_alph(name):
    count=0
    for i in name:
        if i.isalpha():
            count+=1
        # else:

    print(count)

count_alph(name='va889cdfs')
#==============================================================================================
def detail(nm,co,inst='kiran acadamy'):
        print(f'''
            student Name:{nm}
            course Name:{co}
            Institute Name:{inst}
            ''')
detail('vaibhav arjun','Python full stack','kiran acadamy')
detail('ram kumar','java full stack','java by kiran')
#==============================================================================================
def add(*sum):
    total=0
    sum=sum+total
    print(total)
add(4,56,4,2)
#==============================================================================================

def details(**kwargument):
    print(kwargument)
details(name='vaibhav', city='pune', mo=2345678909)

#==============================================================================================
dict={'name': 'vaibhav', 'city': 'pune', 'mo': 2345678909}
print(dict)
#==============================================================================================
#CREATE A FUNCTION TO REVERSE ANY STRING    
   
string=input("you want to revers string enter it:")
store=''
num=len(string)-1
while num>=0:
    store=store+string[num]
    num=num-1
print(store)
#==============================================================================================