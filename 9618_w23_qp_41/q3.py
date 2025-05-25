class Character():
    #PRIVATE Name :STRING
    #PRIVATE Xposition : INTEGER
    #PRIVATE Yposition : INTEGER
    def __init__(self,NameP,XPositionP,YPositionP):
        self.__Name=NameP
        self.__Xposition=XPositionP
        self.__Yposition=YPositionP
    def GetXPosition(self):
        return self.__Xposition
    def GetYPosition(self):
        return self.__Yposition
    def SetXposition(self,NewXposition):
        if NewXposition>10000:
           
           NewXposition=10000
        elif NewXposition<0:
           NewXposition=0 
        self.__Xposition=NewXposition
       
    def SetYposition(self,NewYposition):
        if NewYposition>10000:
           
           NewYposition=10000
        elif NewYposition<0:
           NewYposition=0 
        self.__Yposition=NewYposition     
    def Move(self,Direction):
        if Direction=="up":
            self.__Yposition=self.__Yposition+10
        elif Direction=="down":
            self.__Yposition=self.__Yposition+10 
        elif Direction=="left":
            self.__Xposition=self.__Xposition-10
        elif Direction=="right":
            self.__Xposition=self.__Xposition+10

Jack=Character("Jack",50,50)

class BikeCharacter(Character):
    def __init__(self, NameP, XPositionP, YPositionP):
        super().__init__(NameP, XPositionP, YPositionP)
    def Move(self, Direction):
            if Direction=="up":
                super().SetYPosition(super().GetYPosition()+20)
            elif Direction=="down":
                super().SetYPosition(super().GetYPosition()-20)
            elif Direction=="left":
                super().SetXPosition(super().GetXPosition()+20)
            elif Direction=="right":
                super().SetXPosition(super().GetXPosition()-20)

Karla=BikeCharacter("karla",100,50)
UserCharacter=input("choose character,jack/karla:")
UserDirection=input("Direction: up,down,left,right? Ans:")
if UserCharacter=="jack":
    Jack.Move(UserDirection)
    Xvalue=Jack.GetXPosition()
    Yvalue=Jack.GetYPosition()
    print("Jacks new position is X-",Xvalue,"y-",Yvalue)
elif UserCharacter=="karla":
    Karla.Move(UserDirection)
    Xvalue=Karla.GetXPosition()
    Yvalue=Karla.GetXPosition()
    print("Karla new position is x-",Xvalue,"Y-",Yvalue)

