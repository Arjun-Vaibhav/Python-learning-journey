name="vaibhav arjun"
nm1=name.upper()
print(name.upper())
print(type(nm1))
==============================================================================================
name="VAIBHAV ARJUN"
nm2=name.lower()
print(name.lower())
print(type(nm2))
#==============================================================================================
name="arjun vaibhav Sampat"
fname=name.title()
print(fname)   #Arjun Vaibhav Sampat
#==============================================================================================
institute='java by kiran'
print(institute.capitalize()) #Java by kiran
#==============================================================================================
name="VAIBHAV ARJUN"
name.isalpha()
print(name.isalpha())
#==============================================================================================


var="arjun vaibhav"
print(var.isalpha())  #False
#==============================================================================================
var="arjunvaibhav"
print(var.isalpha())  #True
#==============================================================================================
var="1234"
print(var.isnumeric())   #True
#==============================================================================================
var=" "
print(var.isspace())   #True
#==============================================================================================
var="aadad2323"
print(var.isalnum())  #True
#==============================================================================================
'''
index method 

'''
name="arjun vaibhav"
print(name.index('v',7))     #12
#index method 
institute="The kiran acadamy"
print(institute.index('a'))
print(institute.index('a',8))
print(institute.index('a',11))
#==============================================================================================


# #count

institute="Thae kiran acadamy"

print(institute.count('a'))              #5

print(institute.count('a',5))            #4

print(institute.count('a',5,10))         #1

#==============================================================================================
# #replace

name='vaibhav'
print(name.replace(name,'arjun'))
institute="Thae kiran acadamy"
print(institute.replace('thae','the'))
#==============================================================================================
name='rajkumar abc sdf'
print(name.split())
#==============================================================================================
cls="the kiran academy"
print(cls.startswith('k',4))
print(cls.endswith('n',0,9))
#==============================================================================================