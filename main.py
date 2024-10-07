class Loja:
    def __init__(self):
        self.lista_de_produtos = []
        self.lista_de_clientes = []

    def exibir_catalogo(self):
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
        return f'''Nome: {self.nome}, {self.preco}R$, {self.estoque} unidade(s), Categoria: {self.categoria}'''

class Cliente:
    def __init__(self, nome, id_de_usuario, endereco, email):
        self.nome = nome
        self.id_de_usuario = id_de_usuario
        self.endereco = endereco
        self.email = email
        self.carrinho = CarrinhoDeCompras()

    def adicionar_produto(self, nome, quantidade):
        self.carrinho.adicionar_produto(nome, quantidade)

    def exibir_carrinho(self):
        self.carrinho.exibir_carrinho()

    def remover_produto(self, nome):
        self.carrinho.remover_produto(nome)

    def alterar_quantidade(self, nome, quantidade, opcao):
        self.carrinho.alterar_quantidade(nome, quantidade, opcao)

    def finalizar_compra(self):
        pass


class CarrinhoDeCompras:
    produto_encontrado = False

    def __init__(self):
        self.lista_carrinho = []

    def exibir_carrinho(self):
        print('CARRINHO')
        for produto in self.lista_carrinho:
           print(f'{produto.nome}, {produto.preco}R$, Categoria: {produto.categoria}')
        print()

    def adicionar_produto(self, nome, quantidade):
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
            if produto.nome == nome:
                CarrinhoDeCompras.produto_encontrado = True
                self.lista_carrinho.remove(produto)
                print(f'{produto.nome} removido do carrinho com sucesso!')
                produto.estoque += 1  # Atualiza o estoque do produto

        if not CarrinhoDeCompras.produto_encontrado:
            print('ERRO! Produto não encontrado')

    def alterar_quantidade(self, nome, quantidade, opcao):
        for produto in self.lista_carrinho:
            if produto.nome == nome:
                CarrinhoDeCompras.produto_encontrado = True

        if CarrinhoDeCompras.produto_encontrado:
            if opcao == 'Aumentar':
                CarrinhoDeCompras.adicionar_produto(self, nome, quantidade)
            if opcao == 'Diminuir':
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

    def gerenciar_estoque(self):
        pass

    def finalizar_compra(self):
        pass



loja = Loja()
produto1 = Produto('Celular', 1200, 5, 'Eletronico')
produto2 = Produto('Tv', 4000, 10, 'Eletronico')
produto3 = Produto('Sabão', 5, 10, 'Limpeza')
produto4 = Produto('Arroz', 10, 20, 'Alimenticio')
loja.lista_de_produtos.extend([produto1, produto2, produto3, produto4])
loja.exibir_catalogo()

cliente = Cliente('Zezin', 123, 'Rua passa nada', 'zezin@hotmail.com')
cliente.adicionar_produto('Sabão', 5)
# cliente.adicionar_produto('Celular', 3)
# cliente.adicionar_produto('Tv', 6)
cliente.exibir_carrinho()
# cliente.remover_produto('Sabão')

cliente.alterar_quantidade('Sabão', 2, 'Diminuir')
loja.exibir_catalogo()
cliente.exibir_carrinho()
