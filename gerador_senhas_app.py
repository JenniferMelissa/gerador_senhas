import secrets

while True:
    confirma = input('Gerar senha (s/n)? ').lower()

    if confirma == 's':
        print(secrets.token_urlsafe(16))    #16 é bites que a senha vai ter, é bem segura
        continue
    else:
        print('Programa encerrado.')
        break