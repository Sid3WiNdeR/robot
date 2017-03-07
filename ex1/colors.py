import ev3dev.ev3 as ev3
from ev3dev.ev3 import *



color_sensor = ev3.ColorSensor()
color_sensor.mode = 'COL-COLOR'

colors = ["What the fuck", "noir", "bluh", "ver", "zhaon", "alalalal", "blahn", "mahron"]

while True:
    print(colors[color_sensor.value()])


    if color_sensor.value() == 5:
        ev3.Sound.speak('oh revwar')
        pass

    else:
        print(colors[color_sensor.value()])
        Sound.speak(colors[color_sensor.value()]).wait()
