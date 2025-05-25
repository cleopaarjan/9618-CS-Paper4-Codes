circular_queue=[[""] for x in range(10)]
head_pointer=0 #integer
tail_pointer=0 #integer
num_Items=0 #integer

def Enqueue(circularqueue,headpointer,tailpointer,numberitems,datatoadd):
    if numberitems>=10:
        return False #,circularqueue,headpointer,tailpointer,numberitems
    circularqueue[tailpointer]=datatoadd
    if tailpointer>=9:
        tailpointer=0
    else:
        tailpointer+=1
    numberitems+=1
    return True #,circularqueue,headpointer,tailpointer,numberitems
def Dequeue(circularqueue,headpointer,tailpointer,numberitems):
    if numberitems==0:
        return False
    else:
        returnvalue=circularqueue[headpointer]
        headpointer+=1
        if headpointer>=9:
            headpointer=0
        numberitems-=1
        return returnvalue
    
for x in range(11):
    inputString=input("enter a stirng : ")
    returned=Enqueue(circular_queue,head_pointer,tail_pointer,num_Items,inputString)
    if returned == True: 
        print("Successful") 
    else: 
        print("Unsuccessful")
    
returneditem=Dequeue(circular_queue,head_pointer,tail_pointer,num_Items)
print(returneditem)
returneditem=Dequeue(circular_queue,head_pointer,tail_pointer,num_Items)
print(returneditem)

#90%ok but not full