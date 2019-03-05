from datetime import datetime
import os

class Base:

    def __init__(self, estruturas):
        self.estruturas = estruturas
        self.agora = str(datetime.now()).replace(":", "-")
        self.qtd_estruturas = len(estruturas)

        if(not(os.path.exists("Saídas"))):
            os.mkdir("Saídas")