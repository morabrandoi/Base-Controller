import pyaudio

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(i, info["name"])

try:
    stream = p.open(
        input_device_index=4,
        format=pyaudio.paInt16,
        channels=1,
        rate=48000,
        input=True,
        frames_per_buffer=1024,
    )
except Exception as e:
    print(f"Error: {e}")


try:
    while True:
        data = stream.read(1024)
        # Process the 'data' as needed
        print(data)
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
