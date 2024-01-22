list=[]

n=int(input("enter the no of elements: "))
for i in range (n):
    ele=int(input())
    list.append(ele)

print(list)

result=''

for element in list:
        result += str(element)
print(result)