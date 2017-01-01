from turtle import *
def spiral(sideLen, angle, scaleFactor, minLength):
    '''sideLen is the length of the current side;
       angle is the amount the turtle turns left to draw the next side;
       scaleFactor is the multiplicative factor by which to scale the next side 
       (it is between 0.0 and 1.0);
       minLength is the smallest side length that the turtle will draw.
    '''
    # solution
    if sideLen >= minLength:
        fd(sideLen)
        lt(angle)
        spiral(sideLen*scaleFactor, angle, scaleFactor, minLength)


'''
To test the function with large values, we need to move the turtle from (0,0) in the center
of the canvas to some other point. However, whenever the turtle moves, it leaves a trail behind.
This is why we used the methods pu() and pd() (pen up and pen down).
To keep everything clean, we'll wrap it all in the function.
'''
def drawSpiral(sideLen, angle, scaleFactor, minLength):
    clear()
    reset() 
    padding = 100
    width = sideLen + padding
    height = sideLen + padding
    pu()
    goto(-height/2+padding/2, -width/2+padding/2)
    pd()
    spiral(sideLen, angle, scaleFactor, minLength)
    


if __name__ == "__main__":
    setup(1.0,1.0)
    drawSpiral(625, 90, 0.7, 100)
    clear()
    reset()
    drawSpiral(200,90,0.9,10)
    clear()
    reset()
    drawSpiral(200,72,0.97,10)
    clear()
    reset()
    drawSpiral(200,121,0.95,15)
    exitonclick()
