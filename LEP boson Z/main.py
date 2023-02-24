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


n_event = 1000 # Numero de eventos 

pT_array = []
#loop event
for i in range(n_event):
    if not pythia.next(): continue
    #loop particle
    for particle in pythia.event:
        if particle.id() == 23: # Encontrando o boson Z 
            pT_array.append(particle.pT())
pythia.stat() # Estatistica

np.savetxt("Hist_pT.dat",pT_array,delimiter=',')
