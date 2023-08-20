import ROOT
import sys

def grafico(arquivo):
    pass
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
   print("1) Informacao branch \n2)")
   escolha = int(input())
   switch(escolha,nome_pasta)
    
except FileNotFoundError:
    print("Arquivo não encontrado:", nome_pasta)
    sys.exit()
