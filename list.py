#LIST
#Ques1
list=[]
a=int(input("enter value:"))
for x in range(a):
    x=input("enter items:")
    list.append(x)
print (list)
#Ques2
list2=['google','apple','facebook','microsoft','tesla']
list.extend(list2)
print(list)

#Ques3
list3=['tesla','google','apple','facebook','microsoft','tesla']
print(list3.count('tesla'))

#Ques4
list4=[6,8,9,7,1,5,3]
list4.sort()
print(list4)


#Ques5
A=['1','3','5','7']
B=['2','4','6','8']
C=A+B
C.sort()
print(C)

#Ques6
list5=[]
n=int(input("enter value:"))
for x in range(n):
    x=int(input("enter numbers:"))
    list5.append(x)
even=0
odd=0
for j in list5:
    if j%2==0:
        even+=1
    else:
        odd+=1
print('Total even numbers:',even)
print('Total odd numbers:',odd)



