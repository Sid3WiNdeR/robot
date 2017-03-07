#!/usr/bin/env python3

from ev3dev.ev3 import *
import time


ir = ev3.InfraredSensor()
ir.mode = 'IR-PROX'

print(ir.value())
