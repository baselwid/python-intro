
# var1 ='value'
# print (type(var1))
# print (var1[0])
# print (var1[-1])
# print (var1[1:3])
# print(len(var1))
# var2= 5
# print (type(var2))

# var3 = 3.14
# print (type(var3))

# var4 = True
# print(type(var4))

# var5 = 5+6j
# print (type(var5))
# str1 ='hello'
# str1= 'y'+str1[1:len(str1)]
# print (str1)
# print(str1[0:2]+'mm'+str1[4:len(str1)])

students=[]
student={}
renter=True
while renter:
    insertTime=int(input("how many key do you want to add  "))
    for i in range(insertTime):
        deckey=input("enter the key")
        decvalueTybe=int(input("enter the tybe of the value where 1 for str 2 for int 3 for list 4 for dec"))
        if decvalueTybe==1:
            decvalueTybe=input("enter the value")
        elif decvalueTybe==2:
            decvalueTybe=int(input("enter the value"))
        elif decvalueTybe==3:
            decvalueTybe=[]
            item=int(input('hwo many '+deckey+'do you have?'))
            for j in range(item):
                decvalueTybe.append(input('enter the '+ deckey +':'))
        elif decvalueTybe==4:
            decvalueTybe={}
            item=int(input('hwo many '+deckey+'do you have?')) 
            for j in range(item):
                student[input('enter the key')]=input('enter the value') 

    student[deckey]=decvalue
    students.append(student)
    
print(student)