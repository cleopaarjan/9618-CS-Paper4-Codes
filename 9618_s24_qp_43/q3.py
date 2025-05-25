global QueueHead
global QueueTail
global QueueData

QueueHead=-1
QueueTail=-1

QueueData=[""]*20 # ["" for a in range(20)]
def Enqueue(Data):
    global QueueHead
    global QueueTail
    global QueueData

    if QueueTail==19:
        return False
    elif QueueHead==-1:
        QueueHead=0
        QueueTail=0
        QueueData[QueueHead]=Data
        return True
    else:
        QueueTail+=1
        QueueData[QueueTail]=Data
        return True
    
def Dequeue():
    global QueueTail
    global QueueData
    global QueueHead

    if QueueHead==-1:
        return "false"
    else:
        dequeditem=QueueData[QueueHead]
        QueueHead+=1
        return dequeditem
    
def StoreItems():
    global QueueData
    global QueueTail

    Count=0
    for x in range(10):
        data=input("Enter data: ")
        Total=int(data[0])+int(data[2])+int(data[4])+(int(data[1])+int(data[3])+int(data[5]))*3
        Totaldiv=int(Total/10)
        if (Totaldiv==10 and data[6]=="X") or (str(Totaldiv)==data[6]):
            Result=Enqueue(data[:6])
            if Result==True:
                print("inserted item")
            else:
                print("queue full")
        else:
            Count+=1
        print(QueueData)

    print("there were",Count,"invalid items") 

StoreItems()
val=Dequeue()

if val==False:
    print("no data")
else:
    print(val)