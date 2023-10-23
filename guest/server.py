import socket
import nxbt
import json


class Actions:  # enum
    PRESS_BUTTONS = "press_buttons"
    TILT_STICK = "tilt_stick"


nx = nxbt.Nxbt()
switch_addresses = nx.get_switch_addresses()
already_connected = False


def initialize_nx(is_connected):
    if is_connected:
        return

    try:
        controller_index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            reconnect_address=switch_addresses,
        )

        if controller_index is None:
            raise Exception("No controller available from the list of addresses")
    except Exception:
        controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)

    nx.wait_for_connection(controller_index)
    return controller_index


HOST = "0.0.0.0"  # VirtualBox's default gateway IP for the host machine when using NAT networking
PORT = 6543  # Same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening for a connection...")

    while True:
        conn, addr = s.accept()

        if not already_connected:
            controller_index = initialize_nx(already_connected)
            already_connected = True

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

                    print(f"{action} args={args}", end="\n\n")

                    if action == Actions.TILT_STICK:
                        nx.tilt_stick(
                            controller_index,
                            args.get("stick"),
                            args.get("x"),
                            args.get("y"),
                            tilted=args.get("tilted"),
                            released=args.get("released"),
                            block=args.get("block"),
                        )
                    elif action == Actions.PRESS_BUTTONS:
                        nx.press_buttons(
                            controller_index,
                            args.get("buttons"),
                            down=args.get("down"),
                            up=args.get("up"),
                            block=args.get("block"),
                        )
                except json.JSONDecodeError:
                    print("\n\n\n")
                    print("Received invalid JSON:", data.decode("utf-8"))
                    print("\n\n\n")

            print("Connection terminated. Waiting for a new connection...")
