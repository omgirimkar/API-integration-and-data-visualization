import requests
city_name ="new delhi"
api_key ="4ef7cca153cb2e3e5254a54d74154398"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"


response = requests.get(url)
if response.status_code == 200:
    data  = response.json()
    print(data)

print("weather is",data["weather"][0]["description"])
print("current temperature",data["main"]["temp"])
print("current temperature feels like is",data["main"]["feels_like"])
print("humidity is", data["main"]["humidity"])