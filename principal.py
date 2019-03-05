#Esse arquivo é o que vai gerar os resultados

import estrutura, resultado.texto as texto, resultado.imagem as imagem

#Escolher as estruturas que serão lidas

nomes = ["Arranjo Retangular", "Arranjo Circular"] #Nomes de apresentação
diretorios = ["arranjo_retangular", "arranjo_circular"] #Diretórios
#===========================================================================================

#Lendo Estruturas

estruturas = []
for i in range(len(nomes)):
    estruturas.append(estrutura.Estrutura(diretorios[i], nomes[i]))
#=============================================================================================

#Iniciar Resultados
resultado_texto = texto.Texto(estruturas)
resultado_imagem = imagem.Imagem(estruturas)
resultado_imagem.configurar_imagem((20, 12), 128)

#=============================================================================================

#Relatório Textual
resultado_texto.escrever_bandas()
resultado_texto.escrever_s11(28)
resultado_texto.escrever_s11(25)

#=============================================================================================

#Relatório Imagem
resultado_imagem.grafico_perda_por_retorno()
resultado_imagem.grafico_perda_por_retorno(mascara=[0,1])
resultado_imagem.grafico_perda_por_retorno(faixa=[20,30])
resultado_imagem.grafico_perda_por_retorno(faixa=[20,30], marcacoes=[25,28])
#=============================================================================================