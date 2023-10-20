from enums import Stick, Action, Button


class AudioConstants:
    CHANNELS = 1
    RATE = 48000
    SAMPLE_PERIOD = 0.25

    DEVICE_NAME = "MIGHTY PLUG USB"
    FREQUENCY_MIN = 0  # lowest note on a bass guitar is E1 which is 41.2 Hz
    FREQUENCY_MAX = 392  # highest note on a bass guitar
    N_FTT_BINS = 2**12  # remember 2 ** 12 = 4096

    # derived constants
    CHUNK = round(SAMPLE_PERIOD * RATE)


# TODO: FINISH
# tuple is ((start, end), action, args)
class SocketConstants:
    HOST = "0.0.0.0"  # Listen on all available interfaces
    PORT = 6543  # Port to listen on
    PITCH_TO_ACTION = [
        {
            "start": 0,
            "end": 41.2,
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.E1],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        }((0, 41.2), "E1"),
        ((41.2, 82.4), "A1"),
        ((82.4, 123.5), "D2"),
        ((123.5, 164.8), "G2"),
        ((164.8, 206.0), "C3"),
        ((206.0, 247.0), "F3"),
        ((247.0, 288.3), "B3"),
        ((288.3, 329.6), "E4"),
        ((329.6, 370.8), "A4"),
        ((370.8, 392.0), "D5"),
    ]
