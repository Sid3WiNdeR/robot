import ev3dev.ev3 as *
import time


for ammo in range(0,3):
    moteur_pas_large = ev3.MediumMotor('outC')
    moteur_pas_large.run_to_rel_pos(position_sp=1080, speed_sp=700)
    time.sleep(3)
