from gof.creational import (singleton,factory_method)

if __name__ == "__main__":
    designs = [
        singleton,
        factory_method
    ]

    for design in designs:
        design.test()
    