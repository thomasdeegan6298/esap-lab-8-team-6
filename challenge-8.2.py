from sense_hat import SenseHat
from time import sleep
from PIL import Image
import numpy as np
#import scipy.io

def load_images(values, sense):
	## ##
		## Insert code here ##
	## ##

def clear_leds(sense):
	for x in range(0,7):
		for y in range(0,7):
			sense.set_pixels(x,y,0,0,0)

path_to_file = "Link to image file"

im = Image.open(path_to_file)
rgb_im=im.convert('RGB')
values=np.array(rgb_im)

sense=SenseHat()

clear_leds(sense)

load_image(values,sense)

sense.flip_v()
sense.set_rotation(270)
