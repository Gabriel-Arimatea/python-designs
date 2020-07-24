from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transfer(self, amount):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_value(self):
        raise NotImplementedError("Método não implementado")


class Chequing(Account):

    def __init__(self, initial_amount=0.0):
        self.value = initial_amount
    
    def deposit(self, amount):
        self.value += amount
        print(f'Depósito de {amount:.2f} feito em Chequing')
    
    def withdraw(self, amount):
        self.value -= amount
        print(f'Retirada de {amount:.2f} feito em Chequing')
    
    def transfer(self, amount):
        self.value -= amount
        print(f'transferência de {amount:.2f} feito em Chequing')
    
    def get_value(self):
        return self.value


class Saving(Account):
    
    def __init__(self, initial_amount=0.0):
        self.value = initial_amount
    
    def deposit(self, amount):
        self.value += amount
        print(f'Depósito de {amount:.2f} feito em Saving')
    
    def withdraw(self, amount):
        self.value -= amount
        print(f'Retirada de {amount:.2f} feito em Saving')
    
    def transfer(self, amount):
        self.value -= amount
        print(f'transferência de {amount:.2f} feito em Saving')
    
    def get_value(self):
        return self.value


class Investment(Account):
    
    def __init__(self, initial_amount=0.0):
        self.value = initial_amount
    
    def deposit(self, amount):
        self.value += amount
        print(f'Depósito de {amount:.2f} feito em Investment')
    
    def withdraw(self, amount):
        self.value -= amount
        print(f'Retirada de {amount:.2f} feito em Investment')
    
    def transfer(self, amount):
        self.value -= amount
        print(f'transferência de {amount:.2f} feito em Investment')
    
    def get_value(self):
        return self.value


class BankService:

    def __init__(self):
        self.bank_accounts = []

    def create_new_account(self, type, initial_amount):
        if type == 'chequing':
            self.bank_accounts.append(Chequing(initial_amount=initial_amount))
        elif type == 'saving':
            self.bank_accounts.append(Saving(initial_amount=initial_amount))
        elif type == 'investment':
            self.bank_accounts.append(Investment(initial_amount=initial_amount))
        else:
            raise TypeError("Tipo de conta não suportado.")

    def transfer(self, index_from, index_to, amount):
        self.bank_accounts[index_from].withdraw(amount)
        self.bank_accounts[index_to].deposit(amount)

def test():
    bank = BankService()
    bank.create_new_account('chequing', 10.0)
    bank.create_new_account('saving', 20.0)
    bank.create_new_account('investment', 30.0)
    
    for account in bank.bank_accounts:
        print(account.get_value())

    bank.transfer(2,0,10.0)

    for account in bank.bank_accounts:
        print(account.get_value())