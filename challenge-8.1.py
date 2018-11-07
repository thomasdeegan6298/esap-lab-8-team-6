from sense_hat import SenseHat
from time import sleep

def clear_leds(sense)
	for x in range(0,7):
		for y in range(0,7):
			sense.set_pixels(x,y,0,0,0)

sense = SenseHat()
clear_leds(sense)

## Insert code HERE ##

## Commands for image

## Added code ends HERE ##

#sense.flip_v()
angle=0
while True:
	if angle>270:
		angle = 0
	sense.set_rotation(angle)
	sleep(1)
	angle+=90
