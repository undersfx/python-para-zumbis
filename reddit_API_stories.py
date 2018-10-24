import urllib.request
import json

url = 'http://www.reddit.com/r/Python/.json'

#Solução para "urllib.error.HTTPError: HTTP Error 429: Too Many Requests"
#Reddit bloqueia certas conexões vindas de um mesmo User-Agent
#Usar User-Agent customizado para não compartilhar com o padrão da urllib
#Setar fake User-Agent a ser utilizado
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

#Cria uma request com o header customizado
request = urllib.request.Request(url,headers={'User-Agent': user_agent})

#Realiza o request passando o objeto criado
resp = urllib.request.urlopen(request).read()

parsed = json.loads(resp.decode('utf-8'))

for item in parsed['data']['children']:
  doc = item['data']
  print (doc['title'])
  print ('#comments: %d' %doc['num_comments'])
  print (doc['url'])
  print ()