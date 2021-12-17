import requests
import json
import time

# url local - definida no app.py - executada pelo Flask
url = 'http://127.0.0.1:5000'

# parâmetros de entrada:
classes      = [1,2,3]
idades       = [i for i in range(10,90,1)]
qtdParentes  = [i for i in range(12)]
passagems    = [i for i in range(30,1000,50)]

def generate_use_cases():
    for classe in classes:
        for idade in idades:
            for parents in qtdParentes:
                for passagem in passagems:
                    yield {'Pclass': classe, 'Age': idade, 'SibSp': parents, 'Fare': passagem}

if __name__ == '__main__':
    for data in generate_use_cases():
       
        print(data)
        data = json.dumps(data)
        
        start = time.time()
        send_request = requests.post(url, data)
        print("tempo de resposta: ",time.time()-start)
        print(send_request.json())