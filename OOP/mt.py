# from threading import Thread

# def f1():
#     for i in range(1,10):
#         print(i)

# def f2():
#     for i in range(11,20):
#         print(i)

# t1=Thread(target=f1,name='thread 1')
# t2=Thread(target=f2,name='thread')

# t1.start()
# t2.start()
# print('Hello')

# from threading import Thread,RLock
# lock=RLock
# def task(lock):
#     print('Acquring lock firat time..')
#     lock.acquire()
#     print('Trying to acquire again..')
#     lock.acquire()
#     lock.release()
#     print('done')
#     t1=Thread(target=task,args=(lock))
#     t1.start()

#==============================================================
    #   madule
#==============================================================

# count vowel in given word

# word=input('Enter any strng or words:')
# lstword=list(word)
# print(lstword)
# count=[]
# for i in lstword:
#     if i in 'aeiouAEIOU':
#        count.append(i)
# print('Total vowel in string={}'.format(count))
# print('total number of vowel in word={}'.format(len(count)))


# word=input('Enter any strng or words:')
# lstword=list(word)
# print(lstword)
# count=[]
# for i in lstword:
#     if i not in 'aeiouAEIOU':
#        count.append(i)
# print('Total consonant in string={}'.format(count))
# print('total number of consonant  in word={}'.format(len(count)))


# word='MISISSIPI'
# charactars='I'
# count=0
# for i in word:
#     if i=='I':
#         count+=1

# print('total=',count)


# num=[23,14,56,78,41,25,35,46]
# lenum=int(len(num))
# midnum=lenum//2
# print(num[midnum])

# lst=['P','Y','T','H','O','N']
# jointlst="-".join(lst)
# print(jointlst)

# number_list=[20,3,6,22,60,40]
# max=number_list[0]
# for i in number_list:
#     if max <i:
#         max=i

a='a  b v  e  t   '
print(list(a))
print(len(a))
result=a.strip()
print(len(result))
print(result)
