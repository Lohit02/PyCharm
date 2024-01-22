# parameter that will pack all arguments into a dictionary useful
# so that every function can accept varying amount of keyword argument

def Hello(**kwargs):
    #print("Hello"+kwargs['first']+kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


Hello(first="Lohit ",second="Kumar ",last="Biswas ")
