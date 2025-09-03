vendas = [
    ('Teclado', 50, 2),
    ('Mouse', 25.5, 4),
    ('Monitor', 300, 1),
    ('Fone', 45, 1),
    ('Webcam', 75.20, 2),
]

vendas_filtradas = []

for produto, valor, quantidade in vendas:
    if valor*quantidade >= 100:
        vendas_filtradas.append((produto, valor, quantidade))

produtos_unicos = set()
for produto, valor, quantidade in vendas:
    produtos_unicos.add(produto)

print('Venda filtrada (valor total) >=  100:', vendas_filtradas)
print('Produtos únicos: ', produtos_unicos) 
