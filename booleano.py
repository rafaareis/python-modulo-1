print("--5.2 Definição--")

verdadeiro = True
print(verdadeiro)
print(type(verdadeiro))

falso = False
print(falso)
print(type(falso))

saldo_em_conta = 200
valor_do_saque = 100

pode_sacar = valor_do_saque <= saldo_em_conta
print(pode_sacar)

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar = codigo_de_seguranca_cadastro == codigo_de_seguranca
print(pode_efetuar)

print("--5.2 Operação--")

print(True | True)
print(False | False)
print(True | False)
print(False | True)

print("---------------------")

print(True & True)
print(False & False)
print(True & False)
print(False & True)

print("---------------------")

print(not True)
print(not False)

print("--5.3 Conversão--")

idade = 19
tipo_sangue = 'O-'
filhos = 0
telefone_fixo1 = None
telefone_fixo2 = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo1))
print(bool(telefone_fixo2))