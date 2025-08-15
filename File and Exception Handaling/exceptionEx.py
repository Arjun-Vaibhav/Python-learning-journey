n1=eval(input('enter n1:'))
n2=(input('enter n2:'))
sum=n1+n2
sub=n1-n2
mul=n1*n2
try:
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print('zero cant devisible by number.')
except TypeError:
    print('we can deived int by str')
finally:
    print(f'sum:{sum}')
    print(f'sub:{sub}')
    print(f'mul:{mul}')
#===================================================================================================
def devision(n1,n2):
    try:
        div=n1/n2
    except ZeroDivisionError:
        n2=eval(input('we cant divisible by zero'))
        result=devision(n1,n2)
        return result
    else:
        return div
print(devision(10,0))
#===================================================================================================
def count_line(file):
    try:
        f=open('vaibhav.txt','r')
    except FileNotFoundError:
        f=input('enter file name again:')
        result=count_line(f)
        return result
    
    else:
        lint_line=f.readline()
        count=

#===================================================================================================
