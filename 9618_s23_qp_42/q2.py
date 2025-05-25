class SaleData():
    #Public SaleID : STRING
    #Public Quantity :INTEGER

    #eta recored tai public attributes 

    def __init__(self,SaleIDP,QuantityP):
        self.SaleID=SaleIDP
        self.Quantity=QuantityP

#DECLARE CircularQueue:ARRAY[0:4] OF SaleData
global CircularQueue
global Head 
global NumberOfItems
CircularQueue=[SaleData("",-1)]*5
Head=0
Tail=0
NumberofItems=0

def Enqueue(NewRecord):
    global CircularQueue
    global Head
    global Tail
    global NumberofItems

    if NumberofItems==5:
        return -1
    else:
        CircularQueue[Tail]=NewRecord
        if Tail ==4:
            Tail=0
        else:
            Tail+=1
        NumberofItems=NumberofItems+1
        return 1

def Dequeue():
    global CircularQueue
    global Head
    global NumberofItems

    if NumberofItems==0:
        return SaleData("",-1)
    else:
        record=CircularQueue[Head]
        Head+=1
        if Head>4:
            Head=0
        NumberofItems=NumberofItems-1
        return record

def EnterRecord():
    ID=input("Enter the SaleID:  ")
    Quantity=int(input("Enter the Quantity: "))
    record=SaleData(ID,Quantity)
    if Enqueue(record)==-1:
        print("Full")
    else:
        print("Stored")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()

RecordCheck=Dequeue()
if RecordCheck.SaleID=="":
    print("queue is empty")
else:
    print("")
print(RecordCheck.SaleID+" "+str(RecordCheck.Quantity))

EnterRecord()


for x in range(5):
    Record=CircularQueue[x]
    print(Record.SaleID+" "+str(Record.Quantity))



