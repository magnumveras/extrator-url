import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            url = ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        busca = padrao_url.match(url)

        if not busca:
            raise ValueError("URl não é valida!")

        print("URL é valida!")

        '''
        if not self.url.startswith("https://"):
            raise ValueError("A URL não é segura!")

        if not self.get_base_url().endswith("/cambio"):
            raise ValueError("URl está errada!")
        '''
    def get_base_url(self):
        indice_interrocacao = self.url.find("?")
        url_base = self.url[:indice_interrocacao]
        return url_base

    def get_parametros_url(self):
        indice_interrocacao = self.url.find("?")
        url_parametro = self.url[indice_interrocacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro):
        indice_parametro = self.url.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        verifica_e_comercial = self.url.find("&", indice_valor)
        if verifica_e_comercial == -1:
            valor_parametro = self.url[indice_valor:]
        else:
            valor_parametro = self.url[indice_valor:verifica_e_comercial]

        return valor_parametro


url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
#url = " "
extrator = ExtratorURL(url)
valor = extrator.get_valor_parametro("quantidade")
print(valor)