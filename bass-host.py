import socket
import time
import json

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 6543  # Port to listen on


def send_tilt_stick(
    s, stick="left", x=0.5, y=0.5, tilted=0.1, released=0.1, block=True
):
    message = {
        "action": "tilt_stick",
        "args": {
            "stick": stick,
            "x": x,
            "y": y,
            "tilted": tilted,
            "released": released,
            "block": block,
        },
    }
    s.sendall(json.dumps(message).encode())


def send_press_buttons(s, buttons=["A"], down=0.1, up=0.1, block=True):
    message = {
        "action": "press_buttons",
        "args": {"buttons": buttons, "down": down, "up": up, "block": block},
    }
    s.sendall(json.dumps(message).encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Example usage
    send_tilt_stick(s, x=0.6, y=0.4)
    time.sleep(3)
    send_press_buttons(s, buttons=["B", "X"])
    time.sleep(3)
    s.sendall(b"Hello from VM!")
