userInput = input("Press 1 to get the area of a square.\n Press 2 to get the area of a rectangle.\n Press 3 to get the area of a circle.\n Press 4 to get the area of a triangle.\n")
if userInput == "1":
    LengthSq = int(input("Please enter the side in metres."))
    print(LengthSq * LengthSq,"square metres")
elif userInput == "2":
    LengthR = int(input("Please enter the length in metres."))
    BreadthR = int(input("Please enter the breadth in metres."))
    print(LengthR * BreadthR,"square metre")
elif userInput == "3":
    RadiusC = int(input("Please enter the radius of the circle in metres."))
    print(RadiusC * RadiusC * 22/7, "square metre")
elif userInput == "4":
    BaseT = int(input("Please enter the length of base in metres."))
    HeightT = int(input("Please enter the Height in metres."))
    print(BaseT * HeightT * 1/2,"Square metres")