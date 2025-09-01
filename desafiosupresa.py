ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
ladoC = float(input("Digite o valor do lado C: "))

if ladoA > 0 and ladoB > 0 and ladoC > 0:
    condicao_soma = (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB)
    condicao_diferenca = (ladoA > abs(ladoB - ladoC)) and (ladoB > abs(ladoA - ladoC)) and (ladoC > abs(ladoA - ladoB))

    if condicao_soma and condicao_diferenca:
        print("Os lados formam um triângulo!")
    else:
        print("Os lados NÃO formam um triângulo.")
else:
    print("Erro: todos os lados devem ser positivos.")

