# def iseven():
#     num=eval(input("ENTER ANY NUMBER:"))
#     if num%2==0:
#         print('Even')
#     else:
#         print('not even')
# iseven()

# def square(num):
#     sq=num**2
#     print(sq)
# square(4)

#prameters==> python in parameters 
#An argument is the acual value to we give parameter when we call the function

#WAP to check positive or negative

# def nums(num):
#     if num>=0:
#         print('number is positive')
#     else:
#         print('number is negative')
# nums(-5)

#create a function to check  number1 to number2 is divisible by other number

# def number(num1,num2):
#     if num1/num2==0:
#         print('nummber is divisible.')
#     else:
#         print('nummber not is divisible.')

# number(4,3)        

'''
There are five type of argument
1) positional argument
==> the positional argumet are those where position is matter first goes to fist and second goes to second so on

2) keyword argument 
==> in case of keyword pass the parameters name position does't matter

3)defult arugment
==> defult argument means we give defult argument even if you dont pass argument  we will not show any error

4)positional arbitery argument
==>positional arbitery argument alloced multiple value as a tuple ,we used is where we dont no how many argument will com

5)keyword arbitery argument 
==>positional arbitery argument alloced multiple value as a dict ,we used is where we dont no how many argument will come

'''

# def detail(nm,ag,ct):
#     print(f'My name is {nm} i am {ag} year old and i am from {ct}')

# detail('vaibhav arjun',20,'pune')

# def detail(nm,ag,ct):
#     print(f'My name is {nm} i am {ag} year old and i am from {ct}')
# detail(ag=20,nm='rajkumar',ct='dubai')


#create a function to count number of alphabet only given in string

# def count_alph(name):
#     count=0
#     for i in name:
#         if i.isalpha():
#             count+=1
#         # else:

#     print(count)

# count_alph(name='va889cdfs')

# def detail(nm,co,inst='kiran acadamy'):
#         print(f'''
#             student Name:{nm}
#             course Name:{co}
#             Institute Name:{inst}
#             ''')
# detail('vaibhav arjun','Python full stack','kiran acadamy')
# detail('ram kumar','java full stack','java by kiran')

# def add(*sum):
#     total=0
#     sum=sum+total
#     print(total)
# add(4,56,4,2)


# def details(**kwargument):
#     print(kwargument)
# details(name='vaibhav', city='pune', mo=2345678909)


# dict={'name': 'vaibhav', 'city': 'pune', 'mo': 2345678909}
# print(dict)

#CREATE A FUNCTION TO REVERSE ANY STRING    
   
# string=input("you want to revers string enter it:")
# store=''
# num=len(string)-1
# while num>=0:
#     store=store+string[num]
#     num=num-1
# print(store)

# def fun(lst):    
#     result=lst[0]
#     for i in lst:
#        if result < i:
#            result=i
#     print(result)
# fun([3,5,6,2,3,9])
    # 
'''

character=10
vowel=2 
digit=5
'''


#WAP to check string if have string to check it is a vowel,cpunt  total  character in a string and how many alphabet in a string how many digit in a string and how many vowel in string
# def is_digit(string):
#     count=0
#     char=''
#     dcount=0
#     dchar=''
#     vcount=0
#     vchar=''
#     for i in string:
#         if i.isalpha():
#             count=count+1
#             char=char+i
#             if i in 'aeiouAEIOU':
#                 vcount=vcount+1
#                 vchar=vchar+i
#         elif i.isdigit():
#             dcount=dcount+1
#             dchar=dchar+i
#     print('characters count=',count,'this is character=',char)
#     print('digit count=',dcount,'this isdigit=',dchar)
#     print('vowel count=',vcount,'this is vowel=',vchar)

# is_digit("sjdsic8327asdhdhauiz")


# def second_largest(lst): #[3,2,4,53,55]
#     new=lst[0]
#     for i in lst:
#         if i>new:
#             new=i
#     print(new)
# second_largest([3,4,5,2,6,8])

# def prime_no(nummber): #1,3,5,7,11,13,17,19
#     for i in nummber:
#         if i%1==0 and i%i==0:
#             print('it is a prime number')
#         else:
#             print("it not a prime number")
# prime_no([3,4,7])

def rev_word(sentence):
    words = sentence.split()
    result = []
    for word in words:
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word 
        result.append(reversed_word)
    final_output = ' '.join(result)
    print(final_output)
rev_word("java by kiran")


#WAP 