from koch import *

def snowflake(levels, size):
    # solution: just make a triange of koch curves!
    for i in range(3):
        koch(levels, size)
        rt(120)
    
if __name__ == "__main__":
    for i in range(4):
        snowflake(i, 150)
        clear()
        reset() 
    exitonclick()

