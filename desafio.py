"""
Desafio:

Comercio Padaria
1- O programa tem que rodar em loop infinito até ser parado
x 2- Cliente pedir um tipo de pão (Frances, doce, forma, australiano)
x 3- cada pão vai ter uma quantidade
x 4- valor do pão
 5- pedir forma de pagamento (dinheiro, cartão)
6- forma de entrega
7- dados do cliente (Se for entregar)
8- valor do frete por bairro
X 9- nome do atendente
10- codigo de entrega
"""
pao_frances = "Frances"
pao_doce = "Doce"
pao_forma = "Forma"
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

#Nome da atendente
atendente = "Maria"

#Bairos
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

frete_barroco = 5.00
frete_sao_jose = 15.00

#Codigo de vendas

codigo_venda = 98568


print("Inicializando o sistema...")
while True: 
    print(f" =========== Novo Pedido ===========")
    escolha = input(f"Bem vindo, sou a atendente {atendente}")
    #Tipo de pão
    input("Qual o seu pedido: {pao_frances, pao_doce, pao_forma}  ")
    if escolha == pao_frances:
        quantidade = int(input("Qual a quantidade?"))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            print(f"Seu pedido ficou em R${quantidade * valor_frances}")
        else:
            print(f" Infelismente só tenho {quantidade_frances} pães no momento.")
            break
            
    forma_retirada = input("É para 1:retirar ou 2:entregar? ")
    if forma_retirada == "2":
        bairro_entrega = input(f"Qual o bairro? (1:{bairro_barroco}, 2:{bairro_sao_jose})")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
        elif bairro_entrega == "2":
            valor_frete = frete_sao_jose
            print(f"Valor do frete R${valor_frete}")
        else:
            print("Fora da area de entrega")
            break
    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Informe seu nome:  ")
    forma_de_pagamento = input("Escolha a forma de pagamento (1-dinheiro, 2-cartao): ")
    if forma_de_pagamento == "1":
        froma_de_pagamento = "Dinheiro"
    else:
        forma_de_pagamento = "Cartão"

    codigo_atual = codigo_venda +1

    print(f"O valor total da sua compra foi de R$(valor_compra + valor_frete). ")
    break
