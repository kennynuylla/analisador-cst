import sys

sys.path.append("./resultado")

import base

class Texto(base.Base):

    def __init__(self, estruturas):
        super().__init__(estruturas)
        
        self.arquivo = open("./Saídas/Relatório - %s.txt" %(self.agora), "w", encoding="utf8")
        self.arquivo.write("Relatório Gerado em %s\n" %(self.agora))
        self.arquivo.write("Estruturas: ")

        for i in range(self.qtd_estruturas - 1):
            self.arquivo.write("%s, " %(estruturas[i].nome))
        
        self.arquivo.write("%s\n\n\n" %(estruturas[self.qtd_estruturas - 1].nome))

    def __del__(self):
        self.arquivo.close()

    def escrever_bandas(self):
        self.arquivo.write(".:BANDAS DE SINTONIA\n")
        for estrutura in self.estruturas:
            self.arquivo.write("-> %s\n" %(estrutura.nome))
            self.arquivo.write("Início da Banda | Fim da Banda | Frequência com Menor S11 | Menor S11\n")
            for banda in estrutura.bandas:
                self.arquivo.write("%f       | %f    | %f                | %f\n" %(banda["inicio"], banda["fim"], 
                    banda["frequencia_menor_s11"], banda["menor_s11"]))
            self.arquivo.write("\n")
            
        self.arquivo.write("\n")

    def escrever_s11(self, frequencia):
        self.arquivo.write(".:S11 em %f GHz\n" %(frequencia))
        for estrutura in self.estruturas:
            self.arquivo.write("-> %s: %f\n" %(estrutura.nome, estrutura.obter_s11(frequencia)))
        
        self.arquivo.write("\n\n")
