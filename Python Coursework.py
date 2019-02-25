from graphics import*

def askUserColour():
    coloursList = []
    validColours = ["red", "green", "blue", "magenta", 
                    "cyan", "orange", "brown", "pink"]
    while True:
          
        colour = input("Enter a colour for your patch (eg: red, green, " +   
                        "blue, magenta,   cyan, orange, brown and pink): ")

        if colour in validColours:
        #checks if the colour is valid
            coloursList.append(colour)   
            validColours.remove(colour) 
               
        else:
            print("Invalid, please re-enter eg:", validColours)
        
        if len(coloursList) == 3:
            print("Your colour list for your patch is complete")
            break
            
    return coloursList
            
def askUserSize():
    while True:
        
        validSizes = ["5", "7", "9", "11"]
        size = input("Enter patch size (eg: 5, 7, 9, 11): ")
        #checks input is a valid type
        
        if size in validSizes:
            return int(size)
            break
            
        else:
            print("Invalid, please re-enter (eg:", validSizes, ": ")
            

#This patch creates the final digit pattern
def drawFinalDigitPatch(win, startX, startY, coloursList):
    
    for i in range(0, 100, 20):

        line1 = Line(Point(startX + i, startY),  
                     Point(startX + 100, startY + 100 - i))
        line2 = Line(Point(startX, startY + i), 
                     Point(startX + 100 - i, startY + 100))
        line1.draw(win)
        line1.setOutline(coloursList)
        line2.draw(win)
        line2.setOutline(coloursList)
        
        line3 = Line(Point(startX + i, startY), 
                     Point(startX, startY + i))
        line4 = Line(Point(startX + i, startY + 100),
                     Point(startX + 100, startY + i))
        line3.draw(win) 
        line3.setOutline(coloursList)
        line4.draw(win) 
        line4.setOutline(coloursList)
        

        
#Draws part of the penultimate patch
def drawPenultimatePatch1(win, startX, startY, coloursList, i, z):
    
    rectangle1 = Rectangle(Point(startX + i, startY + z),
                           Point(startX + 20 + i, startY + 20 + z))
    rectangle1.draw(win)
    rectangle1.setFill("white")
    
    triangle1 = Polygon(Point(startX + i, startY + z), 
                        Point(startX + i, startY + 20 + z),
                        Point(startX + 10 + i, startY + 10 + z))
    triangle1.draw(win)
    triangle1.setFill(coloursList)
    
    triangle2 = Polygon(Point(startX + 20 + i, startY + z),
                        Point(startX + 20 + i, startY + 20 + z),
                        Point(startX + 10 + i, startY + 10 + z))
    triangle2.draw(win)
    triangle2.setFill(coloursList)
    
#Draws second part of the penultimate patch
def drawPeniltimatePatch2(win, startX, startY, coloursList, i, z):
    
    rectangle2 = Rectangle(Point(startX + i, startY + z),
                           Point(startX + 20 + i, startY + 20 + z))
    rectangle2.draw(win)
    rectangle2.setFill("white")
    
    triangle3 = Polygon(Point(startX + i, startY + z),
                        Point(startX + i + 20, startY + z),
                        Point(startX + 10 + i, startY + 10 + z))
    triangle3.draw(win)
    triangle3.setFill(coloursList)
    
    triangle4 = Polygon(Point(startX + i, startY + 20 + z),
                Point(startX + 20 + i, startY + 20 + z),
                Point(startX + 10 + i, startY + 10 + z))
    triangle4.draw(win)
    triangle4.setFill(coloursList)
    
        
def drawPeniltimatePatch(win, x, y, coloursList):
    
    count = 0
    for z in range (0, 100, 20):
        for i in range (0, 100, 20):
        
            if count % 2 == 0:
                
                drawPenultimatePatch1(win, x, y, coloursList, i, z)
       
            else:
                drawPeniltimatePatch2(win, x, y, coloursList, i, z)  
             #draws the two parts of the peniltimate patch in the window
             
            count += 1
            
def drawPatchWork(win, x, y, coloursList):

    i = 100
    size = x
    size = y
    colourListIndex = 0

    for y in range(0, size * 100, 100):
        for x in range(0, size * 100, 100):
            
            if x < i:
                drawFinalDigitPatch(win, size + x, size + y, 
                                    coloursList[colourListIndex])
                colourListIndex += 1
                
#makes the list loop through the differnt colours when drawing each patch

            else:
                drawPeniltimatePatch(win, size + x, size + y, 
                                     coloursList[colourListIndex])
                colourListIndex += 1

            if colourListIndex == 3:
                colourListIndex = 0
                
        i = i + 100

def main():
    
    size = askUserSize()
    coloursList = askUserColour()
    win = GraphWin("PW", size * 100, size * 100)
    
    drawPatchWork(win, size, size, coloursList)
    
    win.getMouse()
    win.close()
    
main()
        


    
