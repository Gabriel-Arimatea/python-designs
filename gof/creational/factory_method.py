from abc import ABC

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

class KnifeFactory:

    def create_knife(self, type):
        if type == 'steak':
            print("Criando faca de carne")
            return SteakKnife()
        elif type == 'bread':
            print("Criando faca de pão")
            return BreadKnife()
        else:
            raise NotImplemented("Não se produz esse tipo de faca")

class KnifeStore:

    def order_knife(self, type):
        knife = KnifeFactory().create_knife(type)
        knife.sharpen()
        knife.polish()
        knife.package()
        return knife


def test():

    store = KnifeStore()
    steak_knife = store.order_knife('steak')
    print(type(steak_knife))
    bread_knife = store.order_knife('bread')
    print(type(bread_knife))
