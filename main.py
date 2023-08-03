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

student={"name":"","age":0,"country":'' ,"city":'',"job":'', 'skills': [], 'perant':{'father':'', 'mother':''}}
print(student)

for i in student:

   if type(student[i])== int:

          student[1] = int(input('enter the '+i+' :')) 
     
   elif type(student [i])== list:

       times = int(input('how many skills do you have?'))
       for i in range(times):
            student [1].append(input('enter the '+i+' :'))

   elif type(student [i])== dict:
      student[i]['father']= input('enter the father name:')
      student [i]['mother']= input('enter the mother name:')

   else:
        student [1]= input('enter the' + i+':')

print(student)
