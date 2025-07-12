# Real-Time Group Chat Room with Python: Client-Server Application
#### Video Demo:  : https://youtu.be/pIo0wy9_AH0
#### Description:
This project implements a chat room where multiple clients can communicate in real-time. The server manages chat rooms, allowing clients to create or join existing rooms by specifying their username and room name. Users in a chat room can see who is sending the chat and receive notifications when new members join. The server broadcasts messages to all members in the room. The application uses Python's socket programming and threading to handle multiple clients concurrently to provide an efficient user experience.

## Features

- **Create or Join Chat Rooms**: Clients can either create a new chat room or join an existing one by specifying a room name.
- **Real-Time Messaging**: Messages sent by clients are broadcasted to all members in the chat room.
- **User Notifications**: Clients receive notifications when new users join the chat room.
- **User Management**: Clients are prompted to enter a username and can see a list of members in their chat room.

## How to Run

1. **Start the Server:**
   - Save the server code in a file named `server.py`.
   - Open a terminal, navigate to the directory containing `server.py`, and run:
     ```bash
     python server.py
     ```
   - The server will start and listen for incoming client connections.

2. **Start a Client:**
   - Save the client code in a file named `client.py`.
   - Open a terminal, navigate to the directory containing `client.py`, and run:
     ```bash
     python client.py
     ```
   - Follow the prompts to enter your username and chat room name.

3. **Multiple Clients:**
   - You can run multiple instances of the client to simulate different users joining the same or different chat rooms.

## Code Explanation

### Server (`server.py`)

- **`handle_client(client_socket, client_address)`**: Manages interactions with a single client, handles joining rooms, and broadcasts messages.
- **`broadcast(message, chat_room_name, username, sender_socket)`**: Sends messages to all clients in a specified chat room, except the sender.
- **`start_server()`**: Initializes the server, listens for incoming connections, and spawns threads to handle clients.

### Client (`client.py`)

- **`receive_messages(client_socket)`**: Receives and prints messages from the server.
- **`send_messages(client_socket)`**: Reads user input and sends messages to the server.
- **`start_client()`**: Initializes the client, connects to the server, and starts threads for sending and receiving messages.

