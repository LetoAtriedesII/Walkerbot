'''
Author: Adam Novak
Description: this code is designed to parse data from a csv file and
create motion commands for the robot
Date modified: 03/25/19
Version: 1.0
'''

'''
+x is away from base
+y is towards power cable side of base
+z is upwards
speed is [0, 100] if version is 4.0+
speed is [0, 100000] if 3.0 < version < 4.0

x (mm)          :  150 -> 300
y (mm)          : -150 -> 150 
z (mm)          :   30 -> 150 
speed (mm/s?)   :    0 -> 100
'''

import csv
#vectors of points in space
xPos = [] 
yPos = []
zPos = []
#vectors of differences in points in space
xDist = []
yDist = []
zDist = []
xSpeed = []
ySpeed = []
zSpeed = []

#robot constraint variables
absX = 200
absY = 0
absZ = 100
speed = 100

file = open('parseout.txt','w') 

with open('bnj_walk.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        xPos.append(int(row[1]))
        yPos.append(int(row[2]))
        zPos.append(int(row[3]))
        xSpeed.append(int(row[4]))
        ySpeed.append(int(row[5]))
        zSpeed.append(int(row[6]))

for i in range(0, len(xPos)-1):
    xDist.append(xPos[i] - xPos[i+1])
    yDist.append(yPos[i] - yPos[i+1])
    zDist.append(zPos[i] - zPos[i+1])
    
    #x (mm)          :  150 -> 300
    absX = absX + zDist[i] 
    if absX > 300:
        absX = 300
    elif absX < 150:
        absX = 150

    #y (mm)          : -150 -> 150 
    absY = absY + yDist[i]
    if absY > 150:
        absY = 150
    elif absY < -150:
        absY = -150

    #z (mm)          :   30 -> 150 
    absZ = absZ + zDist[i]
    if absZ > 150:
        absZ = 150
    elif absZ < 30:
        absZ = 30

    #speed (mm/s?)       :   0 -> 250
    if speed > 250:
        speed = 150
    elif speed < 0:
        speed = 0

    file.write('swift.set_position(x=' + str(absX) + ', y=' + str(absY) + ', z=' + str(absZ) + ', speed=' + str(speed)+ ', wait=true)\n')


file.close()
#end
