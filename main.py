import requests

# o retorno do json precisa pegar "current_condition" e depois "temp_C"

BASE_URL = "https://wttr.in/{}?format=j1"

def get_temperature_api(cidade: str):
    r = requests.get(BASE_URL.format(cidade))
    r.raise_for_status()
    res = r.json()

    current_condition = res["current_condition"][0]
    temp_c = current_condition.get("temp_C")

    print(temp_c)
    
    return temp_c

def load_csv():
    with open('cidades.csv') as cidades:
        return cidades.readlines()

def generate_csv(dados_cidade: dict):
    # gerar csv das cidades
    with open("csvnew.csv", "w") as new:
        new.write('cidade,pais,temperatura_c\n')
        cidades_nome = dados_cidade.keys()
        print(cidades_nome)
        for k, v in dados_cidade.items():
            nova_linha = k + ',' + v + '\n'
            # nova_linha += "," + dados_cidade[v]
            new.write(nova_linha)
        return
    
if __name__ == "__main__":
    cidades = load_csv()

    # Adicionar for loop para pegar todas as temperaturas
    temperaturas = dict()
    for index, linha in enumerate(cidades):
        if index == 0:
            continue

        [cidade, pais] = linha.split(",")
        pais = pais.strip()
        print(f"Chamando API para cidade {cidade}")
        try:
            t = get_temperature_api(cidade)
        except Exception as e:
            print(f"Cidade {cidade} falhou. Erro: {e}")  
            continue
        
        temperaturas[f"{cidade},{pais}"] = t
        
        

    print(temperaturas)
    generate_csv(temperaturas)

    # temperatura = get_temperature_api("Santos")

        

    

    
