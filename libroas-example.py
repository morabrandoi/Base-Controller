import pyaudio
import numpy as np
import librosa
import time

# Define some constants
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 48000
CHUNK = 2048
DEVICE_NAME = "MIGHTY PLUG USB"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Find the device index
device_index = None
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(i, info["name"])
    if DEVICE_NAME in info["name"]:
        device_index = i
        break

if device_index is None:
    print(f"Could not find device named {DEVICE_NAME}")
    p.terminate()
    exit()


# Function to process the audio frame and detect pitch
def detect_pitch(y):
    pitches, magnitudes = librosa.piptrack(y=y, sr=RATE)
    index = magnitudes[:, 0].argmax()
    pitch = pitches[index, 0]

    # Return None if no pitch detected
    if pitch == 0.0:
        return None
    return librosa.hz_to_note(pitch)


def callback(in_data, frame_count, time_info, status):
    buffer_np = np.frombuffer(in_data, dtype=np.float32)
    note = detect_pitch(buffer_np)
    if note:
        print(f"Detected note: {note}")
    return (in_data, pyaudio.paContinue)


stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    input_device_index=device_index,
    frames_per_buffer=CHUNK,
    stream_callback=callback,
)
stream.start_stream()

try:
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
