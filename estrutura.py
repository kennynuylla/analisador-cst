class Estrutura:

    def __init__(self, diretorio, nome): #O diretório deve ser o mesmo da pasta
        self.frequencia = []
        self.s11 = []
        self.bandas = []
        self.nome = nome
        self.diretorio = diretorio

        arquivo = open(diretorio)
        linhas = arquivo.readlines()
        linhas = linhas[2:]
        arquivo.close()

        for linha in linhas:
            linha = linha.split()
            if(linha == []): continue #Pular eventuais linhas em branco
            self.frequencia.append(float(linha[0]))
            self.s11.append(float(linha[1]))
        
        self.analisar_bandas()
    
    def analisar_bandas(self):
        temp = {}
        menor_s11 = 0
        frequencia_menor_s11 = 0
        total_frequencias = len(self.frequencia)
        for i in range(total_frequencias):
            if(self.s11[i] < menor_s11):
                menor_s11 = self.s11[i]
                frequencia_menor_s11 = self.frequencia[i]

            if(self.s11[i] <= -10): #Abaixo -10dB é entendido como frequência de sintonia
                if("inicio" in temp.keys()):
                    if(i == total_frequencias - 1):
                        temp["fim"] = self.frequencia[i]
                        temp["frequencia_menor_s11"] = frequencia_menor_s11
                        temp["menor_s11"] = menor_s11
                        self.bandas.append(temp)

                        temp = {}
                        menor_s11 = 0
                else:
                    temp["inicio"] = self.frequencia[i]

            elif(self.s11[i] > -10):
                if("inicio" in temp.keys()):
                    temp["fim"] = self.frequencia[i]
                    temp["frequencia_menor_s11"] = frequencia_menor_s11
                    temp["menor_s11"] = menor_s11
                    self.bandas.append(temp)

                    temp = {}
                    menor_s11 = 0

    def retornar_indice(self, frequencia):
        frequencia_inicial = self.frequencia[0]
        stepsize = self.frequencia[1] - self.frequencia[0]

        return int(round((frequencia - frequencia_inicial)/stepsize))

    def obter_s11(self, frequencia):
        indice = self.retornar_indice(frequencia)
        return self.s11[indice]


