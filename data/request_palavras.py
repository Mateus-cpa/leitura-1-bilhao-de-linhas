import requests as re
import io

resposta = re.get('https://www.ime.usp.br/~pf/dicios/br-utf8.txt')

conteudo_site = resposta.text.encode(encoding='utf-8').decode(encoding='utf-8')

print(f'tipo conteúdo site: {type(conteudo_site)}')
print(conteudo_site.split('\n')[0:5])

with open('palavras_portugues.txt', 'w') as palavras:
    palavras.write(conteudo_site)
    
    


