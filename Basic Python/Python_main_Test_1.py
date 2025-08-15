'''
Data-Type
=> Data type is used for allocating memory space and for storing input (data).
=> Why they are important:
Python is a dynamically typed language. The programmer does not need to write the data type when declaring a variable.

i) List is mutable / Tuple is immutable
ii) List stores values using square brackets [] / Tuple stores values using parentheses ()

is => Checks if two variables point to the same object in memory
== => Checks if the values of two variables are equal
Example:

a = [5, 10, 20]  
b = [5, 10, 20]  
print(a == b)  
print(a is b)  
In real-life cases, using a list is not a good way to store data, but using a dictionary is a better way to store data systematically. Dictionary is more useful than list.

Example: We can't store student information in a systematic way using a list, because a student has different properties such as name, student_roll_no, student_id, etc.

We cannot modify a string in Python after creation because a string is immutable.

Immutable → int, float, str, tuple
Stored in fixed memory.
When you modify them, a new object is created.

Mutable → list, set, dict
Stored in memory with a pointer to data (like a reference).
You can change the data in-place without creating a new object.

a) pop() and remove()
pop() method is used for removing the last element of the list.
remove() method is used for removing the first occurrence of a specified value from the list.

b) intersection() and intersection_update()
intersection() is used for obtaining common elements from both set objects.
intersection_update() updates the calling set by keeping only the common elements.

c) difference() and symmetric_difference()
difference() returns a new set with elements present in the first set but not in the second.
symmetric_difference() returns a new set with elements that are in either set, but not in both.

d) union() and update()
union() returns a new set with unique elements from both sets.
update() adds elements from another set to the current set (in-place update).

e) / and //
/ (division) always returns a float value.
// (floor division) always returns an integer value.

f) is not and !=
is not is a logical identity operator that checks whether two variables do NOT refer to the same object in memory.
!= is the inequality comparison operator. It checks whether two values are NOT equal.


'''