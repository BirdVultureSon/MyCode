from urllib import request

a = request.urlopen('http://158.160.6.201/api/weather/temp.php')
data = a.read().decode()
print(f"Температура: {data}")
b = request.urlopen('http://158.160.6.201/api/weather/wind.php')
dataB = b.read().decode()
print(f"Ветер: {dataB}")
c = request.urlopen('http://158.160.6.201/api/weather/humidity.php')
dataC = c.read().decode()
print(c)
print(f"Влажность: {dataC}")