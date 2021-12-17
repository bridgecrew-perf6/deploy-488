import pickle
import numpy as np
import pandas as pd
import os
import time


class Model:
    def __init__(self) -> None:

        '''
            Definição: 
                Classe que encapsula o modelo de predição de sobrevivência e seus pré processamentos
        '''

        self.engine = pickle.load(open('src/models/model.pkl','rb'))
    
    def predict(self,data : dict) -> dict:

        '''
            Definição:
                Método de predição de sobrevivência de um pasageiro do titanic. 

            Entrada:   
                Dicionário {'Pclass': classe, 
                            'Age':    idade, 
                            'SibSp':  parents, 
                            'Fare':   passagem}
            Retorna:   
                Um dicionario da predição de sobrevivencia de um passageiro do titanic
                1: Sobreviveu
                0: Não sobreviveu
        
        '''

        start = time.time()
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)
        print("tempo de conversão para dataframe: ", time.time() - start)
        result = self.engine.predict(data_df)

        output = {'results': int(result[0])}

        return output

