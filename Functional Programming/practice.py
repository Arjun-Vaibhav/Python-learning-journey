'''
1.10 EXERCISE

the

Programming Problems 
'''

#1. Write a program to enter two integers and then perform all arithmetic operations on them.
num1=int(input('enter the number1:'))
num2=int(input('enter the number2:'))

print('*'*50)
print('addition:        ',num1+num2)
print('substraction:    ',num1-num2)
print('multiplication:  ',num1*num2)
print('division:        ',num1/num2)
print('foor division:   ',num1//num2)
print('modulo:          ',num1%num2)
print('*'*50)
#2. Repeat the program in Question 1 using floating point numbers.
num1=float(input('enter the number1:'))
num2=float(input('enter the number2:'))

print('*'*50)
print('addition:      ',num1+num2)
print('substraction:  ',num1-num2)
print('multiplication:',num1*num2)
print('division:%.2f  ',num1/num2)
print('foor division: ',num1//num2)
print('modulo:%.2f    ',num1%num2)
print('*'*50)
#3. Write a program to perform string concatenation.

string1=input("enter the string1:")
string2=input('enter the string2:')
result=string1+ string2
print(result)


#4. Write a program to demonstrate printing a string within single quotes, double quotes, and triple quotes.


#5. Write a program to print the ASCII value of acharacter.
number=input('enter charactor:')
print(f'ASCII value of char {number}  is',ord(number))
#6. Write a program to read a character in uppercase and then print it in lowercase.

char=input('Enter the char:')

if char.isupper():
    print('lowercase:',char.lower())
else:
    print('the character is lower')
    




    
#7. Write a program to swap two numbers using a temporaryvariable.

a=int(input('enter value of a:'))
b=int(input('enter the value of b:'))
print('before swaping a:',a)
print('before swaping b:',b)
t=a
a=b
b=t
print('after swaping a:',a)
print('after swaping b:',b)
#8. Write a program to demonstrate implicit conversion.

#9. Write a program to demonstrate explicit conversion.

#10. Write a program to read the baddress of a user. Display the result by breaking it in multiple lines.