from abc import ABC, abstractmethod


class WebPage(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError("Nada a mostrar")


class BasicWebPage(WebPage):

    def __init__(self, body, css, js):
        self.__body = body
        self.__css = css
        self.__js = js

    def display(self):
        print(f"Carregando body: {self.__body} ")
        print(f"Carregando css: {self.__css} ")
        print(f"Carregando js: {self.__js} ")


class WebPageDecorator(WebPage):

    def __init__(self, web_page):
        self.__web_page = web_page

    def display(self):
        self.__web_page.display()


class AuthenticatedWebPage(WebPageDecorator):

    def display(self):
        super().display()
        print("Autenticando página")


class AuthorizedWebPage(WebPageDecorator):

    def display(self):
        super().display()
        print("Autorizando página")


def test():
    webpage = BasicWebPage('body', 'css', 'js')
    authenticated_webpage = AuthenticatedWebPage(webpage)
    authorized_webpage = AuthorizedWebPage(authenticated_webpage)
    authorized_webpage.display()
    