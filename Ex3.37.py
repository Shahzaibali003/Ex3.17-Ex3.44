#Exercise 3.37
#Implement function points() that takes as input four numbers x1, y1, x2, y2 that
#are the coordinates of two points (x1; y1) and (x2; y2) in the plane. Your function should
#compute:
#• The slope of the line going through the points, unless the line is vertical
#• The distance between the two points
#Your function should print the computed slope and distance in the following format. If the
#line is vertical, the value of the slope should be string 'infinity'. Note: Make sure you
#convert the slope and distance values to a string before printing them.
import math
def points(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The Slope is : ",slope," The distance is : ",distance)
points(0,0,1,1)
