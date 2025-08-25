
preco_hamburguer = 18.00
cupom_valido = "DESCONTO10"
desconto = 0.10

produto = ""
while produto != "hamburguer":
    produto = input("Digite o nome do produto: ").strip().lower()
    if produto != "hamburguer":
        print("Produto não disponível. Tente novamente.")

tem_cupom = input("Você tem um cupom de desconto? (s/n): ").strip().lower()

preco_final = preco_hamburguer
if tem_cupom == "s":
    codigo = input("Digite o código do cupom: ").strip().upper()
    if codigo == cupom_valido:
        preco_final = preco_hamburguer * (1 - desconto)
        print("Cupom aplicado com sucesso!")
    else:
        print("Cupom inválido. Sem desconto.")

print(f"Total a pagar: R$ {preco_final:.2f}")
print("Pedido finalizado. Obrigado pela preferência!")          
