# module= a file containing python code. May contain functions,classes etc.
# used with modular programing , which is used to separate program into parts.

def Hello():
    print("Say! Hello")

def Bye():
    print("Good Bye")


def printStarNew(row,col):
    if(row==0):
        return
    t=col
    printStarNew(row - 1, col - 1)
    while(t!=0):

        print("*", end=" ")
        t=t-1
    print(" ")





def printStar(r,c):
    if(r==0):
        return
    t=r
    while(t!=0):
        print("*",end=" ")
        t=t-1
    print(" ")
    printStar(r-1,c-1)

