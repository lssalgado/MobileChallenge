import urllib, json
url = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data