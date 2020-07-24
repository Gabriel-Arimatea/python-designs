class SingletonBase:

    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance

def singleton(self):
    instances = {}
    def instance():
        if self not in instances:
            instances[self] = self()
        return instances[self]
    return instance

class Singleton(SingletonBase):
    pass

@singleton
class Singleton2:
    pass

def test():
    s1 = Singleton()
    s2 = Singleton()

    if s1 is s2:
        print("Singleton funciona.")
    else:
        print("Singleton falhou.")

    s3 = Singleton2()
    s4 = Singleton2()

    if s3 is s4:
        print("Singleton pelo decorator funciona.")
    else:
        print("Singleton pelo decorator falhou.")
