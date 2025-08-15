class xyz:
    def m1():
        print('m1 is method of xyz')
    def m2():
        print('m2 is method of xyz')

# x=xyz()
# print(x.m1())

# class abc(xyz):
#     def a1():
#         print('a1 is method of abc')
#     def a2():
#         print('a2 is method of abc')

# a=abc
# a.m1()
# ========================================================================================

class Polygon:
    def __init__(self,nos):
        self.number_of_sides=nos
        self.sides=[]
    def input_sides(self):
        for i in range(self.number_of_sides):
            side=eval(input(f'enter sode {i+1} :'))
            self.side.append(side)
    def display(self):
        for index,length in enumerate (self.sides,1):
            print(f'length of side {index} is {length}')

class Triangle(Polygon):
    def perimeter(self):
        peri=0
        for side in self.sides:
            peri =peri + side
        return f'perimeter of triangle is {peri}'

t1=Triangle(3)

# ========================================================================================

# class Saving_acc:
#     def __init__(self,nm,ac,bal):
#         self.name=nm
#         self.account=nm
#         self.balance=bal
    
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#         else:
#             return 'Invalid amount'

#     def withdraw(self,amount):
#         if amount>0:
#             self.balance-=amount
#         else:
#             return 'Invalid amount'
    
#     def display(self):
#         return f''


class A :
    def m1():
        print('m1 is method of xyz')
    def m2():
        print('m2 is method of xyz')



class B:
    def a1():
        print('b1 is method of b')
    def a2():
        print('b2 is method of b')

class C:
    def  c1():
        print('c1 is method ofc')
    def a2():
        print('c2 is method of c')



