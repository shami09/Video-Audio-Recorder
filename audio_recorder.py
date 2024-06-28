import pyaudio
import wave
import threading

class AudioRecorder:
    def __init__(self, filename='output_audio.wav', channels=1, rate=44100, chunk_size=1024):
        self.filename = filename
        self.channels = channels
        self.rate = rate
        self.chunk_size = chunk_size

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      frames_per_buffer=chunk_size)

        self.audio_frames = []
        self.recording = False
        self.audio_thread = threading.Thread(target=self.record_audio)

    def start_recording(self):
        self.recording = True
        self.audio_thread.start()

    def stop_recording(self):
        self.recording = False
        self.audio_thread.join()

    def record_audio(self):
        while self.recording:
            data = self.stream.read(self.chunk_size)
            self.audio_frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        wave_file = wave.open(self.filename, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(self.audio_frames))
        wave_file.close()
