#DECLARE StackData:ARRAY[0:9] OF INTEGER
#DECLARE StackPointer:INTEGER

global StackData
global StackPointer
StackData=[0]*10
StackPointer=0

def PrintArray():
    print("The StackPointer is",StackPointer)
    for x in range(0,10):
        print(StackData[x])
def Push(number):
    global StackData
    global StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer]=number
        StackPointer=StackPointer+1
        return True
    
def Pop():
    global StackData
    global StackPointer

    if StackPointer==0:
        return -1
    else:
        StackPointer-=1
        temp=StackData[StackPointer]
        return temp
    
for x in range(0,11):
    value=int(input("enter the number you want to add: "))
    flag=Push(value)
    if flag==True:

        print("Sucessfully added")
    else:
        print("Stack is full")

PrintArray()

Pop()
Pop()

PrintArray()






