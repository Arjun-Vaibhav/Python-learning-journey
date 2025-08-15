'''
excute number of time
while==>while loop is itreative statement 
'''

num=1
while num < 5:
    print("vaibhav arjun")
    num=num+1
print("coding..")
#==============================================================================================
#WAP to print number from 11-20 by using while loop
num=11
while num <=20:
    print(num)
    num=num+1
#==============================================================================================
#WAP to print number from 10-1 by using while loop

num=10
while num >= 1:
    print(num)
    num=num-1
#==============================================================================================
#WAP to print list of square of number 11 to 15 using while loop
num=11
square=[]
while num <=15:
    sq=num**2
    square.append(sq)
    num=num+1
print(square)
#==============================================================================================
cube={}
num=1
while num <=5:
    cb=num**3
    cube[num]=cb
    num=num+1
print(cube)
#==============================================================================================
student = ['vaibhav', 'pranav', 'rajnath', 'ganesh', 'tushar']
i = len(student)-1
while i >=0:
    print(student[i])
    i -= 1
#==============================================================================================
name='raj'
n=' '
for i  in name:
    n= i + n
    print(n)   
#==============================================================================================


name = 'raj'
rev = ''
num = len(name) - 1

while num >= 0:
    rev = rev + name[num]
    num -= 1

print(rev)
#==============================================================================================
num=1
nums=5
while num <= 10:
    table =num * nums
    print(num,"x",nums,'=',table) 
    num+=1  
#==============================================================================================
strs='hello'
rev=''
num=len(strs)-1
while num >= 0:
    rev = rev + strs[num] 
    num -=1
print(rev)
#==============================================================================================
num=1
while num <=10:
    if num==6:
        break
    print(num)
    num+=1
#==============================================================================================
num=1
while num <=10:
    if num%2==0:
        num +=1
        continue
    print(num)
    num +=1
#==============================================================================================    

num=int(input("Enter the number:"))
fact=1
while num>=1:
    fact=fact * num
    num-=1
print(fact)
#==============================================================================================    

lst=[1,-9,3,4,-6]
n=0
while n<len(lst):
    if lst[n]>0:
        print(lst[n],'-->',"number is positive.")
    else:
        print(lst[n],'-->',"nummber is negative")
    n+=1