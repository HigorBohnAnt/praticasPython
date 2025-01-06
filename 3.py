import socket
import requests

def obter_ip_local():
    ip_local = socket.gethostbyname(socket.gethostname())
    return ip_local

def obter_ip_publico():
    try:
        resposta = requests.get('https://api.ipify.org?format=json')
        ip_publico = resposta.json()['ip']
        return ip_publico
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter o IP público: {e}"

ip_local = obter_ip_local()
ip_publico = obter_ip_publico()

print(f"IP Local: {ip_local}")
print(f"IP Público: {ip_publico}")
