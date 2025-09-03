acessos = [
    ("Pedro", "sucesso"),
    ("Ana", "falha"),
    ("Maria", "sucesso"),
    ("Pedro", "falha"),
    ("Ana", "falha")
]

usuarios_sucesso = set()
usuarios_falha = set()

for usuario, status in acessos:
    if status == "sucesso":
        usuarios_sucesso.add(usuario)
    else:
        usuarios_falha.add(usuario)


usuarios_somente_falha = usuarios_falha - usuarios_sucesso

print("Usuários com pelo menos um login bem-sucedido:", usuarios_sucesso)
print("Usuários que tiveram somente logins com falha:", usuarios_somente_falha)


