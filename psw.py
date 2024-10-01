senha = 12345
sn = int(input('Digite a senha: '))
while sn != senha:
    print('Reemissão solicitada, senha incorreta.')
    sn = int(input('Digite a senha: '))
if sn == senha:
    print('Acesso garantido.')
