from enum import Enum, unique


# The button object containing the button string constants.
@unique
class Button(Enum):
    Y = "Y"
    X = "X"
    B = "B"
    A = "A"
    JCL_SR = "JCL_SR"
    JCL_SL = "JCL_SL"
    R = "R"
    ZR = "ZR"
    MINUS = "MINUS"
    PLUS = "PLUS"
    R_STICK_PRESS = "R_STICK_PRESS"
    L_STICK_PRESS = "L_STICK_PRESS"
    HOME = "HOME"
    CAPTURE = "CAPTURE"
    DPAD_DOWN = "DPAD_DOWN"
    DPAD_UP = "DPAD_UP"
    DPAD_RIGHT = "DPAD_RIGHT"
    DPAD_LEFT = "DPAD_LEFT"
    JCR_SR = "JCR_SR"
    JCR_SL = "JCR_SL"
    L = "L"
    ZL = "ZL"


# The sticks object containing the joystick string constants
@unique
class Stick(Enum):
    RIGHT_STICK = "R_STICK"
    LEFT_STICK = "L_STICK"


# NOTE: must manually keep this in sync with server.py
@unique
class Action(Enum):  # enum
    PRESS_BUTTONS = "press_buttons"
    TILT_STICK = "tilt_stick"
