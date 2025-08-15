def sum3(abc):
    def xyz(num1,num2,num3):
        sum = abc(num1,num2) + num3
        return sum
    return xyz
@sum3
def sum(num1,num2):
    sum=num1+num2
    return sum
print(sum(2,4,6)) 