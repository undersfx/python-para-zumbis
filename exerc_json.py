import urllib.request
import json

url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

resp = urllib.request.urlopen(url).read()
print('RESPOSTA:', resp)
print(type(resp), '\n')

data = json.loads(resp.decode('utf-8'))
print('DADOS:', data)
print(type(data), '\n')

print ('PIADA:', data['value']['joke'])
