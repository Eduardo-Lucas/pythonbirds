class Pessoa:
    def __init__(self, *filhos, nome=None, idade=58):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    aline = Pessoa(nome='Aline', idade=24)
    eduardo = Pessoa(aline, nome='Eduardo')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(eduardo.cumprimentar())
    print(f'Nome: {eduardo.nome}')
    print(f'Idade: {eduardo.idade}')

    for filho in eduardo.filhos:
        print(f'Filhos: [{filho.nome}, ]')

    eduardo.sobrenome = 'Lucas'
    del eduardo.sobrenome
    print(eduardo.__dict__)
    print(aline.__dict__)
