import ROOT
import sys

def grafico(arquivo,consulta):
    canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)
    
    entrada = ROOT.TFile(arquivo,'read')
    tree = entrada.Get("tree")
    histogram = ROOT.TH1F("histograma_phi", "abs(id)==321 || abs(id)==211;\pi ;Contagem", 100, -ROOT.Math.Pi(),ROOT.Math.Pi())
    histogram.GetXaxis().SetTitleSize(0.05) # Tamanho legenda X
    histogram.GetYaxis().SetTitleSize(0.05)
    histogram.GetYaxis().SetRangeUser(0, 200)
    histogram.SetFillColor(ROOT.kBlue-9)
    tree.Draw("phi >> histograma_phi", consulta)


    
    canvas.Update()
    histogram.Draw()
    comando= 'phi_abs(id) == 321'
    salvar = input("salvar grafico ?").upper()
    if salvar == 'S' or salvar == 'SIM':
        n = 'grafico/grafico_'+comando
        print(n)
        canvas.SaveAs(n+".png")

def infos_branch(arquivo):
    entrada = ROOT.TFile(arquivo,'read')
    tree = entrada.Get("tree")
    print("Quantidade de branches {}".format(tree.GetNbranches()))
    print("Nome de cada branche")
    for branch in  tree.GetListOfBranches():
        print(branch)

def switch(case,arquivo):
   if case == 1:
    infos_branch(arquivo)
   elif case ==2:
    consulta = input("insira o Comando : ")
    grafico(arquivo,consulta)
"""

endereco = "data/root/data.root"
infos_branch(endereco)
"""

# Verifica se o nome do arquivo foi fornecido como argumento de linha de comando
if len(sys.argv) < 2:
    print("Use: python programa.py nome_do_arquivo.dat")
    sys.exit()

# Abre o arquivo fornecido como argumento
nome_pasta = sys.argv[1]
try:
   # infos_branch("data/root/data.root")
   print("Escolha as opcoes:")
   print("1) Informacao branch \n2) Criar grafico")
   escolha = int(input())
   switch(escolha,nome_pasta)
    
except FileNotFoundError:
    print("Arquivo não encontrado:", nome_pasta)
    sys.exit()
