import sys, os, matplotlib.pyplot as plt, numpy as np 

sys.path.append("./resultado")

import base

class Imagem(base.Base):

    def __init__(self, estruturas):
        super().__init__(estruturas)

        self.dir = "./Saídas/" + self.agora
        os.mkdir(self.dir)

        self.figsize = None
        self.dpi = None

    def configurar_imagem(self, figsize, dpi, tamanho_fonte = 22):
        self.figsize = figsize
        self.dpi = dpi
        plt.rcParams['font.size'] = tamanho_fonte

    def grafico_perda_por_retorno(self, mascara = None, faixa = None, marcacoes =[]):
        plt.figure(figsize=self.figsize, dpi=self.dpi)
        legendas = []

        if(mascara == None): mascara = np.full(self.qtd_estruturas, 1) #Plota Tudo

        #Plotar Curvas
        for i in range(self.qtd_estruturas):
            if(mascara[i] == 1):
                if(faixa == None):
                    x = self.estruturas[i].frequencia
                    y = self.estruturas[i].s11
                else:
                    inicio = self.estruturas[i].retornar_indice(faixa[0])
                    fim = self.estruturas[i].retornar_indice(faixa[1])
                    x = self.estruturas[i].frequencia[inicio:fim+1]
                    y = self.estruturas[i].s11[inicio:fim+1]
                
                legendas.append(self.estruturas[i].nome)
                plt.plot(x,y)
        
        #Plotar algum ponto desejado
        for marcacao in marcacoes:
            for estrutura in self.estruturas:
                indice = estrutura.retornar_indice(marcacao)
                x = estrutura.frequencia[indice]
                y = estrutura.s11[indice]
                
                legendas.append("%.01f GHz - %s" %(marcacao, estrutura.nome))
                plt.plot(x,y,marker='o')

        #Últimas Configurações
        plt.legend(legendas)
        plt.title("Perda por Retorno")
        plt.xlabel("Frequência [GHz]")
        plt.ylabel("Perda por Retorno [dB]")
        plt.grid(True)

        #Salvar com nome único
        nome = "grafico"
        while(os.path.exists(self.dir + "/" + nome + ".png")):
            nome += "1"
        
        plt.savefig(self.dir + "/" + nome + ".png")
