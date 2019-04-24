'''
Author: Adam Novak

Description: This code is designed to parse data from a csv file and
create motion commands for the robot

Instructions: Use this script in conjuction with the Workforce Motion Logger. Save the files
from the program and convert the .wfd file to a .csv file by changing the extension. 
Change inputFileName to be the name of the csv file you wish to read. Run the script.
parseWalkingData.py will contain all of the motion commands for the robot. Place each of these
in a file and run the code. 

TODO: Note that the speed is currently not dependent on the PASS sensor's motion, but can easily
be implemented once a scaling factor is determined. Instead, the speed will be set to a constant value
throughout the path.

Date modified: 04/15/19
Version: 1.0
Environment: Python 3.7
'''

'''
Coordinates of the robot that are used in this program.
(Note that this is not the maximum range of the robot.)
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
inputFileName = 'exampleStand.csv'
outputFileName = 'parseout.txt'

#open the output file
file = open(outputFileName,'w') 
#read the csv file
with open(inputFileName) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if len(row[1]) > 0 and len(row[2]) > 0 and len(row[3]) > 0 and len(row[4]) > 0 and len(row[5]) > 0 and len(row[6]) > 0:
            xPos.append(int(row[1]))
            yPos.append(int(row[2]))
            zPos.append(int(row[3]))
            xSpeed.append(int(row[4]))
            ySpeed.append(int(row[5]))
            zSpeed.append(int(row[6]))

#find the delta for each of the axes and output a line to the file
for i in range(0, len(xPos)-1):
    xDist.append(xPos[i] - xPos[i+1])
    yDist.append(yPos[i] - yPos[i+1])
    zDist.append(zPos[i] - zPos[i+1])
    
    '''
    TODO: Set the scaling factor to properly reflect the sensor's speed
    xSpeed.append(xPos[i] - xPos[i+1])
    ySpeed.append(yPos[i] - yPos[i+1])
    zSpeed.append(zPos[i] - zPos[i+1])
    speed = scalingFactor * (xSpeed[i] + ySpeed[i] + zSpeed[i])/3
    '''


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

    file.write('swift.set_position(x=' + str(absX) + ', y=' + str(absY) + ', z=' + str(absZ) + ', speed=' + str(speed)+ ', wait=True)\n')


file.close()
#end
