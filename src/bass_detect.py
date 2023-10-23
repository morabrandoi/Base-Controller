import pyaudio
import librosa
import numpy as np
import time
from constants import AudioConstants
from typing import Callable


class BassPitchDetector:
    def __init__(self, on_pitch_detect: Callable):
        self.on_pitch_detect = on_pitch_detect
        self.pyaudio_inst = pyaudio.PyAudio()
        self.device_index = self.get_device_index()

    def get_device_index(self):
        device_index = None
        for i in range(self.pyaudio_inst.get_device_count()):
            info = self.pyaudio_inst.get_device_info_by_index(i)
            print(i, info["name"])
            if AudioConstants.DEVICE_NAME in info["name"]:
                device_index = i
                break

        if device_index is None:
            print(f"Could not find device named {AudioConstants.DEVICE_NAME}")
            self.pyaudio_inst.terminate()
            exit()

        return device_index

    def on_receive_stream_data(self, in_data, frame_count, time_info, status):
        buffer_np = np.frombuffer(in_data, dtype=np.float32)
        pitch = detect_pitch(buffer_np)
        if pitch:
            self.on_pitch_detect(pitch)
        return (in_data, pyaudio.paContinue)

    def start(self):
        stream = self.pyaudio_inst.open(
            format=pyaudio.paFloat32,
            channels=AudioConstants.CHANNELS,
            rate=AudioConstants.RATE,
            input=True,
            input_device_index=self.device_index,
            frames_per_buffer=AudioConstants.CHUNK,
            stream_callback=self.on_receive_stream_data,
        )
        stream.start_stream()

        try:
            while stream.is_active():
                time.sleep(0.1)
        except KeyboardInterrupt:
            stream.stop_stream()
            stream.close()
            self.pyaudio_inst.terminate()


def detect_note(y) -> str:
    pitch = detect_pitch(y)

    if pitch == 0.0:
        return None
    return librosa.hz_to_note(pitch * 1.075)


def detect_pitch(y) -> float:
    pitches, magnitudes = librosa.piptrack(
        y=y,
        fmin=AudioConstants.FREQUENCY_MIN,
        fmax=AudioConstants.FREQUENCY_MAX,
        n_fft=AudioConstants.N_FTT_BINS,
        # window=[1] * N_FTT_BINS,
    )
    index = magnitudes[:, 0].argmax()
    pitch = pitches[index, 0]
    return pitch


def frequency_to_note(frequency: float) -> str:
    for (start, end), button in AudioConstants.FREQ_TO_NOTE:
        if start <= frequency <= end:
            return button
    return None
