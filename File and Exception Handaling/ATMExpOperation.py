
class DepositError(Exception):
    pass
class  WithdrawError(Exception):
    pass
class InsufficentFundError(Exception):
    pass
#=========================================================================
def menu():
    print('*' * 50)
    print('ATM OPERATION OR FUND TRANSFER!!')
    print('*' * 50)
    print('\t1) Deposit\n')
    print('\t2) Withdraw\n')
    print('\t3) Balance Enquiry\n ')
    print('\t4) Exit')
    print('*' * 50)
#=======================================================================
bal=500.00
def Deposit():
    dmat=float(input('Enter Ur Deposit Amount:'))
    if dmat<0:
        raise  DepositError
    else:
        global bal
        bal+= dmat
        print('Your account xxxxxxxxx2582 credited with INR:{} '.format(dmat))
        print('Now Your account xxxxxxxxx2582 balance is INR:{}'.format(bal))
def withdraw():
    global bal
    wmat = float(input('Enter Ur withdraw Amount:'))
    if wmat <= 0:
        raise WithdrawError
    elif bal<wmat:
        raise InsufficentFundError
    else:
        bal -= wmat
        print('Your account xxxxxxxxx2582 debited with INR:{} '.format(wmat))
        print('Now Your account xxxxxxxxx2582 balance is INR:{}'.format(bal))
def balaeq():
    print('Now Your account xxxxxxxxx2582 balance is INR:{}'.format(bal))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
menu()
while(True):
    try:
        user = int(input('Enter Number:'))
        match (user):
            case 1:
                try:
                    Deposit()
                except ValueError:
                    print('\t dont enter alnum,strs and symbols for depositing the amount:')
                except DepositError:
                    print('\t cant add -ve value or zero value.')
            case 2:
             try:
               withdraw()
             except ValueError:
                 print('\t dont enter alnum,strs and symbols for withdraw the amount:')
             except WithdrawError:
                 print('\t cant withdraw -ve value or zero value.')
             except InsufficentFundError:
                 print('\t does not have sufficent fund')

            case 3:
                balaeq()
            case 4:
                print('Thanks for using this program. ')
                break
            case _:
                print('Your selection of operation wrong.. Try again!!')
    except ValueError:
            print('Dont enter alum ,symbols for choise-- Try Again!!')
