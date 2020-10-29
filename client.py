from socket import *
import random
import hashlib

ip = "127.0.0.1"
porta = 777

g=9
p=1001
a=5
b=3
A = (g**a) % p
B = (g**b) % p
keyA=(B**a) % p
keyB=(A**b) % p

KeyA_hash = hashlib.sha256(str(keyA).encode()).hexdigest()
msg = KeyA_hash.encode()

conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((ip, porta))
conexao.send(msg)
resposta = conexao.recv(1024)
print(resposta.decode())
conexao.close
