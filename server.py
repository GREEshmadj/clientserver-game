import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server.bind(("0.0.0.0", 5000))


server.listen(5) 
print("Server started. Waiting for connections...")


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed by {client_address}")
                break

            # Decode and print the message
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")

            # Send a response back to the client
            response = f"Server received: {message}"
            client_socket.send(response.encode('utf-8'))

        except Exception as e:
            print(f"Error with client {client_address}: {e}")
            break

    client_socket.close()

# Main loop to accept connections
while True:
    try:
        # Accept a new client connection
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")

       
        handle_client(client_socket, client_address)

    except KeyboardInterrupt:
        print("\nServer shutting down.")
        server.close()
        break
    except Exception as e:
        print(f"Server error: {e}")
