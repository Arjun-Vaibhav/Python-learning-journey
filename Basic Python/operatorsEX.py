'''
+ => addition is used to add two number and concatenate to string
operator=> operator is a special symbol are used to performe operation  on data
'''
'''
1) arithematic operator
    A) addition('+')
'''
# print(10 + 30) #40
#==============================================================================================
# print('hello'+'user')   #hellouser
#==============================================================================================
# l1=[2,5,3,5]
# l2=[5,7,3,8]
#==============================================================================================
# print(l1 + l2) #[2, 5, 3, 5, 5, 7, 3, 8]
#==============================================================================================
# print((1,3,4,6,7)+(3,5,6,3)) #(1, 3, 4, 6, 7, 3, 5, 6, 3)
#==============================================================================================
# print({2,4,5,6} + {4,5,6,2}) #TypeError: unsupported operand type(s) for +: 'set' and 'set'
#==============================================================================================
# print({'1':1, '2':4} +{'3':4})
#==============================================================================================
# print(True + True) #2
#==============================================================================================
'''
    B) division('/')
    => division always return float value
'''
# print(10/5) #2.0

#==============================================================================================
'''
    B)  floor division('//')
    => division always return  int value
'''
# print(10/5) #2

#==============================================================================================
'''
    B) power('**')
    =>
'''
# print(5**5) #3125
#==============================================================================================

'''
    B) remaindar('%')
    =>
'''
#==============================================================================================
# print(5 %2) #1

# a=10
# b=5


# print(a>b) #True
# print(a<b)  #False

# print(a>=b)  #True
# print(a<=b)  #False
# print(a==b) #False
# print(a!=b) #False
#==============================================================================================
# a=20
# b=5
# b+=50
# print(b)
# b-=50
# print(b)
# b/=50
# print(b)
# b*=40
# print(b)
#==============================================================================================
# num=10
# num %=2
# print(num)
#==============================================================================================
'''
   Membership operator
   1) in
   2) not in
    =>always retun bool value
'''
# number=[2,4,5,6,7,8]
# print(3 in number)
# print(3 not in number)
#==============================================================================================
'''
  Identity operator
  1) is 
  2) is not
    =>
'''
#==============================================================================================
# a=10
# b=10

# print(a,type(a),id(a))
# print(a,type(b),id(b))
# print(a is b)
# print(a==b)
#==============================================================================================
# l1=[5,10,15]
# l2=[5,10,15]
# print(l1,type(l1),id(l1)) 
# print(l2,type(l2),id(l2))
# print(l1 is l2)
# print(l1==l2)
#==============================================================================================
'''
how to manage
=>python reused object like int ,float etc to impro performance 
but mutable type are 
affect the object directly

'''




'''
explain deff is and ==
=> == to  check value equality
=> is to check reference equality 
'''
#==============================================================================================
# print(a,type(a),id(a))
# print(a,type(b),id(b))
# print(a in b)
# print(a not in b)
#==============================================================================================
# l1=[5,10,15]
# l2=[5,10,15]
# print(l1,type(l1),id(l1)) 
# print(l2,type(l2),id(l2))
# print(l1 in l2)
# print(l1 not in l2)
'''

1) Data-Type:
=> Data type is used for allocating memory space and for storing input(data)
  => why they imp because
2)the python is dynamically typed language programmer not need write data type when are variable declaration.

3) i)  list is mutable / tuple is immutable

   ii) list value store value we can used square  brackets [] / tuple  value store value we can used braces()
4) 'is' => Checks if two variables point to the same object in memory
    '==' => Checks if the values of two variables are equal.
Example:-
   a=[5,10,20]
   b=[5,10,20]
  print(a==b)
  print(a is b)

5) in real life case using list is not good way to storing data but using dictionary is way good way to
 storing data in a systematic way is easily possible and dict is more useful then list     

 example:- we cant  store student information data systematic systematic way 
           beacuse student have defferent propertis such as name , student_roll_no, student_idno etc
6) we can not modify string in python after creation beacuse string is immutable
7) immutable --> int,float,str,tuple
     Stored in fixed memory.
     When you modify them, a new object is created.
   mutable---> list,set,dict
   Stored in memory with a pointer to data (like a reference).
    You can change the data in-place without creating a new object.    
8) a) pop and remove
    => pop() method is used to  for removing the last elements of the list
    =>remove() method is used for removing the first occurence of specified value from list object
   b) intersection and intersection_update
   => this method is used for obtaining common elements from both setobj1 and setobj2
   => intersection_update() is a set method in Python that updates the calling set by keeping 
   only the elements that are common (i.e., intersection) with one or more other sets.
  c) difference and symmetic_difference
  => Returns a new set with elements present in the first set but not in the second.
  =>Returns a new set with elements that are in either set, but not in both (i.e., uncommon elements).
d) union and update
=> union() method is used for obtaining unique of setobj1 and setobj2 and place them i setobj3
=> update() method adds elements from another set to the current set. It updates the set in-place 

e) / and //
=> division ('/')always return float value
=> floor division('//')
 division always return  int value 

 f) 'is not' and '!='
 => is not is a logical identity operator that checks whether two variables do NOT refer to the same object in memory.
 => '!=' is the inequality comparison operator in Python It checks whether two values are NOT equal.

 9) operator=> operator is a special symbol are used to performe operation  on data
 10) 200
     40






    
'''