# #Bank customer
# import datetime as dt
# class bank_customer:
#     bank_name='state bank of india'
#     branch='karvenager'
#     IFSC_code='SBIN004471'

#     def __init__(self ,nm,ac,bal):
#         self.Name=nm
#         self.Account_number=ac
#         self.Bank_balance=bal

#     def check_bank_balance(self):
#         return f'Bank balance is {self.Bank_balance}'
    
#     def deposit(self,amount):
#         if (isinstance(amount,int) or isinstance(amount,float)) and amount >0:
#             self.Bank_balance = self.Bank_balance+ amount
#             return f'Your account {self.Account_number} credited with INR {amount} on {dt.date.today()}, Available balance is {self.Banck_balance}'
#         else:
#             return 'Invaild amount'
#     def withdraw(self,amount):
#         if amount> self.Bank_balance  and amount >0:
#             self.Bank_balance=self.Bank_balance-amount
#             return f'Your account {self.Account_number} debited with INR {amount} on {dt.date.today()}, Available balance is {self.Banck_balance}'
#         return 'insufficent balance'
#     @staticmethod
#     def cal_compund_int(p,t,r,n):
#         r=r/100
#         ci=p*(1+(r/n))**(n*t)
#         t_ci=ci+p
#         return ci,t_ci
    
# c1=bank_customer('vaibhav Arjun',36977014824,10000000)
# c2=bank_customer('prachi kadam',3697701482,1000000)
# # print(c1.check_bank_balance())
# # # print(c2.withdraw(2))
# # print(c2.deposit(100))
# t_ci,ci=bank_customer.cal_compund_int(10000,1,10,2)
# print('total ci:',t_ci)
# print('ci:',ci)


#book 

import datetime as dt

class LibraryBook:
    # Class Attributes (shared among all books)
    library_name = "City Central Library"
    location = "Pune"

    # Constructor (instance attributes)
    def __init__(self, book_id, title, author, year, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    # Instance Method: Show details
    def show_details(self):
        return (f"Library: {LibraryBook.library_name}, Location: {LibraryBook.location}\n"
                f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\n"
                f"Year: {self.year}\nAvailable: {'Yes' if self.available else 'No'}\n")
    def bookissue(self):
        if self.available:
            self.available=False
            return f'book{self.title} issue on {dt.date.today()}'
        else:
            return f'is already issued{self.title}'
result=LibraryBook(101,'rich dad poor dad poor dad','vaibhav arjun',2012,True)
print(result)