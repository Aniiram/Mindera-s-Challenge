import json
import itertools

def compPairs(x,y):
    a = x[0]
    b = y[0]
    if x[0] == y[0]:
        a = x[1]
        b = y[1]
    return a-b

def checkAround(i,j):
    resC = []
    if i+1 < len(grid):
        if grid[i+1][j]:
            grid[i+1][j] = 0
            resC = resC + checkAround(i+1,j)
            resC.append([i+1,j])
    if i-1 > 0:
        if grid[i-1][j]:
            grid[i-1][j] = 0
            resC = resC + checkAround(i-1,j)
            resC.append([i-1,j])
    if j+1 < len(grid[i]):
        if grid[i][j+1]:
            grid[i][j+1] = 0
            resC = resC + checkAround(i,j+1)
            resC.append([i,j+1])
    if j-1 > 0:
        if grid[i][j-1]:
            grid[i][j-1] = 0
            resC = resC + checkAround(i,j-1)
            resC.append([i,j-1])
    return resC

def findAdjCells():
    i = 0
    for row in grid:
        j = 0
        for elem in row:
            resF = []
            if elem:
                elem = 0
                resF.append([i,j])
                resF = resF + checkAround(i,j)
                if len(resF) > 1:
                    print(sorted(list(resF for resF,_ in itertools.groupby(resF)), cmp = compPairs))

            j = j+1
        i = i+1    

print ("----------")
print ("File 5 X 8")
print ("----------")
with open("5X8.json", "r") as read_file:
    grid = json.load(read_file)
    findAdjCells()

##print ("--------------")
##print ("File 100 X 100")
##print ("--------------")
##with open("100x100.json", "r") as read_file:
##    grid = json.load(read_file)
##    findAdjCells()
##
##print ("----------------")
##print ("File 1000 X 1000")
##print ("----------------")
##with open("1000x1000.json", "r") as read_file:
##    grid = json.load(read_file)
##    findAdjCells()
##
##print ("------------------")
##print ("File 10000 X 10000")
##print ("------------------")
##with open("10000x10000.json", "r") as read_file:
##    grid = json.load(read_file)
##    findAdjCells()
##    
##print ("------------------")
##print ("File 20000 X 20000")
##print ("------------------")
##with open("20000x20000.json", "r") as read_file:
##    grid = json.load(read_file)
##    findAdjCells()
