def dados() -> dict:
    """Carregar e retornar os dados de produtos, frete e funcionarios"""
    return{
        "atendente" : "Maria",
        "paes":{
            "frances":{"nome":"Pão frances", "Valor": 0.50,"Quantidade":15},
            "Daces":{"nome":"Pão doce", "Valor": 5.00,"Quantidade":20},
            "Forma":{"nome":"Pão de forma", "Valor": 5.99,"Quantidade":10},
        },
        "bairros":{ 
            "barroco":{"nome":"Barroco","Frete":5.00},
            "Sao jose": {"nome":"Sao jose", "Frete": 15.00},
        },
        "codigo_venda_base":95875
    }
def obter_dados_cliente() -> dict:
    """Solicita e retorna os dados do cliente"""
    nome = input("Informe seu nome:")
    return {"nome": nome}
def solicitar_forma_pagamento() -> str:
    """Solicitar e retornar a forma de pagamento escolhida"""
    while True:
        pagamento = input("Escolha a forma de pagamento(1-Dinehiro, 2-Cartao)")
        if pagamento =="1":
            return"Dinheiro"
        elif pagamento == "2":
            return "Cartao"
        else:
            print("Forma de pagamento invalida")

def gerar_codigo_venda(codigo_base:int) -> int:
    """Gera e retorna o codigo de venda"""
    return codigo_base + 1 

def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Calcular o valor com base no bairro de entrega"""
    print("Bairros para entrega")
    while True:
        for bairo in bairros_disponiveis.values():
            print(f" - {bairo["nome"]}")
            bairros_entrega_nome = input("Qual o bairro de entrega?").lower()
            bairro_encontrado = ""
            for chave, bairo in bairros_disponiveis.values():
                if bairo["nome"].lower() == bairros_entrega_nome:
                    bairro_encontrado = chave
                    break
            if not bairro_encontrado:
                print("Bairro fora da area de Entrega")
            else:
                frete = bairros_disponiveis[bairro_encontrado]["frete"]
                return bairros_entrega_nome, frete
            
def cadastrar_produto(estoque: dict) -> None:
    """Permite ao atendente cadastrar um novo produto"""
    nome_produto = input("Digite o nomer do produto: (identificador)").lower()

    if nome_produto in estoque:
        print("Erro! Produto já cadastrado")
        return

    try:
        nome_completo = input("Digite o nome completo do produto: ")
        valor = float (input("Digite o valor do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

    except ValueError:
        print("Erro! Valor ou quantidade inválidos.")
        return

        if nome_produto and valor > 0 and quantidade >= 0:
            estoque[nome_produto]= {
            "nome": nome_completo,
            "valor": valor,
            "quantidade": quantidade
        }

        print(f'Produto {nome_completo} cadastrado com sucesso!')

    else:
        print("Erro! Dados do produto inválidos.")

   

