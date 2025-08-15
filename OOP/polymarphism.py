# class Book:
#     def __init__(self,nm,pg):
#         self.name=nm
#         self.pages=pg
#     def __add__(self,other):
#         total=self.pages+other.pages
#         return total

# b1=Book('python programing',200)
# b2=Book('data acience',300)
# print(b1+b2)
# print(b1.__add__(b2))

class saving_account:
    crop_loan_ri=8
    home_loan_ri=14
    def __init__(self,nm,ac,bal):
        self.name=nm
        self.account_no=ac
        self.balance=bal
    def cheak_balance(self):
        return self.balance
    def deposit (self,amount):
        if amount>0:
            self.balance+=amount
            return 'return'
        else:
            return 'invalid amount'
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return 'done'
        else:
            return 'insufficient balance'
s1=saving_account('vaibhav',101,10000)

class current_account(saving_account):
    home_loan_ri=20
    def __init__(self, nm, ac, bal,od):
        self.od=od
    def withdraw(self, amount):
        if amount <(self.balance+self.od):
            self.balance-=amount
            return 'done'
        else:
            return 'insufficinet balance'
        
c1=current_account

'''
Method overriding a sub class provide specific of a method is alreday define 
'''
       