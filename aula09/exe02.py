estoque_principal = [
    ("Camiseta", 101),
    ("Calça", 102),
    ("Boné", 103),
    ("Tênis", 104)
]

estoque_online = [
    ("Boné", 103),
    ("Camisa Polo", 105),
    ("Calça", 102),
    ("Chinelo", 106)
]

set_principal = set(estoque_principal)
set_online = set(estoque_online)

print("Produtos disponíveis na loja e no site:", set_principal & set_online)
print("Produtos disponíveis apenas na loja física:", set_principal - set_online)
print("Produtos disponíveis apenas no site:", set_online - set_principal)

