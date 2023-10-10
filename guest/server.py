# THIS IS THE GUEST MACHINE CODE

import socket
import nxbt
import json

HOST = "0.0.0.0"  # VirtualBox's default gateway IP for the host machine when using NAT networking
PORT = 6543  # Same port as used by the server

nx = nxbt.Nxbt()
switch_addresses = nx.get_switch_addresses()

# prompt for controller
if (
    len(switch_addresses) == 0
    or input("Are you connecting to a new Switch? (y/N): ").lower() == "y"
):
    print("Please be on 'Change Grip/Order' screen on Switch")
    controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
else:
    controller_index = nx.create_controller(
        nxbt.PRO_CONTROLLER, reconnect_address=switch_addresses
    )


print("Waiting to connect to Switch...")
nx.wait_for_connection(controller_index)
print("Connected To Switch. Starting server...")

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
                    args = parsed_data.get("args")

                    if action == "tilt_stick":
                        print("tilting stick now")
                        nx.tilt_stick(
                            controller_index,
                            args.get("stick"),
                            args.get("x"),
                            args.get("y"),
                            tilted=args.get("tilted"),
                            released=args.get("released"),
                            block=args.get("block"),
                        )
                    elif action == "press_buttons":
                        print("pressing buttons now")
                        nx.press_buttons(
                            controller_index,
                            args.get("buttons"),
                            down=args.get("down"),
                            up=args.get("up"),
                            block=args.get("block"),
                        )
                except json.JSONDecodeError:
                    print("Received invalid JSON:", data.decode("utf-8"))
                print("Received:", data.decode("utf-8"))

            print("Connection terminated. Waiting for a new connection...")
