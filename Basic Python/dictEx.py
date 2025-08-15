"""
dict => dict is comma sep key and value pair eithin {}

syntax:
    var={k1:v1 , k2:v2 , k3:v3}   

key => unique and immutable     

value=> duplicate and both -> mutable and immutable 

 """

detail={'name':'vaibhav','age':20, 'mobile':8767843199, 'city':'pune'}

print(detail,type(detail))
#==============================================================================================    


square={2:4,3:9,4:16,5:25}

print(square,type(square))
#==============================================================================================    


# # student={1:'pavan',2:'ram',1:'om'}
# # print(student)
#==============================================================================================    

ajay_details={'roll':1, 'name':'ajay', 'course':['python','java','aws'], 'per':80 , 'marks':{'t1':70 , 't2':80, 't3':'90'}}
print(ajay_details,type(ajay_details))
#==============================================================================================    

#create a dict to represent your details

vaibhav_arjun={'rollno':2184, 'Education':'TYBCA', 'mobileno':876756585 , 'Address':'pune'}
print(vaibhav_arjun)
#==============================================================================================    

# #create a dict to represet cube 

cube={1:1 ,2:8, 3:27 , 4:64 , 5:125 , 6:216 ,7:343 , 8:512, 9:729 , 10:100}

print(cube)
#==============================================================================================    


capital={'MH':'mumbai', 'goa':'panji', 'bihar':'patna', 'madhepradesh':'bhopal'}
print(capital)
#==============================================================================================    
course={'subject':'python','duration':'5 month','trainer':'vaibhav patil'}
institute={'institute':'kiran accadamy','branch':'karvenagar'}
# print(course.keys())
# print(course.values())
# print(course.items())
# print(course.popitem())
course.update(institute)
print(course)

#==============================================================================================    


courses={'python':{'title':'python','duration':'5 month','trainer':'vaibhav patil'},'java':{'title':'angular','duration':'6 month','trainer':'kiran sir'},'angular':{'title':'angular','duration':'2 month','trainer':'vaibhav patil'}}
print(courses)

print(courses['angular'])
print(courses['python'][ 'trainer'])
# courses.update['java']['title']='python ful stack web dev with AI'
courses['java']['title'] = 'Python Full Stack Web Dev with AI'
print(courses)
#==============================================================================================    

courses.update({'AWS': {'title': 'AWS', 'duration': '4 month', 'trainer': ' patil Sir'}})
print(courses)
print(list(courses.keys()))


#==============================================================================================    

