import ROOT
import  pandas  as pd
import numpy as np 

# Lendo os arquivos
energia = "91.19GeV"
id_df = pd.read_csv("data/"+energia+"/id.dat",header=None)
event_df = pd.read_csv("data/"+energia+"/event.dat",header=None)
pT_df = pd.read_csv("data/"+energia+"/pT.dat",header=None)
px_df=pd.read_csv("data/"+energia+"/px.dat",header=None)
py_df=pd.read_csv("data/"+energia+"/py.dat",header=None)
pz_df=pd.read_csv("data/"+energia+"/pz.dat",header=None)
eta_df=pd.read_csv("data/"+energia+"/eta.dat",header=None)
phi_df=pd.read_csv("data/"+energia+"/phi.dat",header=None)
carregado_df=pd.read_csv("data/"+energia+"/carregado.dat",header=None)

# Transformando em array 
id_particula = np.array(id_df[0], dtype=int)
evento = np.array(event_df[0], dtype=int)
pT = np.array(pT_df[0], dtype=float)
px = np.array(px_df[0], dtype=float)
py = np.array(py_df[0], dtype=float)
pz = np.array(pz_df[0], dtype=float)
eta = np.array(eta_df[0], dtype=float)
phi = np.array(phi_df[0], dtype=float)
carregado = np.array(carregado_df[0],dtype=int)

#criando o TTree
output = ROOT.TFile("data/root/"+energia+"/data.root","RECREATE")
tree = ROOT.TTree("tree",'tree')
# criando as Branch
tree.Branch('id',id_particula,'id_particula/I')
tree.Branch('evento',evento,'evento/I')
tree.Branch('pT',pT,'pT/D')
tree.Branch('px',px,'px/D')
tree.Branch('py',py,'py/D')
tree.Branch('pz',pz,'pz/D')
tree.Branch('eta',eta,'eta/D')
tree.Branch('phi',phi,'phi/D')
tree.Branch('carregado',carregado,'carregado/I')
# preenchendo a ttree
for i in range(id_df.shape[0]):
    id_particula[0] = id_particula[i]
    evento[0]=evento[i]
    pT[0]=pT[i]
    px[0]=px[i]
    py[0]=py[i]
    pz[0]=pz[i]
    eta[0]=eta[i]
    phi[0]=phi[i]
    carregado[0]=carregado[i]
    tree.Fill()
    
output.Write()
output.Close()