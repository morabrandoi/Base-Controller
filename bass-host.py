import socket
import time
import json
from enums import Buttons, Sticks

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 6543  # Port to listen on


def get_tilt_stick_params(stick, x=50, y=50, tilted=0.1, released=0.1, block=True):
    return {
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


def get_press_buttons_params(buttons, down=0.1, up=0.1, block=True):
    return {
        "action": "press_buttons",
        "args": {"buttons": buttons, "down": down, "up": up, "block": block},
    }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Example usage
    time.sleep(1)
    message = get_tilt_stick_params(
        stick=Sticks.LEFT_STICK, x=100, y=0, tilted=0.5, released=0.1
    )
    s.sendall(json.dumps(message).encode())
    time.sleep(1)
