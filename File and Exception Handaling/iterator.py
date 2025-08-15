# i=[10,20,30,40,50]
# iter_obj=iter(i)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# print(type(iter_obj))
#=================================================================================
# l=[11,22,33]
# t=(11,22,33)
# s='vaibhav'
# num=199
#=================================================================================
'''
__iter__  only===> iterable
__iter__ and __next__ ==iterator
'''

# print(dir(l))

def check(user):
    if '__iter__' in dir(user) and '__next__' in dir (user):
        return 'itarator'
    
    elif '__iter__':
        return 'iterable' 
    else:
        return 'nothing'
print(check(70))
#=================================================================================
class myrange:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return myrange_iterator(self)

class myrange_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj
        def __iter__(self):
            pass
        def __next__(self):
            if self.iterable_obj.start < self.iterable_obj.stop:
                result=self.iterable_obj.start
                self.iterable_obj.start=self.iterable_obj.start + self.iterable.step
                return result
            else:
                raise StopIteration

for i in myrange(1,10,1):
    print(i)

