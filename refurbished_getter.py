import os, urllib, json

def getContent(str):
  response = urllib.urlopen(str)
  data = json.loads(response.read())
  return data

def selector(obj, aux):

  print("Selecione a fruta desejada:")

  for i in obj["fruits"]:
      print str(aux) + " - " + i["name"] + ": " + str(i["price"])
      aux = aux + 1
    
  getInput(aux)

def getInput(aux):
    while True:
        value = raw_input('')
        try:
            value = int(value)
        except:
            print "Opcao invalida, favor selecionar uma fruta:"
            continue
        if value < 0 or value > aux:
            print "Opcao invalida, favor selecionar uma fruta:"
            
        else:
            break

    fruit = input("")

def main():
  os.system('cls||clear')
  
  url = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"
  counter = 0
  dolarToReal = 3.5
  fruit = 0

  fruitsJson = getContent(url)
  
  selector(fruitsJson, counter)

if __name__ == "__main__":
  main()