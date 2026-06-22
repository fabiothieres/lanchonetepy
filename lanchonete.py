cardapio = {
    "x-bacon": 25.00,
    "x-burger": 20.00,
    "x-egg": 22.00,
    "refrigerante lata": 7.00,
    "água s/ gás": 5.00
}

lista_lanches = list(cardapio.keys())

pedidos = []
comanda = 0

print('=======================')
print('       Lanchonete      ')
print('=======================')
print('Olá, seja bem-vindo à nossa lanchonete!')


while True:
    print('\n1. Ver cardápio')
    print('2. Fazer pedido / Adicionar item')
    print('3. Remover item do pedido')
    print('4. Listar itens do pedido')
    print('5. Valor total do pedido')
    print('6. Cancelar operação\n')
    op = int(input('Digite o número da opção desejada:'))

    if op == 1:
        numero = 0
        for lanche in cardapio:
            print(f'{numero}. {lanche}: {cardapio[lanche]}')
            numero += 1
    elif op == 2:
        ped = int(input('Qual o número do item? '))
        lanche_escolhido = lista_lanches[ped]
        preco_do_lanche = cardapio[lanche_escolhido]
        pedidos.append(lanche_escolhido)
        comanda += preco_do_lanche
    elif op == 3:
        if len(pedidos) == 0:
            print('O carrinho está vazio! Não há nada à ser removido.')
        else:
            for i in range(len(pedidos)):
                print(f'{i}. {pedidos[i]}')
            rem = int(input('Deseja remover qual item? '))
            lanche_removido = pedidos.pop(rem)
            comanda -= cardapio[lanche_removido]
    elif op == 4:
        print('Pedidos: ')
        for i in range(len(pedidos)):
            print(pedidos[i])
    elif op == 5:
        print(f'Valor total do pedido: {comanda}')
    elif op == 6:
        print('\nAté mais! ')
        break
    else:
        print('Opção inválida! Digite um número de 1 a 6.')




print('\nDesenvolvido por: Fabio Thieres')
print('Github: fabiothieres')
print('LinkedIn: Fabio Thieres')
