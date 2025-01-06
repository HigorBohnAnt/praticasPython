import requests

def get_weather(city, api_key):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f"Condição do tempo em {city}: {weather}")
        print(f"Temperatura: {temperature}°C")
        print(f"Umidade: {humidity}%")
    else:
        print(f"Erro ao acessar a API. Código de status: {response.status_code}")

api_key = 'f5a1e14d013fc4f19ab6d94822ac0f57' 
city = 'Joinville,br' 

get_weather(city, api_key)
