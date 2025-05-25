
#DECLARE Animal:ARRAY[0:19] OF STRING
#DECLARE Colour:ARRAY[0:9] OF STRING

global Animal
global Colour
global AnimalTopPointer #INTEGER
global ColourTOpPointer #INTEGER
AnimaltopPointer=0
ColourTopPointer=0
Animal=[" "]*20
Colour=[" "]*10

def PushAnimal(DataToPush):
    global Animal
    global AnimaltopPointer
    if AnimaltopPointer==0:
        return False
    else:
        Animal[AnimaltopPointer]=DataToPush
        AnimaltopPointer=AnimaltopPointer+1
        return True

def PopAnimal():
    global Animal
    global AnimaltopPointer
    if AnimaltopPointer==0:
        return
    else:
        AnimaltopPointer=AnimaltopPointer-1
        returnedValue=Animal[AnimaltopPointer]
        return returnedValue
def ReadData():
    try :
        AnimalFile=open("AnimalData.txt","r")
        for line in AnimalFile():
            PushAnimal(line.strip())
        AnimalFile.close()
    except IOError:
        print("File dpesnt exist")

    try :
       ColourFile=open("ColourData.txt","r")
       for line in ColourFile:
            PushColour(line.strip())
       ColourFile.close()
    except IOError:
        print("File dpesnt exist")



def PushColour(DataToPush):
    global Colour
    global ColourTopPointer
    if ColourTopPointer==10:
        return False
    else:
        Colour[ColourTopPointer]=DataToPush
        ColourTopPointer+=1
        return True

def PopColour():
    global Colour
    global ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        ColourTopPointer=ColourTopPointer-1
        returnedValue=Colour[ColourTopPointer]
        return returnedValue
    
def OutPutItem():
    colourPop=PopColour()
    animalPop=PopAnimal()

    if colourPop=="":
        print("NO CLOUR")
        PushAnimal(animalPop)
    elif AnimaltopPointer=="":
        print("No animal")
        PushColour(colourPop)
    else:
        combine=colourPop +" "+animalPop
        print("Combine")

ReadData()
OutPutItem()
OutPutItem()
OutPutItem()
OutPutItem()
