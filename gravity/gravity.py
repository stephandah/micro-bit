from microbit import *

x = 2
y = 2
while True:
    (ax,ay,az) = accelerometer.get_values()
    dx = ax / 500
    dy = ay / 500
    display.set_pixel(int(x), int(y), 0)
    x = x + dx
    if x < 0:
        x = 0
    if x > 4:
        x = 4
    y = y + dy
    if y < 0:
        y = 0
    if y > 4:
        y = 4
    display.set_pixel(int(x), int(y), 5)
    sleep(1000)
