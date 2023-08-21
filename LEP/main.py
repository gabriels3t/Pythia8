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
pythia.readString("Beams:eCM = 91.19") #Gev  refazer com  91.19 gev (energia de cross section do bozon z
#pythia.readString("HardQCD:all = on") # Utilizado para jet de altas energias 1 bi > que z boson
pythia.readString("WeakSingleBoson:ffbar2gmZ = on") # produzir boson Z  
pythia.init() # Inicialização 


"""
pt, px, py, pz, pt, eta(rapidez), phi (ângulo azimutal)
"""

n_event = 10000 # Numero de eventos 
id =[];pT = [];px = [];py = [];pz = [];eta = [];phi = [];event=[];particle_name=[];carregada=[]
#loop event
for i in range(n_event):
    if not pythia.next(): continue

    contator_carregada =0
    #loop particle
    for particle in pythia.event:
        if  particle.isFinal(): # particula estavel  
           if particle.isCharged():
               contator_carregada +=1
           event.append(i)
           id.append(particle.id())
           pT.append(particle.pT())
           px.append(particle.px())
           py.append(particle.py())
           pz.append(particle.pz())
           eta.append(particle.eta())
           phi.append(particle.phi())
           particle_name.append([particle.name(),particle.id()])
           carregada.append(contator_carregada)

np.savetxt("data/91.19GeV/id.dat",id,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/pT.dat",pT,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/px.dat",px,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/py.dat",py,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/pz.dat",pz,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/eta.dat",eta,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/phi.dat",phi,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/event.dat",event,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/carregado.dat",carregada,delimiter=',',fmt='%.16f')
np.savetxt("data/91.19GeV/name_id_particle.dat",particle_name,delimiter=',', fmt='%s')
