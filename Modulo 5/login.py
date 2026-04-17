usuarios = {
    "vini": "1234",
    "maria": "5678",
    "joao": "abcd"
}


def login(usuario, senha):
    # Verificamos se o usuário existe E se a senha dele confere
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

print("Bem-vindo ao sistema de login!")

user = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if login(user, senha):
    print("Seja bem vindo!")
else:
    print("Acesso negado. Tente novamente.")
    
