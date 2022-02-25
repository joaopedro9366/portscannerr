import nmap

scanner = nmap.PortScanner

print('Seja bem vindo ao DIOScanner')
print('<--------------------------->')

ip = input('digite o ip a ser varrido: ')
print('o ip digitado foi: ', ip)
type(ip)

menu = (input("""\n escolha o tipo de varredura a ser realizada
                1 -> varredura do tipo SYN
                2 -> varredura do tipo UDP
                3 -> varredura do tipo intensa
                digite a opçao escolhida: """))
print('a opçao escolhida foi: ', menu)

if menu == "1":
    print('versao do nmap: ', scanner.nmap_version)
    scanner.scan(ip, "1-1024", '-V -sS')
    print(scanner.scaninfo())
    print('Status do IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print('portas abertas: ', scanner[ip]['tcp'].keys())
elif menu == '2':
    print('Versao do nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('status do  IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('portas abertas: ', scanner[ip]['udp'].keys())
elif menu =='3':
    print('Versao do nmap: ', scanner.nmap_version)
    scanner.scan(ip, '1-1024', '-v -sC')
    print('status do IP: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('portas abertas: ', scanner[ip]['tcp'].keys())
else:
    print('EScolha uma opçao correta')