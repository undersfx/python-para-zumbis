import urllib.request
import json
import pprint

#url = 'https://graph.facebook.com/<user>' #Não Funciona mais
api_url = "https://graph.facebook.com/v3.0"

#Novo Método
#Criar aplicativo: https://developers.facebook.com/apps/
#Gerar token de acesso: https://developers.facebook.com/tools/explorer/?method=GET&path=me%3Ffields%3Did%2Cname&version=v3.1
#API Tutorial: https://developers.facebook.com/docs/graph-api/using-graph-api/
#Gerar token permanente: https://dev.to/daviducolo/permanent-facebook-page-access-token-3epi

token = ''

#Buscar dados (passa token, retorna nome e id)
resp = urllib.request.urlopen(api_url + '/me?access_token=%s' %token).read()

data = json.loads(resp.decode('utf-8'))

pprint.pprint(data)
#print (json.dumps(data, indent=4))