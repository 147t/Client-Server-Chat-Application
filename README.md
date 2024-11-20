# Client-Server-Chat-Application

## Overview
This project is a simple chat server and client application built using Python's `socket` library. The system allows multiple clients to connect to the server, send and receive real-time messages, and allows the server to broadcast messages to all connected clients. The server logs all interactions with a timestamp, client name, and IP address, saving the chat history in a text file for later reference.

The chat application provides a straightforward interface for communication, including the ability for users to join, leave, and send messages in a multi-client environment. The server also enables broadcasting server-side messages to all clients.

## Features
- **Real-time Messaging**: Clients can send and receive messages in real-time, and the server broadcasts all messages to connected clients.
- **Client Name Setup**: Clients can set their own name upon connecting to the server. If no name is provided, a default name is assigned.
- **Server-side Broadcasting**: The server can send messages to all connected clients at once.
- **Message Logging**: All messages exchanged in the chat, along with timestamps, client names, and IP addresses, are logged in a text file located in the user's Documents folder.
- **Client Disconnection**: Clients can gracefully disconnect by typing `EXIT`.
- **Server Management**: The server can manually send messages to all clients and manage client connections.

## Technologies Used
- **Python3**
- **Version Control**: Git (for code versioning and collaboration)


