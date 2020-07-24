import json

from abc import ABC, abstractmethod


class WebService:
    
    def request(self, json):
        try:
            json.dumps(json)
        except:
            print("Recebeu um dict")
        
class WebRequester(ABC):

    @abstractmethod
    def request(self, object):
        raise NotImplementedError("Request não implementado.")

class WebAdapter(WebRequester):

    def connect(self, web_service):
        self.web_service = web_service

    def request(self, object):
        json = self.to_json(object)
        self.web_service.request(json)
        print("Request feito com sucesso")

    def to_json(self, object):
        return {
            'mensagem': object.mensagem,
            'codigo': object.codigo
        }

class Body:

    def __init__(self, mensagem, codigo):
        self.mensagem = mensagem
        self.codigo = codigo

class WebClient:

    def __init__(self, web_adapter):
        self.web_adapter = web_adapter

    def make_object(self):
        return Body('teste', 200)

    def do_work(self):
        self.web_adapter.request(self.make_object())

def test():
    web_service = WebService()
    adapter = WebAdapter()
    adapter.connect(web_service)
    client = WebClient(adapter)
    client.do_work()