#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David Harris"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["David Harris"]
__license__ = "GPL"
__version__ = "1.7.1"
__status__ = "Production"

import time
import picamera
import os
import imageio



camera = picamera.PiCamera()
camera.resolution=(1920, 1080)

#Loop for an hour
t_end = time.time() + 60*60
while time.time() < t_end:
  try:
    print '1'
    camera.start_preview()
    #start the preview then give it time to focus and adjust to light
    time.sleep(5)
    ts=time.strftime("%Y-%m-%d-%H%M%S", time.gmtime())
    camera.capture('img-'+ts+'.jpg')
    print '2'
    time.sleep(25)

  except KeyboardInterrupt:
    camera.stop_preview()
    sys.exit()

ts=time.strftime("%Y-%m-%d-%H%M%S", time.gmtime())

#V2 use imageio to compile into a gif

filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
f=0


with imageio.get_writer(ts+'_Movie.gif', mode='I') as writer:
	for filename in filenames:
		image = imageio.imread(filename)
		writer.append_data(image)
		print 'Added File: ' + str(f)
		f+=1
