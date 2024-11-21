import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
city = input('City Name :')
url = api_address + city
print(url)
json_data = requests.get(url).json()
print(json_data)
format_add = json_data['weather'][0]['main']
format_add1 = json_data['weather'][0]['description']
print(format_add,"and",format_add1)