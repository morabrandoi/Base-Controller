import socket
import json
from typing import List
from enums import Stick, Action, Button


class SwitchSocket(socket.socket):
    def send_stick_tilt(
        self, stick: Stick, x=50, y=50, tilted=0.1, released=0.1, block=True
    ):
        self._send_message(
            {
                "action": Action.TILT_STICK,
                "args": {
                    "stick": stick,
                    "x": x,
                    "y": y,
                    "tilted": tilted,
                    "released": released,
                    "block": block,
                },
            }
        )

    def send_press_buttons(self, buttons: List[Button], down=0.1, up=0.1, block=True):
        self._send_message(
            {
                "action": Action.PRESS_BUTTONS,
                "args": {"buttons": buttons, "down": down, "up": up, "block": block},
            }
        )

    def _send_message(self, message):
        self.sendall(json.dumps(message).encode())
