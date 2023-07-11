print('--4.2 Definição--')

nome_aula = "Aula 04, Módulo 01, Strings"
print(nome_aula)
print(type(nome_aula))

string_vazia = ""
print(string_vazia)
print(type(string_vazia))

print('--4.3 Operações--')
print('--4.3.1 Concatenação--')
nome = "Courtney"
sobrenome = "LaPlante"
banda = 'Spiritbox'

apresentacao = "Olá, o meu nome é " + nome + sobrenome + ". Eu sou vocalista da banda " + banda + "."
print(apresentacao)

print('--4.3.2 Concatenação Filtrada--')
nome = "Tatiana"
sobrenome = "Shmayliuk"
banda = 'Jinjer'

apresentacao = f'Olá, o meu nome é {nome} {sobrenome}. Eu sou vocalista da banda {banda} .'
print(apresentacao)

print('--4.3.3 Fatiamento (Slicing)--')

email = "rafa_alvarenga@msn.com"

print('0' + email[0])
print('11' + email[11])

print('-1' + email[-1])
print('-2' + email[-2])

print('--4.3.3.1 E-mail--')

email_usuario = email[0:14]
print(email_usuario)

email_provedor = email[14:23]
print(email_provedor)

print('--4.4 Métodos--')

endereco = 'Avenida Salmão, 300, Parque Residencial Aquarius, São José dos Campos, São Paulo, Brasil'
print(endereco.upper())

posicao = endereco.find('André')
print(posicao)

print(endereco.replace('Avenida', 'Av.' ))
print(endereco.replace('São Paulo', 'SP'))
print(endereco.replace('Brasil', 'BR'))

print('--4.5 Conversão--')

idade = 19
print(idade)
print(type(idade))

idade = str(idade)
print(idade)
print(type(idade))

faturamento = 'R$ 35 mi'
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))