NumberArray=[100,85,644,22,15,8,1]
#DECLARE LastItem:INTEGER
#DECLARE CheckItem:INTEGER
#DECLARE LoopAgain:BOOLEAN

def RecursiveInsersion(IntegerArray,NumberElements):
    if NumberElements<=1:
        return IntegerArray
    
    RecursiveInsersion(IntegerArray,NumberElements-1)
    LastItem=IntegerArray[NumberElements-1]
    CheckItem=NumberElements-2
    LoopAgain=True
    if CheckItem<0:
        LoopAgain=False
    elif IntegerArray[CheckItem]<LastItem:
        LoopAgain=False
    while LoopAgain:
        IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
        CheckItem=CheckItem-1

        if CheckItem<0:
            LoopAgain=False
        elif IntegerArray[CheckItem]<LastItem:
            LoopAgain=False
    

    IntegerArray[CheckItem+1]=LastItem
    return IntegerArray

RecursiveInsersion(NumberArray,len(NumberArray))
print("recursive: ",NumberArray)

def IterativeInsertion(IntegerArray,numberElements):

    for x in range(1,numberElements):
        lastitem=NumberArray[x]
        tempointer=x

        while tempointer>0 and IntegerArray[tempointer-1]>lastitem:
            IntegerArray[tempointer]=IntegerArray[tempointer-1]
            tempointer-=1
        IntegerArray[tempointer]=lastitem
        return IntegerArray
    
print("iterative:",IterativeInsertion(NumberArray,len(NumberArray)))

def BinarySearch(IntegerArray,First,Last,ToFind):
    if First>Last:
        return -1
    else:
        mid=(First+Last)//2
        if IntegerArray[mid]==ToFind:
            return mid
        elif IntegerArray[mid]>ToFind:
            return BinarySearch(IntegerArray,First,mid-1,ToFind)
        else:
            return BinarySearch(IntegerArray,mid+1,Last,ToFind)
        
sorted_array=IterativeInsertion(NumberArray,len(NumberArray))

Found=BinarySearch(sorted_array,0,6,644)
if Found==-1:
    print("not found")
else:
    print("the index is found",Found)
    