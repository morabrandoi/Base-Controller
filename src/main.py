import socket
from switch_socket import SwitchSocket
from bass_detect import frequency_to_note, BassPitchDetector
from constants import SocketConstants, AudioConstants


def note_to_action(note) -> dict | None:
    if note not in SocketConstants.NOTE_TO_ACTION:
        return None

    return SocketConstants.NOTE_TO_ACTION[note]


def main():
    with SwitchSocket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        def on_pitch_detect(pitch):
            pitch *= AudioConstants.PITCH_CORRECTION_FACTOR
            note = frequency_to_note(pitch)
            if note:
                actionDict = note_to_action(note)

                if actionDict:
                    action, args = actionDict["action"], actionDict["args"]
                    print(pitch, note, action)
                    sock.send_action(action, args)
                else:
                    print("Invalid note")

        sock.connect((SocketConstants.HOST, SocketConstants.PORT))
        detector = BassPitchDetector(on_pitch_detect)
        detector.start()


# dunder main idiom
if __name__ == "__main__":
    main()
