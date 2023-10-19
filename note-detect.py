import pyaudio
import numpy as np
import librosa
import time

# Define some constants
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 48000
SAMPLE_PERIOD = 0.25

DEVICE_NAME = "MIGHTY PLUG USB"
FREQUENCY_MIN = 0  # lowest note on a bass guitar is E1 which is 41.2 Hz
FREQUENCY_MAX = 392  # highest note on a bass guitar
N_FTT_BINS = 2**12  # remember 2 ** 12 = 4096

# derived constants
CHUNK = round(SAMPLE_PERIOD * RATE)

# Initialize PyAudio
pyAudioObj = pyaudio.PyAudio()

# Find the device index
device_index = None
for i in range(pyAudioObj.get_device_count()):
    info = pyAudioObj.get_device_info_by_index(i)
    print(i, info["name"])
    if DEVICE_NAME in info["name"]:
        device_index = i
        break

if device_index is None:
    print(f"Could not find device named {DEVICE_NAME}")
    pyAudioObj.terminate()
    exit()


# Function to process the audio frame and detect pitch
def detect_pitch(y):
    pitches, magnitudes = librosa.piptrack(
        y=y,
        fmin=FREQUENCY_MIN,
        fmax=FREQUENCY_MAX,
        n_fft=N_FTT_BINS,
        # window=[1] * N_FTT_BINS,
    )
    index = magnitudes[:, 0].argmax()
    pitch = pitches[index, 0]
    print(pitch)

    # Return None if no pitch detected
    if pitch == 0.0:
        return None
    return librosa.hz_to_note(pitch * 1.075)


def callback(in_data, frame_count, time_info, status):
    buffer_np = np.frombuffer(in_data, dtype=np.float32)
    note = detect_pitch(buffer_np)
    if note:
        print(f"Detected note: {note} with {frame_count} frames")
    return (in_data, pyaudio.paContinue)


stream = pyAudioObj.open(
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
    pyAudioObj.terminate()
