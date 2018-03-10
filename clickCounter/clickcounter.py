from microbit import *
import os

FILE = 'counter.txt'

def readCounter():
    with open(FILE, 'rt') as file:
        content = file.read()
        return int(content)

def writeCounter(n):
    with open(FILE, 'wt') as file:
        file.write(str(n))
        
        
count = 0

files = os.listdir()
for file in files:
    if file == FILE:
         count = readCounter()
         
while True:
    if button_a.was_pressed():
        count += 1
        writeCounter(count)
    elif button_b.was_pressed():
        count = 0
        writeCounter(count)
    display.show(str(count))
        
    
display.clear()
