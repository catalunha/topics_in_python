import requests

url = "https://viacep.com.br/ws/77018416/json/"
response = requests.get(url)
print(response.text)
