import sys
from random import randint
import re


def titulo(msg):
    tamanho = len(msg) +2
    print('-'*tamanho)
    print(msg)
    print('-'*tamanho)

def valida_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Informe um numero inteiro válido.')
        else:
            return n

def valida_email(msg):
    padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        email = input(msg)
        if re.fullmatch(padrao, email):
            return email
        else:
            print('E-mail inválido!')

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_produtos = []
        self.lista_de_clientes = []

    def exibir_catalogo(self):
        titulo(f'{'PRODUTO':<26} {'PREÇO':>17} {'ESTOQUE':>15} {'CATEGORIA':>14}')
        for produto in self.lista_de_produtos:
            print(produto)

    def filtrar_categoria(self, categoria):
        for produto in self.lista_de_produtos:
            if produto.categoria == categoria:
                print(produto)

class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria

    def __str__(self):
        return f'''{self.nome:<28} {f'{self.preco},00R$':>15} {f'{self.estoque:2} unidades':^20} {self.categoria:<2}'''

class Cliente:
    def __init__(self, nome, id_de_usuario, endereco, email):
        self.nome = nome
        self.id_de_usuario = id_de_usuario
        self.endereco = endereco
        self.email = email
        self.carrinho = CarrinhoDeCompras()

    def adicionar_produto(self, nome):
        self.carrinho.adicionar_produto(nome)

    def exibir_carrinho(self):
        self.carrinho.exibir_carrinho()

    def remover_produto(self, nome):
        self.carrinho.remover_produto(nome)

    def alterar_quantidade(self, nome, opcao):
        self.carrinho.alterar_quantidade(nome, opcao)

    def finalizar_compra(self):
        self.carrinho.finalizar_compra()


class CarrinhoDeCompras:
    produto_encontrado = False

    def __init__(self):
        self.lista_carrinho = []

    def exibir_carrinho(self):
        titulo('CARRINHO')
        if len(self.lista_carrinho) == 0:
            print('Seu carrinho está vazio.')
        for produto in self.lista_carrinho:
           print(f'{produto.nome}, {produto.preco}R$, Categoria: {produto.categoria}')
        print()

    def adicionar_produto(self, nome):
        quantidade = valida_int('Qual a quantidade? ')
        for produto in loja.lista_de_produtos:
            if produto.nome == nome:
                CarrinhoDeCompras.produto_encontrado = True
                if produto.estoque >= quantidade:
                    for c in range(quantidade):
                        self.lista_carrinho.append(produto)
                    print(f'{quantidade} unidade(s) de {produto.nome} adicionado(s) ao carrinho com sucesso!')
                    produto.estoque -= quantidade
                else:
                    print('ERRO! Quantidade maior que o estoque disponível.')
        if not CarrinhoDeCompras.produto_encontrado:
            print('ERRO! Produto não encontrado.')

    def remover_produto(self, nome):
        for produto in self.lista_carrinho[:]:  # Usar uma cópia da lista para iterar
            if nome in produto.nome:
                CarrinhoDeCompras.produto_encontrado = True
                self.lista_carrinho.remove(produto)
                print(f'{produto.nome} removido do carrinho com sucesso!')
                produto.estoque += 1  # Atualiza o estoque do produto

        if not CarrinhoDeCompras.produto_encontrado:
            print('ERRO! Produto não encontrado')

    def alterar_quantidade(self, nome, opcao):
        for produto in self.lista_carrinho:
            if produto.nome == nome:
                CarrinhoDeCompras.produto_encontrado = True

        if CarrinhoDeCompras.produto_encontrado:
            quantidade = valida_int('Quantidade: ')
            if opcao == 'A':
                for produto in self.lista_carrinho[:]:
                    quantidade -= 1
                    if produto.nome == nome:
                        self.lista_carrinho.append(produto)
                    if quantidade == 0:
                        break
            if opcao == 'D':
                for produto in self.lista_carrinho[:]:
                    quantidade -= 1
                    if produto.nome == nome:
                        self.lista_carrinho.remove(produto)
                    if quantidade == 0:
                        break
        else:
            print('ERRO! Produto não encontrado')

    def verificar_total(self):
        total_compra = 0
        for produto in self.lista_carrinho:
            total_compra += produto.preco
        return total_compra

    def finalizar_compra(self):
        valor_da_compra = CarrinhoDeCompras.verificar_total(self)
        print(f'O valor da compra é {valor_da_compra},00R$. Volte sempre!')
        sys.exit()

# cliente = Cliente('Zezin', 123, 'Rua passa nada', 'zezin@hotmail.com')

def main():
    while True: # cadastro do cliente
        titulo(f'{loja.nome} - CADASTRO'.center(75))
        print('CADASTRO')
        nome = str(input('Nome: '))
        endereco = str(input('Endereco: '))
        email = valida_email('E-mail: ')
        usuario_id = randint(1000, 5000)
        cliente = Cliente(nome, usuario_id, endereco, email, )
        break

    while True: # menu
        titulo(f'{loja.nome} - CATALOGO'.center(75))
        loja.exibir_catalogo()
        opcao = valida_int('''
[1] ADICIONAR AO CARRINHO
[2] REMOVER DO CARRINHO
[3] VER CARRINHO
[4] ALTERAR QUANTIDADE
[5] FINALIZAR COMPRA 
> ''')
        if opcao == 1 or opcao == 2 or opcao == 4:
            nome_do_produto = input('Informe o nome do produto: ').strip().capitalize()
            if opcao == 1:
                cliente.adicionar_produto(nome_do_produto)
            elif opcao ==2:
                cliente.remover_produto(nome_do_produto)
            elif opcao == 4:
                res = str(input('Deseja (A)umentar ou (D)iminiuir? ')).strip().upper()[0]
                cliente.alterar_quantidade(nome_do_produto, res)

        elif opcao == 3:
            cliente.exibir_carrinho()

        elif opcao == 5:
            cliente.finalizar_compra()

        else:
            print('Informe uma opção válida(tente um número entre 1 e 5).')

if __name__ == '__main__':
    loja = Loja('AMAZONIA')
    produto1 = Produto('Celular', 1200, 5, 'Eletronico')
    produto2 = Produto('Tv', 4000, 10, 'Eletronico')
    produto3 = Produto('Sabão', 25, 10, 'Limpeza')
    produto4 = Produto('Mesa', 300, 20, 'Alimenticio')
    loja.lista_de_produtos.extend([produto1, produto2, produto3, produto4])
    main()