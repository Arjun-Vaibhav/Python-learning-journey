# class student:
#     def __init__(self,nm,mark):
#         self._name=nm
#         self._marks=mark

#     @property
#     def get_name(self):
#         return self._name

#     @property
#     def get_marks(self):
#         return self._marks

# st=student('vaibhav',99)
# print(st.get_name)
# print(st.get_marks)


class Bank:
    def __init__(self, balance):
        self.__balance = balance
    def check_balance(self):
        return self.__balance

b=Bank(100000)
print(b.check_balance())