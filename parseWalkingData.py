'''
Author: Adam Novak
Description: this code is designed to parse data from a csv file and
create motion commands for the robot
Date modified: 03/25/19
Version: 1.0
'''

'''
stretch (mm)        : 150 -> 300
rotation (degrees)  :   0 -> 180 
height (mm)         :  30 -> 150 
speed (mm/s?)       :   0 -> 250
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
rotationX = 90
heightY = 30
stretchZ = 150
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
    
    #rotation (degrees)  :   0 -> 180 
    rotationX = rotationX + zDist[i] 
    if rotationX > 180:
        rotationX = 180
    elif rotationX < 0:
        rotationX = 0

    #height (mm)         :  30 -> 150 
    heightY = heightY + yDist[i]
    if heightY > 150:
        heightY = 150
    elif heightY < 30:
        heightY = 30

    #stretch (mm)        : 150 -> 300
    stretchZ = stretchZ + zDist[i]
    if stretchZ > 300:
        stretchZ = 300
    elif stretchZ < 150:
        stretchZ = 150

    #speed (mm/s?)       :   0 -> 250
    if speed > 250:
        speed = 150
    elif speed < 0:
        speed = 0


    
    file.write('swift.set_position(x=' + str(stretchZ) + ', y=' + str(rotationX) + ', z=' + str(heightY) + ', speed=' + str(speed)+ ', wait=true)\n')


file.close()
#end
