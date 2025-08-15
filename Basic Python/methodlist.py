# # method of list
# '''
# access => 
# a) ADD 

# append() ==> append function is used to add number in last of list
# '''

# # num=[23,56,34,56,23,45]
# # num.append(50)
# # print(num)

# # student=["ram", "sham","vaibhav","arjun"]
# # student.append("prachi")
# # print(student)

# """
# INSERT => 
# """

# l=[11,22,33,['ajay','raj',[1,2,3,5,6,7],'pavan','vishal'],44,66,77]
# l.append(88)
# print(l)
# l.insert(-4,999)
# print(l)
# l[3].insert(1,"vijay")
# l[3].append("vaibhav")
# print(l)
# l[3][3].insert(1,888)
# print(l)
# l[3][3].insert(4,4)
# print(l)
# #[11, 22, 33, ['ajay', 'vijay', 'raj', [1, 888, 2, 3, 4, 5, 6, 7], 'pavan', 'vishal', 'vaibhav'], 999, 44, 66, 77, 88] 

# l[3][2]

# #how to data from list

# l=[22,44,55,111,66]
# l.remove(44)
# print(l)

# numbers=[11,22,33,44,22,55,66]
# numbers.remove(22)
# numbers.pop(-3)

# passed=['bhushan','kunal','pavan','ajay']
# failed=['ramesh','ganesh','dhanesh','om']
# passed.append(failed.pop(1))
# print(passed)
# print(failed)

# l=[11,22,33,['ajay','pavan','raj',[1,7,2,3,5,6,7],'pavan','vishal'],44,33,66,77]
# l.pop(-2)
# print(l)
# # [11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6, 7], 'pavan', 'vishal'], 44, 33, 77]
# l.pop(-2)
# print(l)
# [11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6, 7], 'pavan', 'vishal'], 44, 77]
# l[3].pop(-2)
# print(l[3])
# #['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6, 7], 'vishal']
# l[3][3].pop(-1)
# print(l)
# #[11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6], 'vishal'], 44, 77]

# # li=[11,33,44]
# # li.pop()
# # print(li)

# l.insert(0,10)
# print(l)
# #[10, 11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6], 'vishal'], 44, 77]

# print(l[4][-1][2:])

# l=[11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 3, 5, 6], 'vishal'], 44, 77]
# l[3][3].insert(-3,l.pop(-2))
# print(l)

# print(l[3][3])
# print(l)
# #[11, 22, 33, ['ajay', 'pavan', 'raj', [1, 7, 2, 44, 3, 5, 6], 'vishal'], 77]
# print(l[3][2][2])


# #clear()

# l=[11,33,44,66]
# l.clear()
# print(l)

# #del

# num=[11,22,33,88,99]

# # del num[1]
# # print(num)

# # del num[3][1]
# # print(num)

# num.sort()
# print(num)

# num.sort(reverse=True)
# print(num)

l=[4,6,2,3,4,7,8,3,4]
print(l.count(3))

print(l.index(3,-3))


#copy()
# number1=[11,22,33,44,66]
# number2=number1
# print(number2)

# number2.append(55)
# print(number2)
# print(number1)

# print(id(number1))
# print(id(number2))

number1=[11,22,33,44,66]
number2=number1.copy()
print(number2)

print(id(number1))
print(id(number2))

n1=[2,6,1,7,3]
n2=[5,3,5,1,8]
n1.extend(n2)
print(n1)

num=[2,3,4,5,6]
num.extend([2,3,4,5,1])

num.append(22)
print(num)
name=['ram','sham','vaibhav','kishan']
# name.append(['prachi','yasmeen'])
# print(name)
name.extend(['prachi','yasmeen'])
print(name)