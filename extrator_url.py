class Extrator_Url:
    #Função inicializadora da classe
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    #Função retira os espaços em branco de url
    def sanitiza_url(self, url):
        return url.strip()

    #Função verifica se url não está vazia
    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia!")

    #Função retorna a base da url
    def get_base_url(self):
        indice_interrocacao = self.url.find("?")
        url_base = self.url[:indice_interrocacao]
        return url_base

    #Função retorna os parâmetros da url
    def get_parametros_url(self):
        indice_interrocacao = self.url.find("?")
        url_parametros = self.url[indice_interrocacao + 1:]
        return url_parametros

    #Função retorna o valor de cada parâmetro conforme nome
    def get_retorna_valor(self, nome_parametro):
        indice_parametro = self.get_parametros_url().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        verifica_e_comercial = self.get_parametros_url().find("&", indice_valor)
        valor_parametro = ""
        if verifica_e_comercial == -1:
            valor_parametro = self.get_parametros_url()[indice_valor:]
        else:
            valor_parametro = self.get_parametros_url()[indice_valor:verifica_e_comercial]
        return valor_parametro

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_parametros_url() + "\n" + "URL Base: " + self.get_base_url()

    def __eq__(self, other):
       return self.url == other.url


extrator_url = Extrator_Url("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
extrator_url2 = Extrator_Url("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
extrator_url.valida_url()

nome_parametro = "quantidade"
base = extrator_url.get_base_url()
parametros = extrator_url.get_parametros_url()
valor = extrator_url.get_retorna_valor(nome_parametro)

'''
print(base)
print(parametros)
print("Valor: {}".format(valor))

print("O tamanho da nossa URL é: {} ".format(len(extrator_url)))
'''

#Verificar igualdade entre objetos
print(extrator_url == extrator_url2)

print(extrator_url)