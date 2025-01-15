import json


def calcular_faturamento(dados_faturamento):
    
    faturamento_validos = [faturamento for faturamento in dados_faturamento if faturamento is not None]
    

    menor_faturamento = min(faturamento_validos)
  
    maior_faturamento = max(faturamento_validos)
    
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_media = sum(1 for faturamento in faturamento_validos if faturamento > media_mensal)
    

    return menor_faturamento, maior_faturamento, dias_acima_media


def carregar_dados_json(arquivo_json):
    with open(arquivo_json, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    
    arquivo_json = "faturamento.json"
    
    dados_faturamento = carregar_dados_json(arquivo_json)
    
  
    menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)
    

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
