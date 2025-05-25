class Queue:
    def __init__(self):
        self.QueueArray=[]
        HeadPointer=0 #integer
        TailPointer=0 #integer
        for x in range(0,100):
            self.QueueArray.append(-1)
class Queue:
    def __init__(self):
        self.QueueArray=[]
        for x in range(0,100):
            self.QueueArray.append(-1)

        self.HeadPointer=-1
        self.TailPointer=0
TheQueue=Queue()

def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer==-1:
        AQueue.QueueArray[AQueue.HeadPointer]=TheData
        AQueue.HeadPointer=0
        AQueue.TailPointer+=1
        return 1
    elif AQueue.TailPointer>99:
        return -1
    else:
        AQueue.QueueArray[AQueue.TailPointer]=TheData
        AQueue.TailPointer+=1
        return 1
    
def ReturnAllData(TheQueue):
    Temp=""
    for x in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        Temp=Temp+str(TheQueue.QueueArray[x])+""
    return Temp

for x in range(10):
    Continue=True
    while Continue==True:
        datainput=int(input("integer:"))
        if datainput>-1:
            Continue=False

if Returnvalue==-1:
    print("queue full")
else:
    print("inserted")

print(ReturnAllData(TheQueue))

def Dequeue(AQueue):
    if AQueue.HeadPointer=100 or AQueue.HeadPointer==-1 or AQueue.HeadPointer==AQueue.TailPointer :
        return -1
    else:
        teep=AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.Headpointer=AQueue.Headpointer+1
        return AQueue
    

ReturnValue = Dequeue(TheQueue) 
if ReturnValue == -1: 
    print("Queue empty") 
else: 
    print(ReturnValue, " is returned") 
ReturnValue = Dequeue(TheQueue) 
if ReturnValue == -1: 
    print("Queue empty") 
else: 
    print(ReturnValue, " is returned") 
print(ReturnAllData(TheQueue)) 