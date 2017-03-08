import ev3dev.ev3 as ev3
from ev3dev.ev3 import *

def roulez_jeunesse():
    Sound.speak("Youpi !")
    moteur_large_gauche.run_forever()
    moteur_large_droit.run_forever()

def alte():
    Sound.speak("oh !")
    moteur_large_gauche.stop()=
    moteur_large_droit.stop()

moteur_large_gauche = LargeMotor('outB')
moteur_large_droit = LargeMotor('outC')

infrarouge = InfraredSensor()
infrarouge.mode('IR-PROX')

Sound.speak("ALLÉÉÉ !")
while True:
    roulez_jeunesse()
    distance = infrarouge.value()

    if distance <= 30:
        alte()
        break
