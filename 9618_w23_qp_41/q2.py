#DECLARE Queue : ARRAY[0:49] OF STRING
global Queue
global HeadPointer #int
global TailPOinter #int
Queue=[""]*50
Headpointer=-1
TailPointer=0

def Enqueue(value):
    global Queue
    global Headpointer
    global TailPointer

    if TailPointer ==50:
        print("The Queue is full")
    else:
        Queue[TailPointer]=value
        TailPointer=TailPointer+1
        if Headpointer ==-1:
            Headpointer=0


def Dequeue():
    global Queue
    global TailPointer
    global Headpointer

    if Headpointer==-1:
        print("The queue is empty")
        return "Empty"
    else:
        RemovedItem=Queue[Headpointer]
        Headpointer=Headpointer+1

    
    if Headpointer==TailPointer:
       Headpointer=-1
       TailPointer=0
    return RemovedItem 


def ReadData():
    try:
        file=open("QueueData.txt","r")
        for line in file:
            Enqueue(line.strip())
        file.close()
    except IOError:
        print("file doesnt exist")
#ReadData()
#print(Queue)

class RecordData():
    #PUBLIC ID:STRING
    #PUBLIC Total : INTEGER
    def __init__(self,IDP,TotalP):
        self.ID=IDP
        self.Total=TotalP
#DECLARE Records :ARRAY[0:49] OF RecordData

global Records 
global NumberRecords
NumberRecords=0
Records=[]
for x in range(50):
    Records.append(RecordData("",0))

def TotalData():
    global NumberRecords
    global Records

    DataAccessed=Dequeue()
    Flag=False
    if NumberRecords==0:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        Flag=True
        NumberRecords=NumberRecords+1
    else:
        for x in range(0,NumberRecords):
            if Records[x].ID==DataAccessed:
                Records[x].Total=Records[x].Total+1
                Flag=True
    if Flag==False:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        NumberRecords=NumberRecords+1


def OutputRecords():
    global NumberRecords
    for x in range(NumberRecords):
        print("ID",Records[x].ID,"Total",Records[x].Total)

ReadData()
while Headpointer !=-1:

    TotalData()
print(NumberRecords)
OutputRecords()
