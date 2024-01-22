#parameter that will pack all arguments into a tuple

def add(num1,num2):
    return num1+num2
print("take input as parameter")
print(add(5,6))

def Add_args(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("take input as tuple")
print(Add_args(2,3,5,6,8,8))


#change in tuple doesnot not posible so if we wanna change then we have to create a list or
# basically convert the tuple into a list ten manipulate it.

def ADD_manipulate(*args):
    sum=0
    makelist= list(args)
    makelist[0]=90  #manipulate the first number
    for i in makelist:
        sum+=i
    return sum
print("Take input as tuple then make it a list")
print(ADD_manipulate(1,2,4,6,8))
