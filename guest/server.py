# THIS IS THE GUEST MACHINE CODE

import socket
import nxbt
import json

HOST = "0.0.0.0"  # VirtualBox's default gateway IP for the host machine when using NAT networking
PORT = 6543  # Same port as used by the server

nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
print("Waiting to connect to Switch...")
nx.wait_for_connection(controller_index)
print("Connected To Switch starting server...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening for a connection...")

    while True:
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    # Decode the data to string and parse JSON
                    parsed_data = json.loads(data.decode("utf-8"))
                    action = parsed_data.get("action")
                    args = parsed_data.get("args", {})

                    if action == "tilt_stick":
                        nx.tilt_stick(
                            controller_index,
                            args.get("stick", ""),
                            args.get("x", 0),
                            args.get("y", 0),
                            tilted=args.get("tilted", 0.1),
                            released=args.get("released", 0.1),
                            block=args.get("block", True),
                        )
                    elif action == "press_buttons":
                        nx.press_buttons(
                            controller_index,
                            args.get("buttons", []),
                            down=args.get("down", 0.1),
                            up=args.get("up", 0.1),
                            block=args.get("block", True),
                        )
                except json.JSONDecodeError:
                    print("Received invalid JSON:", data.decode("utf-8"))
                print("Received:", data.decode("utf-8"))

            print("Connection terminated. Waiting for a new connection...")
