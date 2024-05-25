import random
from collections import Counter
import time
import sys

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
    return grid_array[y][x]

def countInList(list):
    return Counter(list)

def getNeighbors(x, y):
    neighborList = []
    for dx, dy in neighbors:
        nx, ny = getLocation(x + dx, y + dy)
        if (nx, ny) != (x, y):
            neighborList.append(getColorLocation(nx, ny))
    return countInList(neighborList)
        
def createEvolveGrid(grid):
    new_Grid = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            row.append(getNeighbors(x, y).most_common(1)[0][0])
        new_Grid.append(row)
    return new_Grid

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
        if count[x] == (size_x * size_y):
            return False
    return True

def generateGrid(size_y, size_x, chars):
    grid_array = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            char = chars[random.randint(0, len(chars)-1)]
            row.append(char)
        grid_array.append(row)
    return grid_array

neighbors = (
    (-1, -1),  
    (-1, 0),  
    (-1, 1),  
    (0, -1),  
    (0, 1),  
    (1, -1),  
    (1, 0),  
    (1, 1),  
)

framesPerSecond = 30
chars = ["\033[31mr\033[0m", "\033[32mg\033[0m", "\033[33mb\033[0m", "\033[34my\033[0m", "\033[35mo\033[0m", "\033[36mp\033[0m", "\033[37mc\033[0m", "\033[30mm\033[0m"]

size_x = 50
size_y = 10

if len(sys.argv) > 1:
    size_x = int(sys.argv[1])
    size_y = int(sys.argv[2])

grid_array = generateGrid(size_y, size_x, chars)

show(grid_array)

oldCounts = []


print("\033[H\033[J", end="")
show(grid_array)



while True:
    print("\033[H\033[J", end="")
    new_grid = createEvolveGrid(grid_array)
    show(new_grid)
    grid_array = new_grid

    new_count = countGrid(grid_array)
    if new_count in oldCounts:
        break
    oldCounts.append(new_count)
    oldCounts = oldCounts[-2:]

    time.sleep(1 / framesPerSecond)
