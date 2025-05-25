class Vehicle:
    #DECLARE ID :STRING
    #DECLARE MaxSpeed:INTEGER
    #DECLARE CurrentSpeed: INTEGER
    #DECLARE IncreaseAmount :INTEGER
    #DECLARE  HorizantalPosition: INTEGER

    def __init__(self,IDP,MAXSpeedP,IncreaseAmountP):
        self.__ID=IDP
        self.__MaxSpeed=MAXSpeedP
        self.__CurrentSpeed=0
        self.__IncreaseAmount=IncreaseAmountP
        self.__HorizontalPosition=0

    def GetCurrentSpeed(self):
       return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizantalPosition(self):
        return self.__HorizontalPosition
    def SetCurrentSpeed(self,NewCurrentSpeed):
        self.__CurrentSpeed=NewCurrentSpeed
    def SetHorizantalPosition(self,Newhp):
        self.__HorizontalPosition=Newhp

    def IncreaseSpeed(self):
        self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__CurrentSpeed=self.__MaxSpeed
        self.__HorizontalPosition=self.__HorizontalPosition+self.__CurrentSpeed

    def OutputcurrentPosition(self):
        print("Current position - ",self.__HorizontalPosition)
        print("Current Speed- ",self.__CurrentSpeed)
    
class Helicopter(Vehicle):
    #VerticalPosition:INTEGER
    #Verticalchange:INTEGER
    #MaxHeight :INTEGER
    def __init__(self,IDP,MAxSpeedP,IncareaseAmountP,VerticalChangeP,MaxHeightP):
        Vehicle.__init__(self,IDP,MAxSpeedP,IncareaseAmountP)
        self.__VerticalChange=VerticalChangeP
        self.__VerticalPosition=0
        self.__MaxHeight=MaxHeightP

    def IncreaseSpeed(self):
        self.__VerticalPosition=self.__VerticalChange+self.__VerticalPosition
        if self.__VerticalPosition>self.__MaxHeight:
            self.__VerticalPosition=self.__MaxHeight
        Vehicle.SetCurrentSpeed(self,Vehicle.GetCurrentSpeed(self)+Vehicle.GetIncreaseAmount(self))
        if Vehicle.GetCurrentSpeed(self)>Vehicle.GetMaxSpeed(self):
            Vehicle.SetCurrentSpeed(self,Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizantalPosition(self,Vehicle.GetHorizantalPosition(self)+Vehicle.GetCurrentSpeed(self))
    def OutputcurrentPosition(self):
        print("Current position-",Vehicle.GetHorizantalPosition(self))
        print("Current speed- ",Vehicle.GetCurrentSpeed(self))
        print("Vertical position- ",self.__VerticalPosition)



Car = Vehicle("Tiger", 100, 20) 
Heli1 = Helicopter("Lion", 350, 40, 3, 100) 
Car.IncreaseSpeed() 
Car.IncreaseSpeed() 
Car.OutputcurrentPosition() 
print("") 
Heli1.IncreaseSpeed() 
Heli1.IncreaseSpeed() 
Heli1.OutputcurrentPosition() 
    
