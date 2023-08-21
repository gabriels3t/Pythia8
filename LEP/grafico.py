import ROOT
import sys

def grafico(arquivo,branch,consulta,label):
    canvas = ROOT.TCanvas("canvas", "Canvas", 800, 600)
    
    entrada = ROOT.TFile(arquivo,'read')
    tree = entrada.Get("tree")

    hist_name = "histograma_"+branch
    titulo = branch+" "+consulta
    if(branch == 'phi'):
        histogram = ROOT.TH1F(hist_name, titulo+";"+label+" ;Contagem", 100, -ROOT.Math.Pi(),ROOT.Math.Pi())
        histogram.GetYaxis().SetRangeUser(0, 200)
    
    histogram = ROOT.TH1F(hist_name, titulo+";"+label+" ;Contagem", 100, 0,0)
    histogram.GetXaxis().SetTitleSize(0.05) # Tamanho label X
    histogram.GetYaxis().SetTitleSize(0.05)
    
    histogram.SetFillColor(ROOT.kBlue-9)
    
    tree.Draw(branch+">>"+hist_name, consulta)
    canvas.Update()
    histogram.Draw()

    salvar = input("salvar grafico ?").upper()
    if salvar == 'S' or salvar == 'SIM':
        n = 'grafico/grafico_'+titulo
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
    branch = input("Insira o nome da Branch : ")
    consulta = input("Insira o Comando : ")
    label_x= input("label x : ")
    
    grafico(arquivo,branch,consulta,label_x)
   elif case==3:
      caminho_macro = 'macro.txt'
      with open(caminho_macro, 'r') as macro:
            macro = macro.readlines()
    
      for i in range(0,len(macro),3):
         branch =macro[i].strip()
         consulta =macro[i+1].strip()
         label_x = macro[i+2].strip()
         grafico(arquivo,branch,consulta,label_x)

# Verifica se o nome do arquivo foi fornecido como argumento de linha de comando
if len(sys.argv) < 2:
    print("Use: python programa.py nome_do_arquivo.dat")
    sys.exit()

# Abre o arquivo fornecido como argumento
nome_pasta = sys.argv[1]
try:
   print("Escolha as opcoes:")
   print("1) Informacao branch \n2) Criar grafico \n3) macro")
   escolha = int(input())
   switch(escolha,nome_pasta)
    
except FileNotFoundError:
    print("Arquivo não encontrado:", nome_pasta)
    sys.exit()
