# class counter:
#     def __init__(self):
#         self.count=0
#     def dec(self):
#         self.count-=1
#     def inc(self):
#         self.count+=1
    
#     def check_count(self):
#         print(self.count)

# obj=counter()
# # print(obj.check_count())
# obj.inc()
# obj.inc()

# obj.check_count()


'''
Incapsulation is a fundamental it is a process of wraping data and
 method in asingle and restrinctiong direct direct acess of some of componentet of an object this is done 
'''

#getter and setter method

class student:
    def __init__(self,nm,age,per):
        self.__name=nm
        self.__age=age
        self.__percentage=per
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_age(self):
        password=input('enter the password:')
        if password=='vaibhavarjun':
            return self.__age
        
    @get_age.setter
    def set_age(self,upage):
        if isinstance(upage,int)and upage>0:
            self._age=upage
        else:
            print('invalid age')
s1=student('vaibhav',23,89)
print(s1.get_name)
s1.set_age=55

    