#WAP 

def fun(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
print(fun(3,5))



# def even(num1):
#     if num1%2==0:
#         return 'num is even'
#     else:
#         return 'num is odd'
#     def positive_negative(num2):
#         if num2>=0:
#             return 'positive'
#         else: 
#             return 'negative'
# print(even(5))




def f1(n1):
    print('function 1')
    n1=n1+2
    def f2(n2):
        print('function 2')
        n2=n2+3
        def f3(n3):
            print('function 3')
            n3=n3+4
            def f4(n4):
                n4=n4+4
                def f5(n5):
                    n5=n5+5         
                    return n5
            return n3,f4  
        return n2,f3  
    return n1,f2            
n1,f2=f1(20)  
n2,f3=f2(20)
n3,f4=f3(20)
n4,f5=f4(40)
print(n1,n2,n3)
print(f5(20))












# def isperfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if sum==num:
#         return True
#     else:
#         return False
# num=int(input('Enter the  number:'))
# print(isperfect(num))

#create function to check number armtrong or not

# def armstrong(num): #153
#     sum=0
#     numbers=str(num)
#     num_len=len(numbers)
#     for i in numbers:
#         sum=sum+int(i)**num_len
#     if sum==num:
#         return True
#     else:
#         return False
# num=int(input('Enter num you want to check number is armstrong or not:'))
# print(armstrong(num))
    
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact =fact*i
#     return fact
# num=int(input('Enter num you want to calculate factorial:'))
# print(fact(num))

'''
=================================================================================================
                                        LAMBDA FUNCTION
=================================================================================================
lambda is a anonumas function
SYNTAX:
      lambda variable : expration

'''
# print((lambda num: num**2 )(5))
# print((lambda num: num**3)(5))


# cube=lambda num:num**2
# print(cube(2))

# sum=lambda num1,num2: num1+num2
# print(sum(5,6))


#create a function to check number is positive or not using lambda function

# p=lambda num: True if num>0 else False
# print(p(4))

# even=lambda num: True if num%2==0 else False
# print(even(4))  

'''
REDUCE
'''
number=[2,3,4,5]
from functools import reduce
print(reduce(lambda sum,num:sum+num,number,0))


data=['kunal','ramdas','kale']
from functools import reduce
print(reduce(lambda name,n:name +' ' +n,data))


numbers=[1,2,3,4]
from functools import reduce
print(reduce(lambda sum,num:sum *num,numbers,1))

#write a program square of multiplication of all number
n=[9,2,3,4]
from functools import reduce
print(reduce(lambda sum,num:sum +num **2,n,0))


