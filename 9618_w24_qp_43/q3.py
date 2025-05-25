LinkedList=[[[]for x in range(2)]for x in range(20)]
FirstNode=-1
FirstEmpty=0
Nextfree=0



def InsertData():
    global FirstNode
    global FirstEmpty
    global Nextfree
    if FirstNode==-1:
        FirstNode=0
    for x in range(5):
        data=int(input("number: "))
        
        LinkedList[Nextfree][0]=data
        LinkedList[Nextfree][1]=FirstNode
        FirstNode=Nextfree
        lastInserted = Nextfree
        Nextfree+=1
        
    LinkedList[lastInserted][1] = -1

def OutputLinkedList():
    print(LinkedList)
InsertData()
OutputLinkedList()


def RemoveData(value):
    global FirstNode
    global LinkedList

    current = FirstNode
    previous = -1

    while current != -1:
        if LinkedList[current][0] == value:
            if previous == -1:
                # The node to remove is the first node
                FirstNode = LinkedList[current][1]
            else:
                # Skip over the current node
                LinkedList[previous][1] = LinkedList[current][1]

            # Optionally mark the removed node as empty (add to free list)
            LinkedList[current] = [None, None]
            return  # Exit after removing first occurrence
        else:
            previous = current
            current = LinkedList[current][1]


RemoveData(5)
print("AFTER")
OutputLinkedList()
