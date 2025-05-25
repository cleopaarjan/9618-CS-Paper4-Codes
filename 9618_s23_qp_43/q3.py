Animal=[]*20
Colour=[]*10

global AnimalTopPointer
global ColourTopPointer


AnimalTopPointer=0
ColourTopPointer=0
def PushAnimal(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer==20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer=AnimalTopPointer+1
    return True

def PopAnimal():

    global AnimalTopPointer
    global ColourTopPointer
    #DECLARE ReturnData:STRING
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer=AnimalTopPointer-1
        return ReturnData

def ReadData():
    try:

        global AnimalTopPointer
        global ColourTopPointer

        Animalfilename="AnimalData.txt"
        Animalfile=open(Animalfilename,"r")
        Animalline=Animalfile.readline().strip()
        while Animalline !="":
            PushAnimal(Animalline)
            Animalline=Animalfile.readline().strip()
        Animalfile.close()
        
        Colourfilename="ColourData.txt"
        Colourfile=open(Colourfilename,"r")
        Colourline=Colourfile.readline().strip()
        while Colourline !="":
            PushColour(Colourline)
            Colourline=Colourfile.readline().strip()
        Colourfile.close()
        
    except IOError:
        print("file nei bro")

def PushColour(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer==10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer=ColourTopPointer+1
    return True

def PopColour():
    global AnimalTopPointer
    global ColourTopPointer
    #DECLARE ReturnData:STRING
    if ColourTopPointer==0:
        return ""
    else:
        ReturnData=Colour[ColourTopPointer-1]
        ColourTopPointer=ColourTopPointer-1
        return ReturnData


def OutPutItem():
    global AnimalTopPointer
    global ColourTopPointer
    a=PopAnimal()
    b=PopColour()
    if b=="":
        print("No Colour")
        PushAnimal(a)
    elif a=="":
        print("no Animal")
        PushColour(b)
    else:
        print(b,a)


ReadData()
OutPutItem()
OutPutItem()
OutPutItem()
OutPutItem()
