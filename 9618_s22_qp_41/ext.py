# demo for global vars
# not included in current qp

globalvar1 = 10

print(globalvar1)

def localization(param1):
    global globalvar1 # declaring that, gloablvar1 is a globally available/recognized variable,
    # therefore, allow other instances of globalvar1 in this scope to use globalvar1's 
    # global memory location for data.
    print("param1 =",param1)
    print("globalvar1 (read only) =",globalvar1+10)
    globalvar1 = 90
    globalvar1 += 10
    print("globalvar1 (write+) =",globalvar1+10)
    

localization(globalvar1)
print(globalvar1)