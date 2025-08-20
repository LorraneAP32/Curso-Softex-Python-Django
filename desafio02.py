# Desafio: Comércio Padaria
print("Inicializando o sistema...")

while True:
    print("\n==== Novo Pedido ====")

    # 1) tipo de pão
    tipo_pao = input("Escolha o tipo de pão (frances, doce, forma, australiano): ").strip().lower()

    # 2) quantidade
    qtd = int(input("Quantidade: "))

    # 3) valor do pão (unitário)
    valor_unit = float(input("Valor unitário do pão (ex.: 5.50): "))
    subtotal = qtd * valor_unit

    # 4) forma de pagamento
    forma_pag = input("Forma de pagamento (dinheiro/cartao): ").strip().lower()
    if forma_pag not in ("dinheiro", "cartao"):
        print("Forma de pagamento inválida.")
        print("Finalizando o sistema...")
        break

    # 5) forma de entrega
    forma_entrega = input("Forma de entrega (retirada/entrega): ").strip().lower()

    # 6) dados do cliente (se for entrega) + frete por bairro
    frete = 0.0
    nome_cliente = ""
    bairro = ""
    if forma_entrega == "entrega":
        nome_cliente = input("Nome do cliente: ").strip()
        bairro = input("Bairro: ").strip()
        frete = float(input(f"Valor do frete para {bairro}: "))

    # 7) nome do atendente
    atendente = input("Nome do atendente: ").strip()

    # 8) código de entrega
    codigo_entrega = input("Código de entrega: ").strip()

    total = subtotal + frete

    # Resumo (estilo do exemplo)
    print("\n--- Resumo do Pedido ---")
    print(f"Pão: {tipo_pao} | Quantidade: {qtd} | Valor unitário: R$ {valor_unit:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Forma de pagamento: {forma_pag}")
    print(f"Forma de entrega: {forma_entrega}")
    if forma_entrega == "entrega":
        print(f"Cliente: {nome_cliente} | Bairro: {bairro}")
        print(f"Frete: R$ {frete:.2f}")
    print(f"Atendente: {atendente}")
    print(f"Código de entrega: {codigo_entrega}")
    print(f"TOTAL: R$ {total:.2f}")

    # Pergunta se continua (loop infinito até você parar)
    continuar = input("\nCadastrar outro pedido? (sim/nao): ").strip().lower()
    if continuar == "nao":
        print("Finalizando o sistema...")
        break