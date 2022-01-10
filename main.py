url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

print(url_parametros.find("?"))

parametro_quantidade = "quantidade"
parametro_moedaOrigem = "moedaOrigem"
parametro_moedaDestino = "moedaDestino"

indice_parametro_q = url_parametros.find(parametro_quantidade)
indice_parametro_mo = url_parametros.find(parametro_moedaOrigem)
indice_parametro_md = url_parametros.find(parametro_moedaDestino)

print(indice_parametro_q)

indice_valor = indice_parametro_q + len(parametro_quantidade) + 1
indice_valor_mo = indice_parametro_mo + len(parametro_moedaOrigem) + 1
indice_valor_md = indice_parametro_md + len(parametro_moedaDestino) + 1

valor = url_parametros[indice_valor:]
valor_mo_mais = url_parametros[indice_valor_mo:]
valor_md_mais = url_parametros[indice_valor_md:]

indice_igual = url_parametros.find("=", indice_parametro_q) + 1
indice_igual_mo = url_parametros.find("=", indice_parametro_mo) + 1
indice_igual_md = url_parametros.find("=", indice_parametro_md) + 1

valorI = url_parametros[indice_igual:]
valor_mo = url_parametros[indice_igual_mo:]
valor_md = url_parametros[indice_igual_md:]

print(valor)
print(valorI)
print(valor_mo)
print(valor_md)
print(valor_mo_mais)
print(valor_md_mais)

indice_valor_final_mo = url_parametros.find("&", indice_valor_mo)
valor_mo_mais = url_parametros[indice_valor_mo:indice_valor_final_mo]

indice_valor_final_md = url_parametros.find("&", indice_valor_md)
valor_md_mais = url_parametros[indice_valor_md:indice_valor_final_md]

print(valor_mo_mais)
print(valor_md_mais)



