# class xyz:
#     def __init__(self):
#         print("Hello, Welocme to init method")
#     def m1(self):
#         print('Hello, welcome to m1 method')

# x1=xyz()


# class xyz:
#     def __init__(self):
#         print(f"id of self is {id(self)}")
#     def m1(self):
#         print('Hello, welcome to m1 method')

# x1=xyz()
# print(f'id of x1 is {id(x1)}')

# x2=xyz()
# print(f'id of x2 is {id(x2)}')


'''
    INSTANCE ATTRIBUTE
'''

class Oppo_79A:
    shopName='kiran mobile shop'
    owner='kiran patil'
    GSTN='123456898'
    def  __init__(self,rm,st,pr,c):
        self.ram=rm
        self.storage=st
        self.price=pr
        self.color=c

op1=Oppo_79A('8GB','128GB',21000,'lightblue')
print(op1.GSTN)
        


class Student:
    institute='The kiran accademy'
    python = 'Python' 
    trainer='vaibhav patil'
    def __init__(self,nm,rn,ag,pr):
        self.name=nm
        self.roll_no=rn
        self.age=ag
        self.per=pr
std1=Student('Vaibhav Arjun',1,20,99,9)


class employee:
    company='TCS'
    company_location='Dubai Fata'
    def __init__(self,enm,esal,adr):
        self.employe_name=enm
        self.employe_salary=esal
        self.address=adr
emp1=employee('prachi kadam',15000,'Ambegaon')



class book:
    bookName='Rich Dad Poor Dad'
    writer='vaibhav Arjun'
    bookLang='English'
    def __init__(self,fsize,tcolor):
        self.font_size=fsize
        self.text_color=tcolor
b1=book(14,'black')
print(b1.font_size)


