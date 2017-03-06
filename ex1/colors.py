from ev3dev import *

color_sensor = ev3.ColorSensor()
color_sensor.mode = 'COL-COLOR'

while True:
    print(color_sensor.value())
    motor = ev3.LargeMotor('outA')
    motor.run_timed(time_sp=3000, speed_sp=500)
    
    if color_sensor.value == 5:
        print 'OFF'
