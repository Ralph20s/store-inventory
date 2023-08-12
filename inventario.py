#Vitor Raphael Simões Bezerra - RM98253

inventario = {1:["Notebook", 3000.00, 5], 2:["Celular", 2500.00, 1], 3:["Camera", 15000.00, 1], 4:["Tv Lg", 6500.00, 1], 5:["Carregador", 90.00, 1]}

def add ():
    index = int(input("Entre com o codigo do produto: "))
    inventario[index] = [input("Entre com o nome: "), float(input("Entre com o valor: ")), int(input("Entre com a quantidade: "))]

def relatorio():
    for chave, valor in inventario.items():
        print("\nID............", chave)
        print("Nome............", valor [0])
        print("Valor...........", valor [1])
        print("QTD.............", valor [2])

def buscar():
    busca = input("Entre com o Nome: ")
    for chave, valor in inventario.items():
        if busca() == valor[0]():
            print("\nID............", chave)
            print("Nome............", valor [0])
            print("Valor...........", valor [1])
            print("QTD.............", valor [2])
            return
    print("Produto não foi encontrado! Lamentamos")

def remover():
    index = int(input("Qual o ID a ser removido: "))
    if index in inventario:
        del inventario[index]
        print("Produto removido com sucesso!")
    else:
        print("ID não encontrado!")

def alterar():
    index = int(input("Qual o ID a ser alterado: "))
    if index in inventario:
        inventario[index][2] = int(input("Entre com a quantidade: "))
        print("Quantidade alterada com sucesso!")
    else:
        print("ID não encontrado")

def depreciar():
    v_depreciar = float(input("Entre com a porcentagem que o produto foi depreciado: "))
    for chave, valor in inventario.items():
        depreciado = valor[1] - (valor[1] * (v_depreciar/100))
        print(f"O produto {valor[0]} teve a depreciação de {v_depreciar}% e atualizou o valor para R${depreciado}")

def menu():
    while True:
        print("\n===== Menu das nossas Opções =====")
        print("1 - Adicionar produto")
        print("2 - Relatório de inventário")
        print("3 - Buscar produto")
        print("4 - Remover produto")
        print("5 - Alterar quantidade")
        print("6 - Depreciar o valor em %")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            add()
        elif opcao == 2:
            relatorio()
        elif opcao == 3:
            buscar()
        elif opcao == 4:
            remover()
        elif opcao == 5:
            alterar()
        elif opcao == 6:
            depreciar()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()