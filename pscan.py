import socket

ip = input('digite o host ou ip a ser verificado: ')

ports = []
count = 0

while count <10:
    ports.append(int(input('digite a porta a ser verificada: ')))
    count +=1


for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print(str(port), 'porta aberta')
    else:
        print(str(port), 'porta fechada')

print('Scan finalizado.')