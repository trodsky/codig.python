#Criando um dicionário para armazenar as informações do cliente
cliente = {}

#Solicitando as informações do cliente
cliente['nome'] = input("Digite o nome do cliente: ")
cliente['telefone'] = input("Digite o telefone do cliente: ")
cliente['email'] = input("Digite o email do cliente: ")

#Solicitando o serviço desejado pelo cliente
print("Serviços disponíveis:")
print("1. Corte de cabelo")
print("2. Pintura de cabelo")
print("3. Manicure")
print("4. Pedicure")
servico = int(input("Digite o número do serviço desejado: "))

#Verificando o serviço escolhido pelo cliente
if servico == 1:
    cliente['servico'] = 'Corte de cabelo'
    cliente['valor'] = 50.00
    if servico == 2:
        cliente['servico'] = 'Pintura de cabelo'
        cliente['valor'] = 120.00
        if servico == 3:
            cliente['servico'] = 'Manicure'
            cliente['valor'] = 30.00
            if servico == 4:
                cliente['servico'] = 'Pedicure'
                cliente['valor'] = 40.00
else:
    print("Opção inválida.")

#Informando o valor do serviço escolhido ao cliente
print("O valor do serviço escolhido é R$", cliente['valor'])

#Salvando as informações do cliente em um arquivo de texto
with open("clientes.txt", "a") as arquivo:
    arquivo.write(str(cliente) + "\n")

print("Cliente registrado com sucesso!")





