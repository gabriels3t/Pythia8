import sys
cfg = open("Makefile.inc")
lib = "home/gabriels3t/programa/pythia8/lib"
for line in cfg:
    if line.startswith("PREFIX_LIB="): lib = line[11:-1]; break
sys.path.insert(0, lib)


import pythia8
import math
import numpy as np

pythia = pythia8.Pythia()
pythia.readFile("macro.cmnd") #Ler macro

nEvents = 1000
pythia.init()

# Criar dados
massa_array = []
id_array = []
px_array= []
py_array= []
pz_array= []
momento_array = []
ener_cinetica_array = []
pT_array=[]


#event Loop 
for i in range(nEvents):
    if not pythia.next(): continue
    #particle loop 
    px=py=pz = momento = 0

    for particle in pythia.event:
        id_array.append(particle.id())
        #Massa 
        massa_array.append(particle.m())
        #Momento para cada eixo
        px = particle.px()
        py = particle.py()
        pz = particle.pz()
        momento = math.sqrt(px**2+py**2+pz**2)
        px_array.append(px)
        py_array.append(py)
        pz_array.append(pz)
        momento_array.append(momento)
        pT_array.append(particle.pT())
        ener_cinetica_array.append(particle.e())
      
pythia.stat() # Estatistica do evento

np.savetxt("data/massa.dat",massa_array,delimiter=',')
np.savetxt("data/id.dat",id_array,delimiter=',')
np.savetxt("data/px_momento.dat",px_array,delimiter=',')
np.savetxt("data/py_momento.dat",py_array,delimiter=',')
np.savetxt("data/pz_momento.dat",pz_array,delimiter=',')
np.savetxt("data/momento.dat",momento_array,delimiter=',')
np.savetxt("data/pT.dat",pT_array,delimiter=',')
np.savetxt("data/energia_cinetica.dat",ener_cinetica_array,delimiter=',')
