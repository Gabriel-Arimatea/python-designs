from gof.creational import (singleton,factory_method)
from gof.structural import (facade,adapter,composite,proxy, decorator)

if __name__ == "__main__":
    designs = [
        singleton, factory_method, #Criacionais
        facade, adapter, composite, proxy, decorator, #Estruturais
    ]

    for design in designs:
        print(f"=======================================================")
        print(f"TESTANDO DESIGN {design}")
        design.test()
        print(f"=======================================================")
    