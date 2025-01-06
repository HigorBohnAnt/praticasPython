import requests

def obter_localizacao_ip():
    try:
        resposta = requests.get("https://ipinfo.io")
        dados = resposta.json()

        cidade = dados.get("city")
        regiao = dados.get("region")
        pais = dados.get("country")
        localizacao = dados.get("loc").split(',')

        latitude = localizacao[0]
        longitude = localizacao[1]

        return f"Localização aproximada: {cidade}, {regiao}, {pais} (Latitude: {latitude}, Longitude: {longitude})"
    except Exception as e:
        return f"Erro ao obter localização: {e}"

localizacao = obter_localizacao_ip()
print(localizacao)