#Exercise 3.43
#The computer game function hit() takes five numbers as input: the x and y coordinates
#of the center and the radius of a circle C, and the x and y coordinates of a point P.
#The function should return True if point P is inside or on circle C and False otherwise.
def hit(x1,y1,r,x2,y2):
    if(((x2-x1)**2+(y2-y1)**2)<=r**2):
       print(True)
    else:
       print(False)
hit(0,0,3,3,0)
hit(0,0,3,4,0)
