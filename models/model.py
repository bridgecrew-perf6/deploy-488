import pickle
import numpy as np
import pandas as pd

# load model
class Model:
    def __init__(self) -> None:
        '''
            Entrada: Dataframe 
            Retorna: um dicionario da predição 
            de sobrevivencia de um passageiro do titanic
        '''

        self.engine = pickle.load(open('model.pkl','rb'))
    
    def predict(self,data) -> dict:

        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)
        result = self.engine.predict(data_df)

        # send back to browser
        output = {'results': int(result[0])}

        return result