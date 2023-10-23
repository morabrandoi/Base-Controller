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

    # uses nonlinear-bucketting (based on 12th root of 2)
    FREQ_TO_NOTE = [
        ((39.85, 42.22), "E1"),
        ((42.22, 44.73), "F1"),
        ((44.73, 47.39), "F#1"),
        ((47.39, 50.21), "G1"),
        ((50.21, 53.2), "G#1"),
        ((53.2, 56.36), "A1"),
        ((56.36, 59.72), "A#1"),
        ((59.72, 63.27), "B1"),
        ((63.27, 67.03), "C2"),
        ((67.03, 71.02), "C#2"),
        ((71.02, 75.24), "D1"),
        ((75.24, 79.72), "D#2"),
        ((79.72, 84.46), "E2"),
        ((84.46, 89.48), "F2"),
        ((89.48, 94.8), "F#2"),
        ((94.8, 100.44), "G2"),
        ((100.44, 106.41), "G#2"),
        ((106.41, 112.74), "A2"),
        ((112.74, 119.45), "A#2"),
        ((119.45, 126.55), "B2"),
        ((126.55, 134.08), "C3"),
        ((134.08, 142.05), "C#3"),
        ((142.05, 150.5), "D3"),
        ((150.5, 159.45), "D#3"),
        ((159.45, 168.93), "E3"),
        ((168.93, 178.98), "F3"),
        ((178.98, 189.62), "F#3"),
        ((189.62, 200.9), "G3"),
        ((200.9, 212.84), "G#3"),
        ((212.84, 225.5), "A3"),
        ((225.5, 238.91), "A#3"),
        ((238.91, 253.12), "B3"),
        ((253.12, 268.17), "C4"),
        ((268.17, 284.12), "C#4"),
        ((284.12, 301.01), "D4"),
        ((301.01, 318.91), "D#4"),
        ((318.91, 337.88), "E4"),
        ((337.88, 357.97), "F4"),
        ((357.97, 379.25), "F#4"),
        ((379.25, 401.81), "G4"),
    ]


class SocketConstants:
    HOST = "0.0.0.0"  # Listen on all available interfaces
    PORT = 6543  # Port to listen on
    NOTE_TO_ACTION = {
        "E1": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.L.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "F1": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.ZL.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "G1": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.ZR.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "G#1": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.R.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "A#1": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.LEFT_STICK.value,
                "x": -100,
                "y": 0,
                "tilted": 0.4,
                "block": True,
            },
        },
        "C2": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.LEFT_STICK.value,
                "x": 100,
                "y": 0,
                "tilted": 0.4,
                "block": True,
            },
        },
        "B1": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.L_STICK_PRESS.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "E2": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.LEFT_STICK.value,
                "x": 0,
                "y": 100,
                "tilted": 0.4,
                "block": True,
            },
        },
        "F#1": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.LEFT_STICK.value,
                "x": 0,
                "y": -100,
                "tilted": 0.4,
                "block": True,
            },
        },
        "F#2": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.RIGHT_STICK.value,
                "x": -100,
                "y": 0,
                "tilted": 0.4,
                "block": True,
            },
        },
        "G#2": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.RIGHT_STICK.value,
                "x": 100,
                "y": 0,
                "tilted": 0.4,
                "block": True,
            },
        },
        "G2": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.R_STICK_PRESS.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "C3": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.RIGHT_STICK.value,
                "x": 0,
                "y": 100,
                "tilted": 0.4,
                "block": True,
            },
        },
        "D2": {
            "action": Action.TILT_STICK,
            "args": {
                "stick": Stick.RIGHT_STICK.value,
                "x": 0,
                "y": -100,
                "tilted": 0.4,
                "block": True,
            },
        },
        "G3": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.X.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "C#3": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.Y.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "D#3": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.A.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
        "A2": {
            "action": Action.PRESS_BUTTONS,
            "args": {
                "buttons": [Button.B.value],
                "down": 0.1,
                "up": 0.1,
                "block": True,
            },
        },
    }
