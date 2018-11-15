#Exercise 3.44
#Write a function distance() that takes as input a number: the time elapsed (in seconds)
#between the flash and the sound of thunder. Your function should return the distance
#to the lightning strike in kilometers. The speed of sound is approximately 340:29 meters per
#second; there are 1000 meters in one kilometer.
def distance(time):
    #in m/s
    speedOfSound=340.29
    #in k/s
    speedOfSound=(340.29)/1000
    #distance
    return time*speedOfSound
distance(3)
