f=open(file='vaibhav.txt',mode='r')
for i in f:
    print(i)
#=================================================================================
f=open('vaibhav.txt','r')
data=f.read(3)
print(data)

#=================================================================================
f=open('vaibhav.txt','r')
data1=f.readline()
data2=f.readline()
print(data1)
print(data2)
#=================================================================================
f=open('vaibhav.txt','r')
data1=f.readline(0)
print(data1)
#=================================================================================
f=open("vaibhav.txt",'r')
print(f.tell())
f.read(2)
print(f.tell())
f.seek(0)
print(f.readline())
#=================================================================================

name=input('enter name:')
age=input('enter age:')
per=input('enter per:')
f=open('student_details.txt','w')
f.writelines([f'{name}\n',f'{age}\n',f'{per}'])
def copyfile(file1, file2):
    f = open(file1, 'r+')
    f1 = open(file2, 'w+')
    for i in f:
        f1.writelines([i])
#=================================================================================
cp = copyfile('student_details.txt', 'vaibhav.txt')
print(cp)

#=================================================================================
