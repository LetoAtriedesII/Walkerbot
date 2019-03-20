#this code is designed to parse data from a csv file and
#create motion commands for the robot

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

with open('bnj_walk.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        xPos.append(int(row[1]))
        yPos.append(int(row[2]))
        zPos.append(int(row[3]))
        xSpeed.append(int(row[4]))
        ySpeed.append(int(row[5]))
        zSpeed.append(int(row[6]))

for i in range(0, len(xPos)):
    xDist.append(xPos[i] - xPos[i+1])
    yDist.append(yPos[i] - yPos[i+1])
    zDist.append(zPos[i] - zPos[i+1])
    print('swift.set_polar(stretch=' + str(xDist[i]) + ', rotation=' + str(zDist[i]) + ', height=' + str(zDist[i]) + ', speed=' + str(xSpeed[i]) + ', wait=True)')



#end
