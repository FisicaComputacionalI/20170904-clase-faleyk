import numpy as np
import matplotlib.pylab as pl
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y=[0,0,0,0,0,0,0,1,1,1,1,0,2,0,0,0,0,0,0,1,1,1]
pl.xlabel('anios de vida')
pl.ylabel('numero de novios y mascotas')
pl.plot(x,y,'ro')
pl.savefig ('temp03.png')
