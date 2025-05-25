class Ballon:
    #DECLARE Health :INTEGER
    #DECLARE Colour : STRING
    #DECLARE Defence_Item: STRING

    def __init__(self,Defence_ItemP,colourP):
        self.__Health=100
        self.__Colour=colourP
        self.__Defence_Item=Defence_ItemP
    def GetDefenceItem(self):
        return self.__Defence_Item
    def ChangeHealth(self,change):
        self.__Health=self.__Health+change
    def  CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False

defence=input("enter defence method: ")
colour=input("enter the colour: ")
Ballon1=Ballon(defence,colour)

def Defend(ballonP):
    strenth=int(input("Enter the strength of opponent: "))
    ballonP.ChangeHealth(-strenth)
    print("You defended with ", str(ballonP.GetDefenceItem())) 
    if ballonP.CheckHealth()==True:
        print("defence faild")
    else:
        print("suceeded")
    return ballonP
ballo=Ballon(defence,colour)
Balloon1 = Defend(ballo) 