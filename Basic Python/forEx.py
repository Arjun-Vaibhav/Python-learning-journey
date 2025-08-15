'''
for=> it is used to excute to block of code number of time
'''
#==============================================================================================    

# name=['vaibhav','arjun','ganpatrav','shamrav']  # iterable
# for names in name:                              # iteration
#     print(names)
# print('THE END') 
#==============================================================================================    

# details={'name':'vaibhav', 'age':32, 'city':'pune'}
# for i,j in details.items():
#     print(i,j)
#==============================================================================================    

'''
range()=> it is  used to genarate seq. of number

syntax=>
        var=range(start value , stop value, step value)
'''
#==============================================================================================    

# number=range(10,101,10)
# for val in number:

#     print(val)
#==============================================================================================    

#wap to genarate from 11 to 20

# num=range(11,21)
# for i in num:
#     print(i)

#==============================================================================================    

# num=range(10,0,-1)
# for i in num:
#     print(i)
#==============================================================================================    

# # num=range(1,11)
# # for i in num:
# #     print(i**3)
#==============================================================================================    

# num=range(5,51,5)
# for i in num:
#     print(i)
#==============================================================================================    

# for i in range(1,21):
#     if(i %2==0):
#         print(i)
#==============================================================================================    

# num=range(1,101)
# n=list(num)
# print(n)
# for val in num:
#     print(list(num))

fact=1
for i in range(1,6):
    fact = fact *i
    print(fact)

#==============================================================================================    



python_result = {
    'shubham': {'t1': 50, 't2': 60, 't3': 70},
    'rahul': {'t1': 60, 't2': 80, 't3': 70},
    'kunal': {'t1': 70, 't2': 90, 't3': 80}
}
percentage_result = {}
for name, marks in python_result.items():
    print(name,marks)
    total=sum(marks.values())
    print(total)

#==============================================================================================    
square_lst=[]
num=[1,2,3,4,5,'6','7',8,'9',10]
for i in num:
    square=int(i)**2
    square_lst.append(square)
print(square_lst) 

#==============================================================================================    

items = [1, "apple", True, 2.5]
for i in items:
    dtype=type(i)
    print(i,'---->',dtype)

#==============================================================================================
number=[1,2,3,4,5,6,7]
square=[]
for i in number:
   sq=i*i
   square.append(sq)
print(square)
#==============================================================================================
student=['prathmesh','ritesh','prem','umesh']
st=set()
for i in student:
    i.upper()
    std=i.upper()
    st.add(std)
print(st)


#==============================================================================================    

'''
# what are data type and why are they imp.
# 
'''
#==============================================================================================    

# number=[1,2,3,4,5,6,7]
# for i in number:
#    sq=i*i
#    number.append(sq)
# print(number)
#==============================================================================================    

# result={}

# for i in range(4):
#     roll=int(input("Enter the roll number:"))
#     per=float(input("Enter the percentage:"))
#     result[roll]=per
# print(result)
#==============================================================================================    

# info={}
# num=int(input("How many member you want to add data:"))
# for i in range(num):
#     name=input("Enter person name:")
#     age=int(input("Enter person age:"))
#     info[name]=age
# print(info)

#==============================================================================================
for i in range(1,11):
    num=i**3

    print(num)
#==============================================================================================
st={ }
for i in range(2,11,2):
    sq=i * i
    st[i]=sq
print(st)
#==============================================================================================
result={'prathmesh':80,'ritesh':70,'prem':35,'umesh':60}
for key,value in result.items():
    result[key]= value + 5
print(result)
#==============================================================================================
result={'prathmesh':80,'ritesh':70,'prem':35,'umesh':60,'ganesh':89}
name=[]
for i in result:
 name.append(i)
print(name)
#==============================================================================================
emp={'prathmesh':80000,'ritesh':70000,'prem':35000,'umesh':60000}
# emps=[]
for key,value in emp.items():
    emp[key]= value + 20 * value /100
print(emp)
#==============================================================================================
product= {'sugar':42, 'shengdane':120, 'shabudana':80, 'tandul':50, 'oli':140}
lists={}
for key,value in product.items():
 
  total=value - 10 * value /100
  lists[key]=total
print(lists)
#==============================================================================================
number=[1,2,3,4,5]
sum=0
for i in number:
    sum= i + sum
print(sum)
#==============================================================================================