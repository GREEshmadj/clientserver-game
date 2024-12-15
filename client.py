import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = input("Enter the server IP address: ")  
server_port = 5000  

try:
    print(f"Connecting to server at {server_ip}:{server_port}...")
    client.connect((server_ip, server_port))
    print("Connected to the server!")

    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

    client.close()
    print("Disconnected from the server.")

except socket.timeout:
    print("Connection timed out. The server is not responding.")
except socket.error as e:
    print(f"Connection error: {e}")
