class Node:
    #PRIVATE LeftPointer: INTEGER
    #PRIVATE Data: INTEGER
    #DECLARE RightPointer:INTEGER
    def __init__(self,DataP):
        self.__Data=DataP
        self.__RightPointer=-1
        self.__LeftPointer=-1

    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    def SetLeft(self,LeftPointernew):
        self.__LeftPointer=LeftPointernew
    def SetRight(self,RightPointerNew):
        self.__RightPointer=RightPointerNew
    def SetData(self,DataNew):
        self.__Data=DataNew


class TreeClass():
    #FirstNode : INTEGER
    #NumberNodes: INTEGER
    def __init__(self):
        self.__FirstNode=-1
        self.__NumberNodes=0
        self.__Tree=[] # OF TYPE NODE
        for x in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self,NewNode):
        if self.__NumberNodes==0:
            self.__Tree[self.__NumberNodes]=NewNode
            self.__NumberNodes+=1
            self.__FirstNode=0
        else:
            self.__Tree[self.__NumberNodes]=NewNode
            NodeAccess=self.__FirstNode
            direction=""

            while (NodeAccess !=-1):
                previous=NodeAccess
                if NewNode.GetData()<self.__Tree[NodeAccess].GetData():
                    NumberNodes=NumberNodes+1
    def OutputTree(self):
        if self.__NumberNodes==0:
            print("no nodes")
        else:
            for x in range(0,self.__NumberNodes):
                print(self.__Tree[x].GetLeft()," ",self.__Tree[x].GetData(),"",self.__Tree[x].GetRight())




thetree=TreeClass()
thetree.InsertNode(10)
thetree.InsertNode(Node(10))
thetree.InsertNode(Node(11))
thetree.InsertNode(Node(5))
thetree.InsertNode(Node(1))
thetree.InsertNode(Node(20))
thetree.InsertNode(Node(7))
thetree.InsertNode(Node(15))
thetree.OutputTree()