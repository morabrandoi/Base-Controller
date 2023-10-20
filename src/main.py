import socket
from switch_socket import SwitchSocket
from constants import SocketConstants


def frequency_to_action(frequency):
    for (start, end), button in SocketConstants.PITCH_TO_ACTION:
        if start <= frequency <= end:
            return button
    return None


def main():
    with SwitchSocket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        def on_pitch_detect(pitch):
            pass


# dunder main idiom
if __name__ == "__main__":
    main()
