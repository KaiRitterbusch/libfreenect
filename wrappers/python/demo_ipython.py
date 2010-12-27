#!/usr/bin/env python
from freenect import sync_get_depth, sync_get_video
import cv  
import numpy as np
  
def doloop():
    global depth, rgb
    while True:
        # Get a fresh frame
        (depth,_), (rgb,_) = sync_get_depth(), sync_get_video()
	# Down sample 11 to 8 bits
        depth >>=(11-8)
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        da = np.hstack((d3,rgb))
        
        # Simple Downsample
        cv.ShowImage('both',np.array(da[::2,::2,::-1]))
        if cv.WaitKey(5) == 27 : break
    freenect.sync_stop()
        
doloop()

"""
IPython usage:
 ipython
 [1]: run -i demo_freenect
 #<ctrl -c>  (to interrupt the loop)
 [2]: %timeit -n100 sync_get_depth(), sync_get_rgb() # profile the kinect capture

"""

