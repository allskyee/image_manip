#!/usr/bin/python

import Image
import sys
from struct import *
import array
 
if len(sys.argv) != 4:
        print "Usage:"
        print "yuv420_to_bmp.py <yuv file> <width> <height> "
        sys.exit(1) # exit
else:
        pass
 
image_name = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
y = array.array('B')
u = array.array('B')
v = array.array('B')
 
f = open(image_name, "rb")
 
image_out = Image.new("RGB", (width, height))
pix = image_out.load()
 
print width, height

# read luma channel
for i in range(0,height):
    for j in range(0, width):
        y.append(ord(f.read(1)));
 
# read  u
for i in range(0, height/2):
    for j in range(0, width/2):
        u.append(ord(f.read(1)));

# read  v
for i in range(0, height/2):
    for j in range(0, width/2):
        v.append(ord(f.read(1)));
 
for i in range(0,height):
    for j in range(0, width):
        Y_val = y[(i*width)+j]
        U_val = u[((i/2)*(width/2))+(j/2)]
        V_val = v[((i/2)*(width/2))+(j/2)]
        B = 1.164 * (Y_val-16) + 2.018 * (U_val - 128)
        G = 1.164 * (Y_val-16) - 0.813 * (V_val - 128) - 0.391 * (U_val - 128)
        R = 1.164 * (Y_val-16) + 1.596*(V_val - 128)
        pix[j, i] = int(R), int(G), int(B) 
 
image_out.save(image_name + ".bmp")
