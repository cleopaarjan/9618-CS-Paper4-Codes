class Employee():
    #PRIVATE HourlyPay:REAL
    #PRIVATE EmployeeNumber:STRING
    #PRIVATE PayYear2022:ARRAY [0:51] OF REAL
    def __init__(self,HourlyPayP,EmployeeNumberP,JobTitleP):
        self.__HourPay=HourlyPayP
        self.__EmployeeNumber=EmployeeNumberP
        self.__JobTitle=JobTitleP
        self.__PayYear2022=[0.0]*52

    def GetEmployeenumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self,WeekNumber,HourWorked):
        pay=self.__HourPay+HourWorked
        self.__PayYear2022[WeekNumber-1]=pay

    def GetTotalPay(self):
        Total=0
        for x in range(52):
            Total=Total+self.__PayYear2022[x]

            return Total

class Mananager(Employee):
    #PRIVATE BonousValue:REAL
    def __init__(self, HourlyPayP, EmployeeNumberP, JobTitleP,BonousP):
        super().__init__(HourlyPayP, EmployeeNumberP, JobTitleP)
        self.__BonousValue=BonousP

        def SetPay(self,WeekNumber,Hourworked):
            NewHours=Hourworked+(Hourworked*(self.__BonousValue/100))
            super().SetPay(WeekNumber,NewHours )

#DECLARE EmployeeArray : ARRAY[0:7] OF Employee
EmployeeArray=[Employee(0.0,"","")]*8
MaybeBonus=""
JobTitle=""
try:
    Employeefile=open("Employees.txt","r")
    for x in range(8):
        HourlyPay=float(Employeefile.readline().strip())
        EmployeeNumber=Employeefile.readline().strip()
        MaybeBonus=Employeefile.readline().strip()
        try:
            Bonus=float(MaybeBonus)  #float("junior developer")
            JobTitle=Employeefile.readline().strip()
            EmployeeArray[x]=Mananager(HourlyPay,EmployeeNumber,JobTitle,Bonus)
        except:
            JobTitle=MaybeBonus
            EmployeeArray[x]=Employee(HourlyPay,EmployeeNumber,JobTitle)

    Employeefile.close()
except IOError:
    print("File not found")

def EnterHours():
    try:
        HoursFile=open("HoursWeek1.txt","r")
        for x in range(8):
            EmployeeID=HoursFile.readline().strip()
            Hoursworked=float(HoursFile.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeenumber()==EmployeeID:
                    EmployeeArray[y].SetPay(1,Hoursworked)
        HoursFile.close()
    except IOError:
        print("File not Exist")


EnterHours()
for x in range(8):
    EmployeeNumber=EmployeeArray[x].GetEmployeenumber()

    TotalPay=EmployeeArray[x].GetTotalPay()
    print(EmployeeNumber+" "+str(TotalPay))



