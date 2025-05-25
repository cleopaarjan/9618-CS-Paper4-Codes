class Picture:
    #PRIVATE Description : STRING
    #PRIVATE Height : INTEGER
    #PRIVATE FrameColour : STRING

    def __init__(self,Descriptionp,Heightp,Widthp,FrameColourp):

        self.__Description=Descriptionp
        self.__Height=Heightp
        self.__Colour=FrameColourp
        self.__Width=Widthp

    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__Colour
    def GetWidth(self):
        return self.__Width
    
    def SetDescription(self,description):
        self.__Description=description

PictureArray=[]
for i in range(100):
    PictureArray.append(Picture("",0,0,""))


def ReadData(pirctureArray):
    Filename="Pictures.txt"
    Counter=0
    try:
        File=open(Filename,"r")
        FechedData=str((File.readline()).strip())
        while FechedData !="":
            Description=FechedData
            Width=int((File.readline()).strip())
            Height=int((File.readline()).strip())
            Frame=((File.readline()).strip()).lower()
            PictureArray[Counter]=Picture(Description,Height,Width,Frame)

            FechedData=str((File.readline()).strip())
        File.close()
    except IOError:
        print("File not Found")
    return PictureArray


NumberPicturesInArray= ReadData(PictureArray)


FrameColour=input("")
MaxWidth=int(input("enter the "))
MaxHeight=int(input(" "))
for e in range(0,NumberPicturesInArray):
    if PictureArray[e].GetColour()==FrameColour:
        if (PictureArray[e].GetWidth()<=MaxWidth):
            if (Picture[e].GetHeight()<=MaxHeight):
                print(PictureArray[e].GetDescription()," ",str(PictureArray[e]).GetWidth()," ",str(PictureArray[e].GetHeight()))