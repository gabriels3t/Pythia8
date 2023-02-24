import sys
import pandas as pd 
import ROOT 

def montar(nome_arquivo,titulo='titulo',eixox='X',eixoy='Y',bins=100,intervaloa=-10,intervalob=10):
    arquivo = open(nome_arquivo,'r+')
    arquivo.seek(0)
    arquivo.write("Arquivo" + '\n')
    arquivo.close()

    df = pd.read_csv(nome_arquivo)

    hist = ROOT.TH1F('hist',titulo,bins,intervaloa,intervalob)
    for i in range(df.shape[0]):
        hist.Fill(df['Arquivo'][i])

    hist.GetYaxis().SetTitle(eixoy) # Eixo X
    hist.GetXaxis().SetTitle(eixox) # Eixo Y
    c = ROOT.TCanvas("","",800,600)

    hist.Draw()
    #c.Draw()
    n = 'grafico'+nome_arquivo[:-4]
    c.SaveAs(n+".png")

    input("")


# Verifica se o nome do arquivo foi fornecido como argumento de linha de comando
if len(sys.argv) < 2:
    print("Use: python programa.py nome_do_arquivo.dat")
    sys.exit()

# Abre o arquivo fornecido como argumento
nome_pasta = sys.argv[1]
try:
    montar(nome_pasta)
    
except FileNotFoundError:
    print("Arquivo não encontrado:", nome_pasta)
    sys.exit()
