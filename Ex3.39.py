#Exercise 3.39
#The computer game function collision() checks whether two circular objects collide;
#it returns True if they do and False otherwise. Each circular object will be given by
#its radius and the (x; y) coordinates of its center. Thus the function will take six numbers
#as input: the coordinates x1 and y1 of the center and the radius r1 of the first circle, and the
#coordinates x2 and y2 of the center and the radius r2 of the second circle.
def collision(x1,y1,r1,x2,y2,r2):
    if(((x2-x1)**2+(y2-y1)**2)<(r1+r2)**2):
        print(True)
    else:
        print(False)
collision(0,0,3,0,5,3)
collision(0,0,1.4,2,2,1.4)
