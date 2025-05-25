class node:
    def __init__(self,datap,nextnodep):
        self.data=datap
        self.nextnode=nextnodep

LinkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer=0
emptyList=5
print([[a.data,a.nextnode] for a in LinkedList] )

def outputNodes(linkedlist,startpointer):
    while startpointer !=-1:
        print(linkedlist[startpointer].data)
        startpointer=linkedlist[startpointer].nextnode


def addnode(linkedlist,startpointer,emptylist):
    datatoadd=input("Enter the data to add: ")

    if emptylist<0 or emptylist>9:
        return False
    else:
        newNode=node(int(datatoadd),-1)
        linkedlist[emptylist]=newNode
        previousPointer=0
        while(startpointer!=-1):
            previousPointer=startpointer
            startpointer=LinkedList[startpointer].nextnode
        linkedlist[previousPointer].nextnode=emptylist
        emptylist=LinkedList[emptylist].nextnode

        return True
    
outputNodes(LinkedList,startPointer)
outputNodes(LinkedList,startPointer)
x=addnode(LinkedList,startPointer,emptyList)
print("added node: ",x)
outputNodes(LinkedList,startPointer)