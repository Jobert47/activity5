userinput= input("Enter Name: ")
rooms = [
    ["juan", "pedro", "clear"],
    ["as", "ab", "Eriz"],
    ["gcc", "gi", "ckc",]
]

for room in rooms:
     for name in room:
        if name == userinput:
            print( userinput  + " yes")
        else:
            print( userinput  +  " No")
    
