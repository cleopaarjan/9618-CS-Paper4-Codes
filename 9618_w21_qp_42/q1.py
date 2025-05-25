def Unknown(xP,yP):
    if xP==yP:
        return 1
    elif xP<yP:
        print(xP+yP)
        return (Unknown(xP+1,yP)*2)
    else:
        print(xP+yP)
        return ((Unknown(xP-1,yP))//2)
print("10 and 15!")    
Unknown(10, 15)
print(Unknown)
print("10 and 10")
Unknown(10, 10)
print(Unknown)
print("15 and 10")
Unknown(15, 10)
print(Unknown)