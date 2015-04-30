#!/usr/bin/env python

Vf  = 1.2 #V
If  = 0.001 #A
Vcc = 5.0 #V
print("Optocoupler resistors: {} Ohms".format((Vcc-Vf)/If))

# output alum bypass is estimated for 10us@12A
