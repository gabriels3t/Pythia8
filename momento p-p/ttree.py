import pandas as pd 
import ROOT 
import array

nome_arquivo = ['data/id.dat','data/massa.dat','data/momento.dat','data/px_momento.dat','data/py_momento.dat','data/pz_momento.dat','data/pT.dat','data/energia_cinetica.dat']
for i in range(len(nome_arquivo)):
    arquivo = open(nome_arquivo[i],'r+')
    arquivo.seek(0)
    arquivo.write("Arquivo" + '\n')
    arquivo.close()

id_df = pd.read_csv("data/id.dat")
massa_df = pd.read_csv("data/massa.dat")
momento_df=pd.read_csv("data/momento.dat")
px_df=pd.read_csv("data/px_momento.dat")
py_df=pd.read_csv("data/py_momento.dat")
pz_df=pd.read_csv("data/pz_momento.dat")
ener_cinetica_df= pd.read_csv("data/energia_cinetica.dat")
pT_df = pd.read_csv("data/pT.dat")



output = ROOT.TFile("root/dados.root",'RECREATE')
tree = ROOT.TTree("tree","tree")    

id_particula = array.array("i", map(int, id_df['Arquivo'].values.tolist()))
massa = array.array("d",massa_df['Arquivo'].array)
momento = array.array("d",momento_df['Arquivo'].array)
px = array.array("d",px_df['Arquivo'].array)
py = array.array("d",py_df['Arquivo'].array)
pz = array.array("d",pz_df['Arquivo'].array)
pT = array.array("d",pT_df['Arquivo'].array)
ener_cinetica = array.array("d",ener_cinetica_df['Arquivo'].array)

tree.Branch("id",id_particula,"id_particula/I")
tree.Branch("massa",massa,"massa/D")
tree.Branch("momento",momento,"momento/D")
tree.Branch("px",px,"px/D")
tree.Branch("py",py,"py/D")
tree.Branch("pz",pz,"pz/D")
tree.Branch("pT",pT,"pT/D")
tree.Branch("energia_cinetica",ener_cinetica,"ener_cinetica/D")

for i in range(len(id_df)):
    id_particula[0] = id_particula[i]
    massa[0] =massa[i]
    momento[0]=momento[i]
    px[0]=px[i]
    py[0]=py[i]
    pz[0]=pz[i]
    pT[0]=pT[i]
    ener_cinetica[0]=ener_cinetica[i]
    tree.Fill()

output.Write()
output.Close()
