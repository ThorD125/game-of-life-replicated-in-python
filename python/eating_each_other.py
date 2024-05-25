import random
from collections import Counter
import time

def show(grid):
    for row in grid:
        for col in row:
            print(f"{col} ", end="")
        print(f"")

def getLocation(x, y):
    if x < 0:
        x = 0
    if x >= size_x:
        x = size_x - 1
    if y < 0:
        y = 0
    if y >= size_y:
        y = size_y - 1
    return (x, y)

def getColorLocation(x, y):
    return gridarray[y][x]

# print(getLocation(17,11))
# print(neighbors)

def countInList(list):
    return Counter(list)

def getNeighbors(x, y):
    neighborList = []
    for dx, dy in neighbors:
        # print(f"dx: {x, dx}, dy: {y, dy}")
        nx, ny = getLocation(x + dx, y + dy)
        # print(nx, ny)
        # print(getColorLocation(nx, ny))
        if (nx, ny) != (x, y):
            neighborList.append(getColorLocation(nx, ny))
    return countInList(neighborList)
        
# print("locaiton: 5,4")
# print(getNeighbors(5,4).most_common(1)[0][0])

def createEvolveGrid(grid):
    newGrid = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            row.append(getNeighbors(x, y).most_common(1)[0][0])
        newGrid.append(row)
    return newGrid

def countGrid(grid):
    count = {}
    for char in chars:
        count[char] = 0
    for row in grid:
        for col in row:
            count[col] += 1
    return count

def checkCount(count):
    for x in count:
        # print(f"{x}: {count[x]}")
        if count[x] == (size_x * size_y):
            return False
    return True

def generateGrid(size_y, size_x, chars):
    gridarray = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            char = chars[random.randint(0, len(chars)-1)]
            row.append(char)
        gridarray.append(row)
    return gridarray

neighbors = (
    (-1, -1),  # Above left
    (-1, 0),  # Above
    (-1, 1),  # Above right
    (0, -1),  # Left
    (0, 1),  # Right
    (1, -1),  # Below left
    (1, 0),  # Below
    (1, 1),  # Below right
)

size_x = 50
size_y = 10
framesPerSecond = 30
chars = ["\033[31mr\033[0m", "\033[32mg\033[0m", "\033[33mb\033[0m", "\033[34my\033[0m", "\033[35mo\033[0m", "\033[36mp\033[0m", "\033[37mc\033[0m", "\033[30mm\033[0m"]

gridarray = generateGrid(size_y, size_x, chars)

show(gridarray)
count = countGrid(gridarray)

oldCounts = []
while checkCount(count):
    print("\033[H\033[J", end="")
    newgrid = createEvolveGrid(gridarray)
    show(newgrid)
    gridarray = newgrid
    newcount = countGrid(gridarray)
    if newcount in oldCounts:
        break
    oldCounts.append(newcount)
    oldCounts = oldCounts[-2:]
    count = newcount
    print(count)
    time.sleep(1 / framesPerSecond)

print("\033[H\033[J", end="")
show(gridarray)
print(count)

# https://realpython.com/conway-game-of-life-python/
