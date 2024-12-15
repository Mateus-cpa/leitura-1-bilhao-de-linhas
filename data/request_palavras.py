import requests as re

resposta = re.get('https://www.ime.usp.br/~pf/dicios/br-utf8.txt')
print(f'tipo response: {type(resposta)}')
print(resposta.status_code)
conteudo_site = resposta.text.encode('utf-8')

with open('palavras_portugues.txt', 'wb') as palavras:
    palavras.write(conteudo_site)
    


