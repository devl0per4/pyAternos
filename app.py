import os
Clear = lambda: os.system('cls')
Delay = lambda: input()
Console = lambda: input('$')
from python_aternos import *
atclient = Client()
servers = atclient.account.list_servers()
print('Please log in')
username = input('Username:')
password = input('Password:')
atclient.login(username, password)
servers = atclient.account.list_servers()
Clear()
if True:
    print('Enter number of server:')
    server_number = int(input('>>>'))
    server = servers[server_number]
    Clear()
    while True:
        qq = Console()
        if qq == 'change.Server':
            print('Enter number of server')
            server_number = input('>>>')
            server = servers[server_number]
            Clear()
        if qq == 'server.Start':
            print('Launching server', server_number)
            server.start()
            Clear()
        if qq == 'server.Stop':
            print('Stoping server', server_number)
            server.stop()
            Clear()
        if qq == 'exit':
            break
print('Connection was breaked.')
Delay()