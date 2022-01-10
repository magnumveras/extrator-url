url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

#url = ""
print(url)

#Sanitização da URL
url = url.strip()

#Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

#Pega até a interrogação da URL e coloca em variável
indice_interrocacao = url.find("?")
url_base = url[:indice_interrocacao]
print(url_base)

#Pega URL após a interrogação com parâmetros
url_parametro = url[indice_interrocacao + 1:]
print(url_parametro)

parametro = "quantidade"
indice_parametro = url_parametro.find(parametro)
indice_valor = indice_parametro + len(parametro) + 1
verifica_e_comercial = url_parametro.find("&", indice_valor)
print(indice_valor)
if verifica_e_comercial == -1:
    valor_parametro = url_parametro[indice_valor:]
else:
    valor_parametro = url_parametro[indice_valor:verifica_e_comercial]

print("Moeda Origem = {}".format(valor_parametro))

