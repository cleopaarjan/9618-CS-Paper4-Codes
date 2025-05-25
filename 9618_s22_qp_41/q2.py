class Ballon():
    #PRIVATE Health:INTEGER
    #PRIVATE Colour:STRING
    #PRIVATE DefenseItem:STRING

    def __init__(self,ColourP,DefenceItemP):
        self.__DefenceItem=DefenceItemP
        self.__Colour=ColourP
        self.__Health=100
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self,newhealth):
        self.__Health=self.__Health+newhealth
    def checkHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
          


def Defend(BallonObject):
    strength=int(input("Enter the strength: "))
    BallonObject.ChangeHealth(strength)
    # ChangeHealth(BallonObject,strength)
    # ChangeHealth(self,newhealth)

    print("Your Defence is: ",BallonObject.GetDefenceItem())

    if BallonObject.checkHealth()==True:
        print("no health left")
    else:
        print("Health Remaining")
    return  BallonObject

UserDefence=input("Enter the defence Item: ")
UserColour=input("Enter the colour: ")
Ballon1=Ballon(UserColour,UserDefence)
Ballon1=Defend(Ballon1)