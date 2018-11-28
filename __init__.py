import math
from test.test_importlib.data02 import one

# open the file
inputFile = open("minterms", "r")

# create a 2D minterm array
minterm = [[0 for i in range(4)] for j in range(26)]
spares =  [[0 for i in range(4)] for j in range(26)]
spareCount = 0
a = [0, 0, 0, 0]

# count the number of minterms in the file
x = sum(1 for line in open('minterms'))

# create an array of minterms from the file and remove the \n character
fileLine = inputFile.readlines()
fileLine = [line.rstrip('\n') for line in open('minterms')]

inputFile.close()

# place the contents from the fileLine array into a 2D array
count = 0
while count < x:
    a[0:3] = map(int, str(fileLine[count]))
    minterm[count][0] = a[0]
    minterm[count][1] = a[1]
    minterm[count][2] = a[2]
    minterm[count][3] = a[3]
    count = count + 1
    
# create a new truth table that sorts the minterms by how many 1's they have
unsorted = (x / 2) + 1
j = 0
temp = [0, 0, 0, 0]
while j < unsorted:
    i = 0
    while i < x - 1: 
        if minterm[i].count(1) > minterm[i + 1].count(1):
            temp = minterm[i]
            minterm[i] = minterm[i + 1]
            minterm[i + 1] = temp 
        i = i + 1
    j = j + 1  
   
# Make multiple arrays for the numbers of ones
i = 0
zeroCount = 0
oneCount = 0
twoCount = 0
threeCount = 0
fourCount = 0
while i < x:   
    if minterm[i].count(1) == 0:
        zeroCount = zeroCount + 1 
    elif minterm[i].count(1) == 1:
        oneCount = oneCount + 1
    elif minterm[i].count(1) == 2:
        twoCount = twoCount + 1
    elif minterm[i].count(1) == 3:
        threeCount = threeCount + 1
    elif minterm[i].count(1) == 4:
        fourCount = fourCount + 1
    i = i + 1

zero = [[0 for i in range(4)] for j in range(zeroCount)]
one = [[0 for i in range(4)] for j in range(oneCount)]
two = [[0 for i in range(4)] for j in range(twoCount)]
three = [[0 for i in range(4)] for j in range(threeCount)]
four = [[0 for i in range(4)] for j in range(fourCount)]

i = 0
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0

# Make five arrays, one for each number of ones (0,1,2,3,4)
while i < x:    
    if minterm[i].count(1) == 0:
        zero[c0][0] = minterm[i][0]
        zero[c0][1] = minterm[i][1]
        zero[c0][2] = minterm[i][2]
        zero[c0][3] = minterm[i][3]
        c0 = c0 + 1
    elif minterm[i].count(1) == 1:
        one[c1][0] = minterm[i][0]
        one[c1][1] = minterm[i][1]
        one[c1][2] = minterm[i][2]
        one[c1][3] = minterm[i][3]
        c1 = c1 + 1
    elif minterm[i].count(1) == 2:
        two[c2][0] = minterm[i][0]
        two[c2][1] = minterm[i][1]
        two[c2][2] = minterm[i][2]
        two[c2][3] = minterm[i][3]
        c2 = c2 + 1
    elif minterm[i].count(1) == 3:
        three[c3][0] = minterm[i][0]
        three[c3][1] = minterm[i][1]
        three[c3][2] = minterm[i][2]
        three[c3][3] = minterm[i][3]
        c3 = c3 + 1
    else:
        four[c4][0] = minterm[i][0]
        four[c4][1] = minterm[i][1]
        four[c4][2] = minterm[i][2]
        four[c4][3] = minterm[i][3]
        c4 = c4 + 1
    i = i + 1
    
# Step 1
# group minterms that are only one term different replacing it with a -
# Compare the zero array with the ones array
zeroGroup = [[0 for i in range(4)] for j in range(c0*c1)]
oneSpares = [[0 for i in range(4)] for j in range(oneCount)]
spareOneCount = 0
k = 0
zG = 0
simC = 0
while(k < c0):
    i = 0
    everZero = oneCount
    while (i < c1):
        simC = 0
        if (zero[k][0] == one[i][0]):
            simC = simC + 1
        if(zero[k][1] == one[i][1]):
            simC = simC + 1
        if(zero[k][2] == one[i][2]):
            simC = simC + 1
        if(zero[k][3] == one[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(one[i][j] == zero[k][j]):
                    zeroGroup[zG][j] = zero[k][j]
                elif(one[i][j] != zero[k][j]):
                    zeroGroup[zG][j] = "-"
                j = j + 1
            zG = zG + 1
        else:
            everZero = everZero - 1
        i = i + 1
    if(everZero == 0):
        spares[spareCount] = zero[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the zero to one counter
k = 0
while(k < oneCount):
    i = 0
    everOne = zeroCount
    while (i < zeroCount):
        simC = 0
        if(one[k][0] == zero[i][0]):
            simC = simC + 1
        if(one[k][1] == zero[i][1]):
            simC = simC + 1
        if(one[k][2] == zero[i][2]):
            simC = simC + 1
        if(one[k][3] == zero[i][3]):
            simC = simC + 1
        if(simC != 3):
            everOne = everOne - 1
        i = i + 1
    if(everOne == 0):
        oneSpares[spareOneCount] = one[k]
        spareOneCount = spareOneCount + 1
    k = k + 1
# Compare the one array with the twos array 
oneGroup = [[0 for i in range(4)] for j in range(c2*c1)]
twoSpares = [[0 for i in range(4)] for j in range(c2)]
spareTwoCount = 0
k = 0
oG = 0
simC = 0
while(k < c1):
    i = 0
    everOne = c2
    while (i < c2):
        simC = 0
        if(one[k][0] == two[i][0]):
            simC = simC + 1
        if(one[k][1] == two[i][1]):
            simC = simC + 1
        if(one[k][2] == two[i][2]):
            simC = simC + 1
        if(one[k][3] == two[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(two[i][j] == one[k][j]):
                    oneGroup[oG][j] = one[k][j]
                elif(two[i][j] != one[k][j]):
                    oneGroup[oG][j] = "-"
                j = j + 1
            oG = oG + 1
        else:
            everOne = everOne - 1
        i = i + 1
    if((everOne == 0) & (oneSpares.count(one[k]) > 0)):
        spares[spareCount] = one[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the one to two counter
k = 0
while(k < c2):
    i = 0
    everTwo = c1
    while (i < c1):
        simC = 0
        if(two[k][0] == one[i][0]):
            simC = simC + 1
        if(two[k][1] == one[i][1]):
            simC = simC + 1
        if(two[k][2] == one[i][2]):
            simC = simC + 1
        if(two[k][3] == one[i][3]):
            simC = simC + 1
        if(simC != 3):
            everTwo = everTwo - 1
        i = i + 1
    if(everTwo == 0):
        twoSpares[spareTwoCount] = two[k]
        spareTwoCount = spareTwoCount + 1
    k = k + 1 
# Compare the two array with the three array 
twoGroup = [[0 for i in range(4)] for j in range(c3*c2)]
threeSpares = [[0 for i in range(4)] for j in range(c3)]
spareThreeCount = 0
k = 0
twoG = 0
simC = 0
while(k < c2):
    i = 0
    everTwo = c3
    while (i < c3):
        simC = 0
        if (two[k][0] == three[i][0]):
            simC = simC + 1
        if(two[k][1] == three[i][1]):
            simC = simC + 1
        if(two[k][2] == three[i][2]):
            simC = simC + 1
        if(two[k][3] == three[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(three[i][j] == two[k][j]):
                    twoGroup[twoG][j] = two[k][j]
                elif(three[i][j] != two[k][j]):
                    twoGroup[twoG][j] = "-"
                j = j + 1
            twoG = twoG + 1
        else:
            everTwo = everTwo - 1
        i = i + 1
    if((everTwo == 0) & (twoSpares.count(two[k]) > 0)):
        spares[spareCount] = two[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the two to three counter
k = 0
while(k < c3):
    i = 0
    everThree = c2
    while (i < c2):
        simC = 0
        if(three[k][0] == two[i][0]):
            simC = simC + 1
        if(three[k][1] == two[i][1]):
            simC = simC + 1
        if(three[k][2] == two[i][2]):
            simC = simC + 1
        if(three[k][3] == two[i][3]):
            simC = simC + 1
        if(simC != 3):
            everThree = everThree - 1
        i = i + 1
    if(everThree == 0):
        threeSpares[spareThreeCount] = three[k]
        spareThreeCount = spareThreeCount + 1
    k = k + 1 
# Compare the three array with the four array 
threeGroup = [[0 for i in range(4)] for j in range(c4*c3)]
k = 0
threeG = 0
simC = 0
while(k < c3):
    i = 0
    everThree = c4
    while (i < c4):
        simC = 0
        if (three[k][0] == four[i][0]):
            simC = simC + 1
        if(three[k][1] == four[i][1]):
            simC = simC + 1
        if(three[k][2] == four[i][2]):
            simC = simC + 1
        if(three[k][3] == four[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(four[i][j] == three[k][j]):
                    threeGroup[threeG][j] = three[k][j]
                elif(four[i][j] != three[k][j]):
                    threeGroup[threeG][j] = "-"
                j = j + 1
            threeG = threeG + 1
        else:
            everThree = everThree - 1
        i = i + 1 
    if((everThree == 0) & (threeSpares.count(three[k]) > 0)):
        spares[spareCount] = threeGroup[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the three and four counter
k = 0
while(k < c4):
    i = 0
    everFour = c3
    while (i < c3):
        simC = 0
        if(four[k][0] == three[i][0]):
            simC = simC + 1
        if(four[k][1] == three[i][1]):
            simC = simC + 1
        if(four[k][2] == three[i][2]):
            simC = simC + 1
        if(four[k][3] == three[i][3]):
            simC = simC + 1
        if(simC != 3):
            everFour = everFour - 1
        i = i + 1
    if(everFour == 0):
        spares[spareCount] = four[k]
        spareCount = spareCount + 1
    k = k + 1
    
# Remove extra rows
i = 0
while(i < len(zeroGroup)):
    if(zeroGroup[i] == [0,0,0,0]):
        break
    i = i + 1
zeroGroup = zeroGroup[0:i]
i = 0
while(i < len(oneGroup)):
    if(oneGroup[i] == [0,0,0,0]):
        break
    i = i + 1
oneGroup = oneGroup[0:i]
i = 0
while(i < len(twoGroup)):
    if(twoGroup[i] == [0,0,0,0]):
        break
    i = i + 1
twoGroup = twoGroup[0:i]
i = 0
while(i < len(threeGroup)):
    if(threeGroup[i] == [0,0,0,0]):
        break
    i = i + 1
threeGroup = threeGroup[0:i]
#Step 2
# group minterms that are only one term different replacing it with a -
# Compare the zero array with the ones array
zeroGroupTwo = [[0 for i in range(4)] for j in range(len(zeroGroup)*len(oneGroup))]
oneSpares = [[0 for i in range(4)] for j in range(oG)]
spareOneCount = 0
k = 0
zGTwo = 0
simC = 0
while(k < zG):
    i = 0
    everZero = oG
    while (i < oG):
        simC = 0
        if(zeroGroup[k][0] == oneGroup[i][0]):
            simC = simC + 1
        if(zeroGroup[k][1] == oneGroup[i][1]):
            simC = simC + 1
        if(zeroGroup[k][2] == oneGroup[i][2]):
            simC = simC + 1
        if(zeroGroup[k][3] == oneGroup[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(oneGroup[i][j] == zeroGroup[k][j]):
                    zeroGroupTwo[zGTwo][j] = zeroGroup[k][j]
                elif(oneGroup[i][j] != zeroGroup[k][j]):
                    zeroGroupTwo[zGTwo][j] = "-"
                j = j + 1
            zGTwo = zGTwo + 1
        else:
            everZero = everZero - 1
        i = i + 1
    if(everZero == 0):
        spares[spareCount] = zeroGroup[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the zero to one counter
k = 0
while(k < oG):
    i = 0
    everOne = zG
    while (i < zG):
        simC = 0
        if(oneGroup[k][0] == zeroGroup[i][0]):
            simC = simC + 1
        if(oneGroup[k][1] == zeroGroup[i][1]):
            simC = simC + 1
        if(oneGroup[k][2] == zeroGroup[i][2]):
            simC = simC + 1
        if(oneGroup[k][3] == zeroGroup[i][3]):
            simC = simC + 1
        if(simC != 3):
            everOne = everOne - 1
        i = i + 1
    if(everOne == 0):
        oneSpares[spareOneCount] = oneGroup[k]
        spareOneCount = spareOneCount + 1
    k = k + 1
# Compare the one array with the twos array 
oneGroupTwo = [[0 for i in range(4)] for j in range(twoG * oG)]
twoSpares = [[0 for i in range(4)] for j in range(twoG)]
spareTwoCount = 0
k = 0
oGTwo = 0
simC = 0
while(k < oG):
    i = 0
    everOne = twoG
    while (i < twoG):
        simC = 0
        if(oneGroup[k][0] == twoGroup[i][0]):
            simC = simC + 1
        if(oneGroup[k][1] == twoGroup[i][1]):
            simC = simC + 1
        if(oneGroup[k][2] == twoGroup[i][2]):
            simC = simC + 1
        if(oneGroup[k][3] == twoGroup[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(twoGroup[i][j] == oneGroup[k][j]):
                    oneGroupTwo[oGTwo][j] = oneGroup[k][j]
                elif(twoGroup[i][j] != oneGroup[k][j]):
                    oneGroupTwo[oGTwo][j] = "-"
                j = j + 1
            oGTwo = oGTwo + 1
        else:
            everOne = everOne - 1
        i = i + 1
    if((everOne == 0) & (oneSpares.count(oneGroup[k]) > 0)):
        spares[spareCount] = oneGroup[k]
        spareCount = spareCount + 1
    k = k + 1  
# flip the one to two counter
k = 0
while(k < twoG):
    i = 0
    everTwo = oG
    while (i < oG):
        simC = 0
        if(twoGroup[k][0] == oneGroup[i][0]):
            simC = simC + 1
        if(twoGroup[k][1] == oneGroup[i][1]):
            simC = simC + 1
        if(twoGroup[k][2] == oneGroup[i][2]):
            simC = simC + 1
        if(twoGroup[k][3] == oneGroup[i][3]):
            simC = simC + 1
        if(simC != 3):
            everTwo = everTwo - 1
        i = i + 1
    if(everTwo == 0):
        twoSpares[spareTwoCount] = twoGroup[k]
        spareTwoCount = spareTwoCount + 1
    k = k + 1
# Compare the two array with the three array 
twoGroupTwo = [[0 for i in range(4)] for j in range(threeG * twoG)]
k = 0
twoGTwo = 0
simC = 0
while(k < twoG):
    i = 0
    everTwo = threeG
    while (i < threeG):
        simC = 0
        if (twoGroup[k][0] == threeGroup[i][0]):
            simC = simC + 1
        if(twoGroup[k][1] == threeGroup[i][1]):
            simC = simC + 1
        if(twoGroup[k][2] == threeGroup[i][2]):
            simC = simC + 1
        if(twoGroup[k][3] == threeGroup[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(threeGroup[i][j] == twoGroup[k][j]):
                    twoGroupTwo[twoGTwo][j] = twoGroup[k][j]
                elif(threeGroup[i][j] != twoGroup[k][j]):
                    twoGroupTwo[twoGTwo][j] = "-"
                j = j + 1
            twoGTwo = twoGTwo + 1
        else:
            everTwo = everTwo - 1
        i = i + 1 
    if((everTwo == 0) & (twoSpares.count(twoGroup[k]) > 0)):
        spares[spareCount] = twoGroup[k]
        spareCount = spareCount + 1
    k = k + 1   
# flip the two to three counter
k = 0
while(k < threeG):
    i = 0
    everThree = twoG
    while (i < twoG):
        simC = 0
        if(threeGroup[k][0] == twoGroup[i][0]):
            simC = simC + 1
        if(threeGroup[k][1] == twoGroup[i][1]):
            simC = simC + 1
        if(threeGroup[k][2] == twoGroup[i][2]):
            simC = simC + 1
        if(threeGroup[k][3] == twoGroup[i][3]):
            simC = simC + 1
        if(simC != 3):
            everThree = everThree - 1
        i = i + 1
    if(everThree == 0):
        spares[spareCount] = threeGroup[k]
        spareCount = spareCount + 1
    k = k + 1
   
#Step 3
# group minterms that are only one term different replacing it with a -
# Compare the zero array with the ones array
zeroGroupThree = [[0 for i in range(4)] for j in range(oGTwo*zGTwo)]
oneSpares = [[0 for i in range(4)] for j in range(oGTwo)]
spareOneCount = 0
k = 0
zGThree = 0
simC = 0
while(k < zGTwo):
    i = 0
    everZero = oGTwo
    while (i < oGTwo):
        simC = 0
        if(zeroGroupTwo[k][0] == oneGroupTwo[i][0]):
            simC = simC + 1
        if(zeroGroupTwo[k][1] == oneGroupTwo[i][1]):
            simC = simC + 1
        if(zeroGroupTwo[k][2] == oneGroupTwo[i][2]):
            simC = simC + 1
        if(zeroGroupTwo[k][3] == oneGroupTwo[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(oneGroupTwo[i][j] == zeroGroupTwo[k][j]):
                    zeroGroupThree[zGThree][j] = zeroGroupTwo[k][j]
                elif(oneGroupTwo[i][j] != zeroGroupTwo[k][j]):
                    zeroGroupThree[zGThree][j] = "-"
                j = j + 1
            zGThree = zGThree + 1
        else:
            everZero = everZero - 1
        i = i + 1
    if(everZero == 0):
        spares[spareCount] = zeroGroupTwo[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the zero to one counter
k = 0
while(k < oGTwo):
    i = 0
    everOne = zGTwo
    while (i < zGTwo):
        simC = 0
        if(oneGroupTwo[k][0] == zeroGroupTwo[i][0]):
            simC = simC + 1
        if(oneGroupTwo[k][1] == zeroGroupTwo[i][1]):
            simC = simC + 1
        if(oneGroupTwo[k][2] == zeroGroupTwo[i][2]):
            simC = simC + 1
        if(oneGroupTwo[k][3] == zeroGroupTwo[i][3]):
            simC = simC + 1
        if(simC != 3):
            everOne = everOne - 1
        i = i + 1
    if(everOne == 0):
        oneSpares[spareOneCount] = oneGroupTwo[k]
        spareOneCount = spareOneCount + 1
    k = k + 1
# Compare the one array with the twos array 
oneGroupThree = [[0 for i in range(4)] for j in range(twoGTwo * oGTwo)]
twoSpares = [[0 for i in range(4)] for j in range(twoGTwo)]
spareTwoCount = 0
k = 0
oGThree = 0
simC = 0
while(k < oGTwo):
    i = 0
    everOne = twoGTwo
    while (i < twoGTwo):
        simC = 0
        if(oneGroupTwo[k][0] == twoGroupTwo[i][0]):
            simC = simC + 1
        if(oneGroupTwo[k][1] == twoGroupTwo[i][1]):
            simC = simC + 1
        if(oneGroupTwo[k][2] == twoGroupTwo[i][2]):
            simC = simC + 1
        if(oneGroupTwo[k][3] == twoGroupTwo[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(twoGroupTwo[i][j] == oneGroupTwo[k][j]):
                    oneGroupThree[oGThree][j] = oneGroupTwo[k][j]
                elif(twoGroupTwo[i][j] != oneGroupTwo[k][j]):
                    oneGroupThree[oGThree][j] = "-"
                j = j + 1
            oGThree = oGThree + 1
        else:
            everOne = everOne - 1
        i = i + 1
    if((everOne == 0) & (oneSpares.count(oneGroupTwo[k]) > 0)):
        spares[spareCount] = oneGroupTwo[k]
        spareCount = spareCount + 1
    k = k + 1  
# flip the one to two counter
k = 0
while(k < twoGTwo):
    i = 0
    everTwo = oGTwo
    while (i < oGTwo):
        simC = 0
        if(twoGroupTwo[k][0] == oneGroupTwo[i][0]):
            simC = simC + 1
        if(twoGroupTwo[k][1] == oneGroupTwo[i][1]):
            simC = simC + 1
        if(twoGroupTwo[k][2] == oneGroupTwo[i][2]):
            simC = simC + 1
        if(twoGroupTwo[k][3] == oneGroupTwo[i][3]):
            simC = simC + 1
        if(simC != 3):
            everTwo = everTwo - 1
        i = i + 1
    if(everTwo == 0):
        twoSpares[spareTwoCount] = twoGroupTwo[k]
        spareTwoCount = spareTwoCount + 1
    k = k + 1

#Step 4
# group minterms that are only one term different replacing it with a -
# Compare the zero array with the ones array
zeroGroupFour = [[0 for i in range(4)] for j in range(len(zeroGroupThree)*len(oneGroupThree))]
oneSpares = [[0 for i in range(4)] for j in range(oGThree)]
spareOneCount = 0
k = 0
zGFour = 0
simC = 0
while(k < zGThree):
    i = 0
    everZero = oGThree
    while (i < oGThree):
        simC = 0
        if(zeroGroupThree[k][0] == oneGroupThree[i][0]):
            simC = simC + 1
        if(zeroGroupThree[k][1] == oneGroupThree[i][1]):
            simC = simC + 1
        if(zeroGroupThree[k][2] == oneGroupThree[i][2]):
            simC = simC + 1
        if(zeroGroupThree[k][3] == oneGroupThree[i][3]):
            simC = simC + 1
        if(simC == 3):
            j = 0
            while(j < 4):
                if(oneGroupThree[i][j] == zeroGroupThree[k][j]):
                    zeroGroupFour[zGFour][j] = zeroGroupThree[k][j]
                elif(oneGroupThree[i][j] != zeroGroupThree[k][j]):
                    zeroGroupFour[zGFour][j] = "-"
                j = j + 1
            zGFour = zGFour + 1
        else:
            everZero = everZero - 1
        i = i + 1
    if(everZero == 0):
        spares[spareCount] = zeroGroupThree[k]
        spareCount = spareCount + 1
    k = k + 1
# flip the zero to one counter
k = 0
while(k < oGThree):
    i = 0
    everOne = zGThree
    while (i < zGThree):
        simC = 0
        if(oneGroupThree[k][0] == zeroGroupThree[i][0]):
            simC = simC + 1
        if(oneGroupThree[k][1] == zeroGroupThree[i][1]):
            simC = simC + 1
        if(oneGroupThree[k][2] == zeroGroupThree[i][2]):
            simC = simC + 1
        if(oneGroupThree[k][3] == zeroGroupThree[i][3]):
            simC = simC + 1
        if(simC != 3):
            everOne = everOne - 1
        i = i + 1
    if(everOne == 0):
        oneSpares[spareOneCount] = oneGroupThree[k]
        spareOneCount = spareOneCount + 1
    k = k + 1 
    
spares = spares[0:spareCount]
# Remove extra rows
i = 1
while(i < len(zeroGroupFour)):
    if(zeroGroupFour[i] == [0,0,0,0]):
        break
    i = i + 1
finalZero = [[0 for i in range(4)] for j in range(i)]
finalZero = zeroGroupFour[0:i]
i = 0
i = 0
size = len(finalZero) + len(spares)
semifinal = [[0 for i in range(4)] for j in range(size)]
sspare = 0
while(i < len(finalZero)):
    semifinal[i] = finalZero[i]
    i = i + 1
while(sspare < len(spares)):
    semifinal[i] = spares[sspare]
    i = i + 1
    sspare = sspare + 1   
size = len(semifinal)
time = 0
i = 0    
j = 0
que = False
while (i < size):
    que = False
    j = 0
    while(j < size):
        if((i > j) & (semifinal[i] == semifinal[j])):
            que = True
        j = j + 1
    if(que == False):
        time = time + 1
    i = i + 1
final = [[0 for i in range(4)] for j in range(time)]
i = 0
j = 0
count = 0
que = False
while (i < size):
    que = False
    j = 0
    while(j < size):
        if((i > j) & (semifinal[i] == semifinal[j])):
            que = True
        j = j + 1
    if(que == False):
        final[count] = semifinal[i]
        count = count+1
    i = i + 1
# write final expression to a file
outputFile = open("expression.txt", "a") 
outputFile = open("expression.txt","w")
i = 0
while i < time:
    outputFile.write(str(final[i]))
    outputFile.write('\n')
    i = i + 1
outputFile.close() 