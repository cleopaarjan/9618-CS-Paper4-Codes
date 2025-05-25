class Vehicle():
    #PRIVATE ID:STRING
    #PRIVATE MaxSpeed:INTEGER
    #PRIVATE CurrentSpeed:INTEGER
    #PRIVATE IncreaseAmount:INTEGER
    #PRIVATE HorizantalPosition:INTEGER
    def __init__(self,IDp,MaxSpeedp,CurrentSpeedp,IncreaseAmountp,HorizantalPositionp):
        self.__ID=IDp
        self.__MaxSpeed=MaxSpeedp
        self.__CurrentSpeed=CurrentSpeedp
        self.__IncreaseAmount=IncreaseAmountp
        self.__HorizantalPosition=HorizantalPositionp
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizantalPosition(self):
        return self.__HorizantalPosition
    def SetCurrentSpeed(self,CurrentSpeedNew):
        self.__CurrentSpeed=CurrentSpeedNew
    def SetHorizontalPosition(self,HorizontalPositionNew):
        self.__HorizantalPosition=HorizontalPositionNew
    def IncreaseSpeed(self):
        self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__CurrentSpeed=self.__MaxSpeed

        self.__HorizantalPosition=self.__HorizantalPosition+self.__CurrentSpeed
    def Outputprocedure(self):
        print("Current Speed: ",self.__CurrentSpeed)
        print("Horizontal Position: ",self.__HorizantalPosition)




class HeliCopter(Vehicle):
    #PRIVATE VerticalPosition: INTEGER
    #PRIVATE VerticalChange:INTEGER
    #PRIVATE MaxHeigt:INTEGER
    def __init__(self, IDp, MaxSpeedp, CurrentSpeedp, IncreaseAmountp, HorizantalPositionp,VerticalChangep,MaxGeightp):
        super().__init__(IDp, MaxSpeedp, CurrentSpeedp, IncreaseAmountp, HorizantalPositionp,VerticalChangep,MaxGeightp)
        self.__VerticalChange=VerticalChangep
        self.__MaxHeight=MaxHeight=MaxHeight     
        self.__VerticalPosition=0   

    def IncreaseSpeed(self):
        self.__VerticalPosition=self.__VerticalPosition+self.__VerticalChange
        if self.__VerticalPosition>self.__MaxHeight:
            self.__VerticalPosition=self.__MaxHeight
        super().IncreaseSpeed()  
    def Outputprocedure(self):
        super().Outputprocedure()
        print("vertical Position",self.__VerticalPosition)

car=Vehicle("Tiger",100,20)
Helicop=HeliCopter("Lion",350,40,3,100)

car.IncreaseSpeed()
car.IncreaseSpeed()

Helicop.IncreaseSpeed()
Helicop.IncreaseSpeed()
Helicop.Outputprocedure()
