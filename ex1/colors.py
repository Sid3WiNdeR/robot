from ev3dev.ev3 import *

ev3.Sound.setLanguage("French")

color_sensor = ev3.ColorSensor()
color_sensor.mode = 'COL-COLOR'

colors = ["What the fuck", "noir", "bleu", "vert", "jaune", "alalalal", "blanc", "marron"]

while True:
    print(color_sensor.value())
    #motor = ev3.LargeMotor('outA')
    #motor.run_timed(time_sp=3000, speed_sp=500)

    if color_sensor.value == 5:
        ev3.Sound.speak('Au Revoir')

    else:
        print(colors[cl.value()])
        Sound.speak(colors[cl.value()])
