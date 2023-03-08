#For converting pixel thresholding calc from ImageMagick:
#convert ~/Downloads/0f865be4c6b6330.gif -threshold 50% -depth 1 txt:
# ex: 
# 27,63: (255,255,255)  #FFFFFF  white
# 28,63: (255,255,255)  #FFFFFF  white
# 29,63: (255,255,255)  #FFFFFF  white
# 30,63: (0,0,0)  #000000  black
# 31,63: (0,0,0)  #000000  black
# 32,63: (0,0,0)  #000000  black

import pprint as pp
import re

input_set = open("pawpatrol_intro_pixels.txt", 'r').read().splitlines() 

matcher = re.compile('\(0')

#print(input_set)
px = []
for i in range(0,64):
    px.append(['.'] * 64)
for i in input_set:
    #print(i)
    vals = i.split(': ')
    coords = vals[0].split(',')
    pixel = ' '
    if re.match(matcher,vals[1]):
        pixel = '+'
    #print (coords)
    px[int(coords[1])][int(coords[0])] = pixel
for j in px:
    print ("b'" + ''.join(j) + "',")

