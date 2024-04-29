import requests

url = 'http://traductor-production-b952.up.railway.app/translate'  # Reemplaza 'tu_dominio' con la URL de tu API
data = {'textsource': 'Hello, how are you?', 'target_lang': 'ES'}

response = requests.post(url, json=data)

if response.status_code == 200:
    translated_text = response.json()['result']
    print(translated_text)
else:
    print('Error en la solicitud:', response.status_code)