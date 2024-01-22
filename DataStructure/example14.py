val=int(input("Enter a Number : "))

arr=[int(i) for i in str(val)]

def isSame(arr):
    for x in range(0,len(arr)-1):
        if arr[x]!=arr[x-1]:
            return False
    return True

def GiveSum(val):
    sum=0
    while val!=0:
        sum=sum+val%10
        val=val//10
    return sum

if(isSame(arr)==True):
    print(GiveSum(val)*3)
else:
    print(GiveSum(val))





