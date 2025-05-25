class Tree:
    def __init__(self,TreeNameP,HeightGrowthP,MaxHeightP,MaxWidthP,EvergreenP):
        self.__TreeName=TreeNameP
        self.__HeightGrowth=HeightGrowthP
        self.__MaxHeight=MaxHeightP
        self.__MaxWidth=MaxWidthP
        self.__EverGreen=EvergreenP

    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__EverGreen
    
def ReadData():
    TreeObjects=[]
    try:
        file=open("Trees.txt")
        TreeData=[]
        TreeData=file.read().split("\n")
        SplitTrees=[]
        for item in TreeData:
            SplitTrees.append(item.split(","))
        file.close()
        for item in SplitTrees:
            TreeObjects.append(Tree(item[0],int(item[1]),int(item[2]),int(item[3]),item[4]))
    except IOError:
        print("-not found")
    return TreeObjects

def PrintTrees(Item):

    Final = "does not lose its leaves" 
    if Item.GetEvergreen() == "No": 
        Final = "loses its leaves each year" 
    print(Item.GetTreeName(), "has a maximum height", Item.GetMaxHeight(),"a maximum width",Item.GetMaxWidth(),"and grows", Item.GetGrowth(),"cm a year. It",Final)

TreeObjects = ReadData() 
PrintTrees(TreeObjects[0]) 

def ChooseTree(Trees): 
    Evergreen = input("Do you want a tree that loses its leaves (enter lose), or keeps its leaves (enter keep)") 
    MaxHeight = int(input("What is the maximum tree height in cm")) 
    MaxWidth = int(input("What is the maximum tree width in cm")) 
    Options = [] 
    if Evergreen.lower() == "keep" or Evergreen.lower() == "keep leaves" or Evergreen.lower() == "keeps its leaves": 
        keep = "Yes" 
    else: 
        keep = "No" 
    for Item in Trees: 
         
        if Item.GetMaxHeight() <= MaxHeight and Item.GetMaxWidth() <= MaxWidth and keep == Item.GetEvergreen(): 
            Options.append(Item) 
            PrintTrees(Item) 
        if len(Options) == 0: 
             print("No suitable trees")

ChooseTree(TreeObjects)