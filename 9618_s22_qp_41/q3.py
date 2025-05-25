#DECLARE QueueArray:ARRAY[0:9] OF STRING
QueueArray=[""]*10
HeadPointer=0 #INTEGER
TailPointer=0 #INTEGER
NumberOFItems=0 #INTEGER

#Can not pass Parameter as by ref so it as global

def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOFItems

    if NumberOFItems>=10:
        return False
    
    QueueArray[TailPointer]=DataToAdd
    if TailPointer>=9:
        TailPointer=0
    else:
        TailPointer=TailPointer+1
    
    NumberOFItems=NumberOFItems+1
    return True

def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOFItems

    if NumberOFItems==0:
        return False
    else:
        Value=QueueArray[HeadPointer]
        HeadPointer+=1
    if HeadPointer>9:
        HeadPointer=0

    NumberOFItems-=1
    return Value

for x in range(0,11):
    data=input("Enter the data to add: ")
    flag=Enqueue(data)

    if flag==True:
        print("the data is sucessfuly added")
    else:
        print("Queue is full")
flagdequeue=Dequeue()
flagdequeue2=Dequeue()
print(flagdequeue)
print(flagdequeue2)