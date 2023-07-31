import sys
cfg = open("Makefile.inc")
lib = "home/gabriels3t/programa/pythia8/lib"
for line in cfg:
    if line.startswith("PREFIX_LIB="): lib = line[11:-1]; break
sys.path.insert(0, lib)


import pythia8 
import numpy as np

pythia = pythia8.Pythia()
pythia.readString("Beams:idA = 11") #eletron
pythia.readString("Beams:idB = -11") #positron
pythia.readString("Beams:eCM = 209") #Gev 
pythia.readString("HardQCD:all = on") # Utilizado para jet de altas energias 
pythia.readString("WeakSingleBoson:ffbar2gmZ = on") # produzir boson Z  
pythia.init() # Inicialização 


"""
pt, px, py, pz, pt, eta(rapidez), phi (ângulo azimutal)
"""

n_event = 1000 # Numero de eventos 
id =[];pT = [];px = [];py = [];pz = [];eta = [];phi = [];event=[]
#loop event
for i in range(n_event):
    if not pythia.next(): continue
    #loop particle
    for particle in pythia.event:
        if  particle.isFinal(): # particula estavel  
           event.append(i)
           id.append(particle.id())
           pT.append(particle.pT())
           px.append(particle.px())
           py.append(particle.py())
           pz.append(particle.pz())
           eta.append(particle.eta())
           phi.append(particle.phi())

np.savetxt("data/id.dat",id,delimiter=',')
np.savetxt("data/pT.dat",pT,delimiter=',')
np.savetxt("data/px.dat",px,delimiter=',')
np.savetxt("data/py.dat",py,delimiter=',')
np.savetxt("data/pz.dat",pz,delimiter=',')
np.savetxt("data/eta.dat",eta,delimiter=',')
np.savetxt("data/phi.dat",phi,delimiter=',')
np.savetxt("data/event.dat",event,delimiter=',')
