import re
'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

'''

#url padrão https://www.bytebank.com.br/cambio

url = "https://bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
busca = padrao_url.match(url)

if not busca:
    raise ValueError("URl não é valida!")

print("URL é valida!")
