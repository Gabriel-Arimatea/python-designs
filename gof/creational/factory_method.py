from abc import ABC, abstractmethod

class Knife:
    def sharpen(self):
        print("Faca afiada")

    def polish(self):
        print("Faca polida")

    def package(self):
        print("Faca embalada")


class SteakKnife(Knife):
    pass


class BreadKnife(Knife):
    pass


class ChefsKnife(Knife):
    pass


class KnifeStore(ABC):

    @abstractmethod
    def get_knife(self, type):
        raise NotImplementedError("Método não implementado")

    def order_knife(self, type):
        knife = self.get_knife(type)
        knife.sharpen()
        knife.polish()
        knife.package()
        return knife


class SimpleKnifeStore(KnifeStore):

    def get_knife(self, type):
        if type == 'steak':
            print("Criando faca de carne")
            return SteakKnife()
        elif type == 'bread':
            print("Criando faca de pão")
            return BreadKnife()
        else:
            raise TypeError("Não se produz esse tipo de faca")


class CompleteKnifeStore(KnifeStore):

    def get_knife(self, type):
        if type == 'steak':
            print("Criando faca de carne")
            return SteakKnife()
        elif type == 'bread':
            print("Criando faca de pão")
            return BreadKnife()
        elif type == 'chefs':
            return ChefsKnife()
        else:
            raise TypeError("Não se produz esse tipo de faca")


def test():

    print('Testando loja simples')
    simple_store = SimpleKnifeStore()
    steak_knife = simple_store.order_knife('steak')
    print(type(steak_knife))
    bread_knife = simple_store.order_knife('bread')
    print(type(bread_knife))
    try:
        chefs_knife = simple_store.order_knife('chefs')
        print(type(chefs_knife))
    except:
        print('Esta loja de fato não vende faca de chef')

    print('Testando loja completa')
    complete_store = CompleteKnifeStore()
    steak_knife = complete_store.order_knife('steak')
    print(type(steak_knife))
    bread_knife = complete_store.order_knife('bread')
    print(type(bread_knife))
    chefs_knife = complete_store.order_knife('chefs')
    print(type(chefs_knife))

