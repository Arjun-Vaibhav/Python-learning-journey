'''
========================================================================================================
                                                METHOD
                1)Instence Method
                2)class method
                3) static method
========================================================================================================
'''


# class student:
#     institute='JBK'
#     course='Python'
#     trainer='Vaibhav'
#     fees='40000'
#     duration='5 month'
#     def __init__(self,rll,nm,ag):
#         self.roll_no=rll
#         self.name=nm
#         self.age=ag
#         self.marks={}
#     def student_detail(self):
#         return f'''
#         Name: {self.name}
#         Age:{self.age}
#         Course:{self.course}
#         marks:{self.marks}
#         Institute:{student.institute}
#     '''
#     def add_marks(self,testName,marks):
#         self.marks[testName]=marks
    
#     def perMarks(self):
#         obt=0
#         for i in self.marks.values():
#             obt=obt+i
#         total=100*len(self.marks)
#         per=(obt/total)*100
#         return f'{per}%'
    
#     @classmethod
#     def course_details(cls):
#         return f'''
#         course Name:{cls.course}\n Fees:{cls.fees}\n Duration:{cls.duration} \n tainer:{cls.trainer}
#         '''
    
#     @classmethod
#     def update_fees(cls,ufees):
#         cls.fees=ufees
#         return 'Updated successfully'
#     @staticmethod
#     def cal_rf(totalfees, paid):
#         rf= totalfees -paid
#         return rf

# # arjun=student(1,'arjun',21)
# # # print(arjun.student_detail())
# # arjun.add_marks('test_1',56)
# # arjun.add_marks('test_2',70)
# # # print(arjun.perMarks())
# # # print(arjun.student_detail())
# # print(arjun.course_detail())
# # print(student.update_fees)

# arjun = student(1, 'arjun', 21)
# arjun.add_marks('test_1', 56)
# arjun.add_marks('test_2', 70)

# print(arjun.course_details())           # Fixed function name
# print(student.update_fees(45000))       # Added function call with argument


# print(arjun.cal_rf(30000,20000))

#Employee

class Employee:
    company = 'Infosys'
    department = 'IT'
    base_salary = 40000
    location = 'Pune'

    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary_paid = 0
        self.bonuses = {}
        # self.total_bonuses=tb

    def employee_detail(self):
        return f'''
        Employee ID: {self.emp_id}
        Name: {self.name}
        Age: {self.age}
        Department: {Employee.department}
        Company: {Employee.company}
        Location: {Employee.location}
        Bonuses: {self.bonuses}
        Salary Paid: ₹{self.salary_paid}
        '''
    
    def add_bonus(self,BonusType,bounses):
        self.bonuses[BonusType]=bounses
    def total_bonus(self):
        sum=0
        for i in self.bonuses.values():
           sum=sum+i
        return f'''\tTotal_bonus=₹{sum}'''
    @classmethod
    def company_datail(cls):
        return f'''
        \n\tcompany Name:{cls.company}\n\t Department:{cls.department} \n\t base_salary:{cls.base_salary}\n\t location:{cls.location}
        '''
    @classmethod
    def Update_salary(self,usalry):
            self.base_salary=usalry
            return f'Salary update Successfully= {usalry}'
    @staticmethod
    def remaining_salary(total, paid):
        return f'Remaining Salary: ₹{total - paid}\nSalary update Successfully'


result=Employee(101,'vaibhav arjun',21)

# print(result.employee_detail())
result.add_bonus('gudipadava',2000) 
print('*'*60)
print('\temployee_detail')
print('*'*60)
print(result.employee_detail())
print('*'*60)
print(result.total_bonus())
print('*'*60)
print('\tCOMPANY DETAILS')
print('*'*60)
print(result.company_datail())
print('*'*60)
print(Employee.Update_salary(450000))
print('*'*60)
print( result.remaining_salary(45000,20000))
print('*'*60)