from socket import *
import random
import hashlib

ip = "127.0.0.1"
porta = 777

conexao = socket(AF_INET, SOCK_STREAM)
conexao.bind((ip, porta))
conexao.listen(2)

print("Aguardando conexão com o cliente....")
while True:
    g=9
    p=1001
    a=5
    b=3
    A = (g**a) % p
    B = (g**b) % p
    keyB=(A**b) % p
    KeyB_hash = hashlib.sha256(str(keyB).encode()).hexdigest()
    con, cliente = conexao.accept()
    print("Conectado a", cliente)
    while True:
        msg_recebida = con.recv(1024)
        print("KeyA:", msg_recebida.decode())
        print("KeyB:", KeyB_hash)
        json_value = {
            'keyA' : msg_recebida.decode(),
            'keyB': KeyB_hash,
            'b' : b
        }
        msg_enviada = f'Conexao recebida com sucesso, 200, keyA: {msg_recebida.decode()}, keyB: {KeyB_hash}, b: {b}' 
        con.send(str(json_value).encode())
        break
    con.close
