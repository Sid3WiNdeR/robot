from ev3dev import *

color_sensor = ev3.ColorSensor()
color_sensor.mode = 'COL-COLOR'

while True:
    print(color_sensor.value())
    if color_sensor.value == 5:
        print 'OFF'
