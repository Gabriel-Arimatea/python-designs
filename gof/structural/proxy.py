from abc import ABC, abstractmethod


class Order(ABC):

    @abstractmethod
    def fullfill_order(self):
        raise NotImplementedError("Adicionar não implementado")


class SimpleWarehouse(Order):

    def __init__(self, name, stock):
        self.__name = name
        self.__stock = stock
    
    def fullfill_order(self):
        print("Registrando pedido")
        self.__stock -= 1

    def get_stock(self):
        return self.__stock

    def get_name(self):
        return self.__name

class MediumWarehouse(Order):

    def __init__(self, name, stock):
        self.__name = name
        self.__stock = stock
    
    def fullfill_order(self):
        print("Registrando pedido")
        print("Saiu para transportadora")
        self.__stock -= 1

    def get_stock(self):
        return self.__stock

    def get_name(self):
        return self.__name

class LargeWarehouse(Order):

    def __init__(self, name, stock):
        self.__name = name
        self.__stock = stock
    
    def fullfill_order(self):
        print("Registrando pedido")
        print("Gerando nota fiscal")
        print("Saiu para transportadora")
        self.__stock -= 1

    def get_stock(self):
        return self.__stock

    def get_name(self):
        return self.__name

class OrderFullfillment(Order):

    def __init__(self):
        self.__warehouses = []
    
    def add_warehouse(self, warehouse):
        self.__warehouses.append(warehouse)
    
    def fullfill_order(self):
        for warehouse in self.__warehouses:
            print(f"Checando depósito {warehouse.get_name()}")
            if warehouse.get_stock() > 0:
                warehouse.fullfill_order()
                break
            else:
                print(f"Pedido não pode ser atendido pelo depósito {warehouse.get_name()}")


def test():
    warehouse1 = SimpleWarehouse('teste1', 1)
    warehouse2 = MediumWarehouse('teste2', 2)
    warehouse3 = LargeWarehouse('teste3', 3)
    order = OrderFullfillment()
    order.add_warehouse(warehouse1)
    order.add_warehouse(warehouse2)
    order.add_warehouse(warehouse3)

    for i in range(0,7):
        print("------------------------")
        print(f"Gerando pedido # {i+1}")
        order.fullfill_order()