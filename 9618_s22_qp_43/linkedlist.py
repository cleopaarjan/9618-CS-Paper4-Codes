class Node:
    def __init__(self):
        self.__Name=None
        self.__Previous=None
        self.__Next=None
        
    def SetName(self,NameP):
        self.__Name=NameP
    def SetPrevious(self,previousP):
        self.__Previous=previousP
    def SetNext(self,nextp):
        self.__Next=nextp
    def GetName(self):
        return self.__Name
    def GetPrevious(self):
        return self.__Previous
    def GetNext(self):
        return self.__Next

def Main():
    #SETTING UP INITIAL LINKED LIST
    #START POINTER IS NOW NULL POINTER,list is empty
    StartPointer=None
    currentPointer=StartPointer
    Cont=True
    while Cont:
        x=input("lekho: ")
        if x=="":
            break
        y=Node()
        y.SetName(x)
        if StartPointer==None:
            StartPointer=y
            currentPointer=StartPointer
        else:
            while currentPointer.GetNext()!=None:
                currentPointer=currentPointer.GetNext()
            currentPointer.SetNext(y)
            y.SetPrevious(currentPointer)

    NewPointer=StartPointer
    print(NewPointer)
    while NewPointer.GetNext()!=None:
        print(NewPointer.GetName())
        NewPointer=NewPointer.GetNext()
    print(NewPointer.GetName())
    
Main()