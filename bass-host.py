import socket

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 65432  # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening for a connection...")
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Process the data received from the VM here
            print("Received:", data.decode("utf-8"))
