# #Employee

# class Employee:
#     company = 'Infosys'
    # department = 'IT'
    # base_salary = 40000
    # location = 'Pune'

    # def __init__(self, emp_id, name, age):
    #     self.emp_id = emp_id
    #     self.name = name
        # self.age = age
#         self.salary_paid = 0
#         self.bonuses = {}
#         # self.total_bonuses=tb

    # def employee_detail(self):
    #     return f'''
    #     Employee ID: {self.emp_id}
    #     Name: {self.name}
#         Age: {self.age}
#         Department: {Employee.department}
#         Company: {Employee.company}
#         Location: {Employee.location}
#         Bonuses: {self.bonuses}
#         Salary Paid: ₹{self.salary_paid}
#         '''
    
#     def add_bonus(self,BonusType,bounses):
#         self.bonuses[BonusType]=bounses
#     def total_bonus(self):
#         sum=0
#         for i in self.bonuses.values():
#            sum=sum+i
#         return f'''\tTotal_bonus=₹{sum}'''
#     @classmethod
#     def company_datail(cls):
#         return f'''
#         \n\tcompany Name:{cls.company}\n\t Department:{cls.department} \n\t base_salary:{cls.base_salary}\n\t location:{cls.location}
#         '''
#     @classmethod
#     def Update_salary(self,usalry):
#             self.base_salary=usalry
#             return f'Salary update Successfully= {usalry}'
#     @staticmethod
#     def remaining_salary(total, paid):
#         return f'Remaining Salary: ₹{total - paid}\nSalary update Successfully'


# result=Employee(101,'vaibhav arjun',21)

# # print(result.employee_detail())
# result.add_bonus('Gudipadva',2000) 
# print('*'*60)
# print('\temployee_detail')
# print('*'*60)
# print(result.employee_detail())
# print('*'*60)
# print(result.total_bonus())
# print('*'*60)
# print('\tCOMPANY DETAILS')
# print('*'*60)
# print(result.company_datail())
# print('*'*60)
# print(Employee.Update_salary(450000))
# print('*'*60)
# print( result.remaining_salary(45000,20000))
# print('*'*60)


# class product:
#     def __init__(self,pnm,p_price):
#         self.product_name=pnm
#         self.product_price=p_price
    
#     def display(self):
#         return f'''
#             Product Name:{self.product_name}
#             product price:{self.product_price}
#             '''
#     def apply_discount(self, percent):
#          discount_price=self.product_price- (self.product_price* percent/100)
#          total_dic=self.product_price-discount_price
#          return discount_price,total_dic
            


# p1=product('Sugar',4000000)
# p2=product('banana',450000)
# obj1,obj2=p1.apply_discount(10)
# print(f'This is total discount:  ₹ {obj2}')
# print(f'this is after  dicounded amount: ₹ {obj1}')

# class Student:
#     def __init__(self,sname):
#         self.student_name=sname
#         self.student_marks={}

#     def display_student_info(self):
#         return f'''
#         student name:{self.student_name}
#         student marks:{self.student_marks}    
#          '''
#     def addSmarks(self,sub,marks):
#         self.student_marks[sub]= marks
    
#     def avgmarks(self):
#         sum=0
#         for i in self.student_marks.values():
#             sum=sum+i
#             total_avg=sum/len(self.student_marks)
#             return f'Average of total marks:{total_avg}'
            
# s1=Student('Vaibahv arjun')

# s1.addSmarks('math',60)
# s1.addSmarks('account',80)
# print(s1.display_student_info())
# print(s1.avgmarks())

class bank:
    def __init__(self, name ,balance):
        self.holder_name=name
        self.bank_balance=balance

    def check_bank_bal(self):
        return f'bank balance is ={self.bank_balance}'
    def depositAmt(self, amount):
        if (isinstance(amount,int) or isinstance(amount,float)) and amount>0:
            self.bank_balance= self.bank_balance+amount
            return f'Amount Deposit successfully: {amount} and total balance in your a/c is: {self.bank_balance}'
        else:
            return 'Invalid amount'
    
    def withdraw(self,amount):
        if (isinstance(amount,int) or isinstance(amount,float)) and amount>0:
            self.bank_balance= self.bank_balance-amount
            return f'Amount debited successfully: {amount} and total balance in your a/c is: {self.bank_balance}'
        else:
            return 'Invalid amount'
c1=bank('vaibhav arjun',20000)

print(c1.depositAmt(4000))
print(c1.withdraw(2000))
print(c1.check_bank_bal())