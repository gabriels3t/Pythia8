import sys
cfg = open("Makefile.inc")
lib = "home/gabriels3t/programa/pythia8/lib"
for line in cfg:
    if line.startswith("PREFIX_LIB="): lib = line[11:-1]; break
sys.path.insert(0, lib)

import pythia8

# Configuração da geração de eventos
pythia = pythia8.Pythia()
pythia.readString("Top:gg2ttbar = on") # gera eventos ttbar
pythia.init()

# Loop de geração de eventos
for iEvent in range(10):
    pythia.next()
    event_number = pythia.info.event()
    print(f"Número do evento atual: {event_number}")
    
    # Aqui você pode fazer outras operações com as partículas geradas no evento
    particles = pythia.event

pythia.stat()
