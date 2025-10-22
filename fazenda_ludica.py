
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"


class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"


class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros 

    def emitir_som(self):
        return "Muuu!"

    # Getter
    def obter_producao_leite(self):
        return self.__producao_leite_litros

    # Setter
    def registrar_ordenha(self, litros):
        self.__producao_leite_litros = litros


if __name__ == "__main__":
    cachorro = Cachorro("Rex", 3, "Labrador")
    gato = Gato("Mimi", 5, "Branco")
    vaca = Vaca("Mimosa", 7, 25.5)

    print(cachorro.apresentar())
    print(gato.apresentar())
    print(vaca.apresentar())

    print(cachorro.emitir_som())
    print(gato.emitir_som())
    print(vaca.emitir_som())

    print("\nProdução atual de leite:", vaca.obter_producao_leite(), "litros")
    vaca.registrar_ordenha(28.0)
    print("Produção após ordenha:", vaca.obter_producao_leite(), "litros")