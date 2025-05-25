#DECLARE Queue:ARRAY [0:99] OF INTEGER
global Queuue
global Headpointer
global Tailpointer

Queue=[0]*100
Headpointer=-1
Tailpointer=0

def Enqueue(Data):
    global Queue
    global Headpointer
    global Tailpointer

    if Tailpointer<100:
        Queue[Tailpointer]=Data
        Tailpointer+=1
        if Headpointer==-1:
            Headpointer=0
        return True
    return False

def Dequeue():
    global Queue
    global Headpointer
    global Tailpointer

    if Headpointer==-1:
        print("queue is emoty")
    else:
        item=Queue[Headpointer]
        return item
    Headpointer+=1

    if Headpointer==Tailpointer:
        Tailpointer=0
        Headpointer=-1


finalflag=True
for num in range(1,21):
    temp=Enqueue(num)
    if temp==False:
        finalflag=False

if finalflag==True:
    print("sucessful")
else:
    print("Unsucessful")

def RecursiveOutput(Start):
    if Start<0:
        return 0
    else:
        return Queue[Start]+RecursiveOutput(Start-1)
    
temp=RecursiveOutput(Tailpointer)
print(temp)

