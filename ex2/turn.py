import ev3dev.ev3 as ev3
from ev3dev.ev3 import *

def roulez_jeunesse():
    Sound.speak("Youpi !")
    moteur_large_gauche.run_forever()
    moteur_large_droit.run_forever()

def nah():
    Sound.speak("Nah !")
    moteur_large_gauche.run_to_rel_pos(position_sp=45, speed_sp=350, stop_action="brake")
    moteur_large_droit.run_to_rel_pos(position_sp=-45, speed_sp=350, stop_action="brake")

def alte():
    Sound.speak("oh !")
    moteur_large_gauche.stop()
    moteur_large_droit.stop()

moteur_large_gauche = LargeMotor('outB')
moteur_large_droit = LargeMotor('outC')

infrarouge = InfraredSensor()
infrarouge.mode('IR-PROX')


while True:
    Sound.speak("ALLÉÉÉ !")
    roulez_jeunesse()
    distance = infrarouge.value()

    if distance <= 30:
        alte()
        nah()
        roulez_jeunesse()
