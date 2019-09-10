from microbit import *

def wait_for_start():
    while True:
        if button_a.is_pressed():
            return

def display_time():
    return button_b.is_pressed()
    
def show_pixels(n):
    display.clear()
    for i in range(n):
        x = i % 5
        y = i // 5
        display.set_pixel(x, y, 8)

def reset_detected():
    return accelerometer.is_gesture('shake')

def blink_display():
    for i in range(10):
        display.show(Image.CHESSBOARD)
        sleep(1000)
        display.clear()
        sleep(1000)

# main
secs_to_work = 25 * 60 

while True:
    secs = 0
    display.scroll("start")
    wait_for_start()
    while secs < secs_to_work:
        if display_time():
            show_pixels(secs // 60)
        else:
            show_pixels(0)
        if reset_detected():
            break
        sleep(1000)
        secs += 1
    else:
        blink_display()
