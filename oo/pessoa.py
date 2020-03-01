class Pessoa:
    # atributo de classe ou default
    olhos = 2

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
    eduardo.olhos = 1
    del eduardo.olhos
    print(eduardo.__dict__)
    print(aline.__dict__)

    print(f'Qtd. de olhos: {Pessoa.olhos}')
    print(f'Nome: {eduardo.nome} Qtd. de olhos: {eduardo.olhos}')
    print(f'Nome: {aline.nome} Qtd. de olhos: {aline.olhos}')
    print(id(Pessoa.olhos), id(eduardo.olhos), id(aline.olhos))
