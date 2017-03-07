import ev3dev.ev3 as ev3
from ev3dev.ev3 import *

def roulez_jeunesse():
    Sound.speak("Youpi !")
    mL.run_forever()
    mR.run_forever()

def nah():
    Sound.speak("Nah !")
    mL.run_to_rel_pos(position_sp=45, speed_sp=360, stop_action="brake")
    mR.run_to_rel_pos(position_sp=-45, speed_sp=360, stop_action="brake")

def alte():
    Sound.speak("this is the end")
    mL.stop()
    mR.stop()

moteur_large_gauche = LargeMotor('outB')
moteur_large_droit = LargeMotor('outC')

infrarouge = InfraredSensor()
infra.mode('IR-PROX')
