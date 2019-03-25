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
xPos = []
yPos = []
zPos = []
xDist = []
yDist = []
zDist = []
xSpeed = []
ySpeed = []
zSpeed = []
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
    file.write('swift.set_polar(stretch=' + str(xDist[i]) + ', rotation=' + str(zDist[i]) + ', height=' + str(zDist[i]) + ', speed=' + str(xSpeed[i]) + ', wait=True)\n')


file.close()
#end
