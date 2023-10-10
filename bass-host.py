import socket
import time
import json
from enums import Buttons, Sticks, Actions

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 6543  # Port to listen on


def get_tilt_stick_params(stick, x=50, y=50, tilted=0.1, released=0.1, block=True):
    return {
        "action": Actions.TILT_STICK,
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
        "action": Actions.PRESS_BUTTONS,
        "args": {"buttons": buttons, "down": down, "up": up, "block": block},
    }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Example usage
    time.sleep(10)
    message = get_tilt_stick_params(
        stick=Sticks.LEFT_STICK, x=100, y=0, tilted=0.5, released=0.1
    )
    s.sendall(json.dumps(message).encode())
    time.sleep(4)
    print("MOVING RIGHT HERE")
    message = get_tilt_stick_params(
        stick=Sticks.LEFT_STICK, x=-100, y=0, tilted=0.5, released=0.1
    )
    s.sendall(json.dumps(message).encode())
