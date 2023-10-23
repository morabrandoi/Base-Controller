import socket
from switch_socket import SwitchSocket
from bass_detect import frequency_to_note, BassPitchDetector
from constants import SocketConstants


def note_to_action(note) -> dict | None:
    if note not in SocketConstants.NOTE_TO_ACTION:
        return None

    return SocketConstants.NOTE_TO_ACTION[note]


def main():
    with SwitchSocket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        def on_pitch_detect(pitch):
            print(pitch)
            note = frequency_to_note(pitch)
            print(note)
            if note:
                actionDict = note_to_action(note)

                if actionDict:
                    action, args = actionDict["action"], actionDict["args"]
                    print(action)
                    print(args)
                    sock.send_action(action, args)
                else:
                    print("Invalid note")

        detector = BassPitchDetector(on_pitch_detect)
        detector.start()


# dunder main idiom
if __name__ == "__main__":
    main()
