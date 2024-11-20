import socket
import threading



host = '127.0.0.1'
port = 9644

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

def receive_messages(clientSocket):
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

name = clientSocket.recv(1024).decode('utf-8')
print(name)

clientName = input("Enter your name: ")
clientSocket.send(clientName.encode('utf-8'))


receive_thread = threading.Thread(target=receive_messages, args=(clientSocket,))
receive_thread.daemon = True  
receive_thread.start()

while True:
    msg = input(f"{clientName}: ")
    if msg.lower() == 'exit':
        clientSocket.send("EXIT".encode('utf-8'))
        break
    
    else:
        clientSocket.send(msg.encode('utf-8'))

clientSocket.close()
