import socket
import threading
import datetime
import os




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9644
server.bind((host, port))
server.listen(5)

print(f"Server started on {host}:{port}")
clients = []

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_message(message):
    try:
        
        logFilePath = os.path.join(os.path.expanduser('~'), 'Documents', 'chat_log.txt')
        
        with open(logFilePath, 'a', encoding='utf-8') as logFile:
            logFile.write(message + '\n')
    except Exception as e:
        print(f"Error logging message: {e}")


def handle_client(clientSocket, clientAddr):
    clientName = None  
    
    try:
        
        clientSocket.send("Please set your name:".encode('utf-8'))
        clientName = clientSocket.recv(1024).decode('utf-8')
        
        if not clientName:
            clientName = f"Guest{clientAddr[1]}"  

        print(f"Client {clientAddr} set their name as {clientName}")
        broadcast(f"{clientName} has joined the chat!", clientSocket)
    
        clients.append((clientSocket, clientName))
        
        while True:
            message = clientSocket.recv(1024).decode('utf-8')
            if message == 'EXIT':
                break
            else:
                timeStamp = get_timestamp()
                log_message(f"[{timeStamp}] {clientName} ({clientAddr[0]}): {message}")
                print(f"[{timeStamp}] Message from {clientName} ({clientAddr}): {message}")
                broadcast(f"[{timeStamp}] {clientName}: {message}", clientSocket)

    except Exception as e:
        
        print(f"Error with client {clientAddr}: {e}")
    
    finally:
        remove_client(clientSocket, clientName)
        clientSocket.close()

def broadcast(message, clientSocket):
    for client in clients:
        if client[0] != clientSocket: 
            try:
            
                client[0].send(message.encode('utf-8'))
            
            except Exception as e:
                print(f"Error sending message to client: {e}")
                continue


def remove_client(clientSocket, clientName):
    for client in clients:
        if client[0] == clientSocket:
            clients.remove(client)
            print(f"Client {clientName} has been removed.")
            broadcast(f"{clientName} has left the chat.", clientSocket)
            break


def server_send_message():
    while True:
        serverMsg = input("Server: ")
        
        if serverMsg.lower() == 'exit':
            break
        
        timeStamp = get_timestamp()
        msgWTimestamp = f"[{timeStamp}] Server: {serverMsg}"
        log_message(msgWTimestamp)  
        broadcast(msgWTimestamp, None)  




serverThread = threading.Thread(target=server_send_message)
serverThread.daemon = True
serverThread.start()


while True:
    clientSocket, clientAddr = server.accept()
    print(f"Connection established with {clientAddr}")
    
    client_thread = threading.Thread(target=handle_client, args=(clientSocket, clientAddr))
    client_thread.start()
