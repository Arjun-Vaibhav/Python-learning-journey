#WAP which will generate multiplication table for a given number
#1) if the given number is negative if hit to generate NegativeNumberError
#2) if the given number is Zero then hit and ganerate ZeroError
#3) if givn number is alpha-numeric then generate ValueError
#4) if number is number is positive then print table


class NegativeNumberError(Exception):
    pass
class ZeroError(BaseException):
    pass
#==============================================================================================
def CreateTable(num):
    n=int(num)
    if n<0:
        raise NegativeNumberError
    elif n==0:
        raise ZeroError
    else:
        print('*' * 50)
        for i in range(1,11):
            print('{} X {}= {}'.format(n,i,n*i))
    print('*' * 50)
# ==============================================================================================
while(True):
    try:
        num = input('Enter number for generating table:')
        CreateTable(num)
    except ValueError:
        print('Dont enter strs,float and special symbols.')
    except ZeroError:
        print("Don't Enter Zero for multiplication of table")
    except NegativeNumberError:
        print("Don't Enter Negative value for multiplication of table")
    else:
        print('thanks for using program....')
        break



