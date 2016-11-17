from microbit import *
import random

def createCells(n,m):
    cells = []
    for r in range(n):
        row = [False for c in range(m)]
        cells.append(row)
    return cells

def displayCells(cells):
    for row in range(len(cells)):
        for col in range(len(cells[row])):
            if cells[row][col]:
                display.set_pixel(col, row, 9)
            else:
                display.set_pixel(col, row, 0)
            
def randomInit(cells):
    for r in range(len(cells)):
        row = cells[r]
        for c in range(len(row)):
            cells[r][c] = random.choice([True, False])

def neighbours(cells, row, col):
    ''' count active neighbours with row and col index wrap around '''
    rows = len(cells)
    cols = len(cells[0])
    n = 0
    for r in range(row-1,row+2):
         ri = r % rows
         for c in range(col-1, col+2):
             ci = c % cols
             n += int(cells[ri][ci])
    return n - int(cells[row][col])
    
def nextState(cells, row, col):
    ''' calculate the next state of cell in row and col'''
    n = neighbours(cells, row, col) 
    alive = cells[row][col]
    if not alive and n == 3:
        return True
    if alive and 2 <= n <= 3:
        return True
    return False
    
def nextGeneration(c, n):
    ''' calculate the next generation of cells and return the number of cells that changed'''
    changes = 0
    for row in range(len(c)):
        for col in range(len(c[row])):
            n[row][col] = nextState(c, row, col)
            if n[row][col] != c[row][col]:
                changes += 1
    return changes

display.on()    
cur = createCells(5,5) # current generation of cells
nex = createCells(5,5) # next generation of cells

while True:
    randomInit(cur)
    displayCells(cur)
    sleep(1000)
    changes = 1
    while changes > 0:
        changes = nextGeneration(cur, nex)
        displayCells(nex)
        sleep(1000)
        nex, cur = (cur,nex) # swap current and next generation
    
    
