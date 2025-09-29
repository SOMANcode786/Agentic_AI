import sounddevice as sd
import numpy as np

recorded_chunks = []

def record_audio(in_samplerate: int):
    print("🎤 Recording started! Press Enter to stop...")
    with sd.InputStream(
        samplerate=in_samplerate,
        channels=1,
        dtype="int16",
        callback=lambda indata, frames, time, status: recorded_chunks.append(indata.copy())
    ):
        input()
    print("🛑 Recording stopped.")
    return recorded_chunks

def playback_audio(chunks, out_samplerate: int):
    audio_buffer = np.concatenate(chunks)
    print("🔊 Playing recorded audio...")
    sd.play(audio_buffer, samplerate=out_samplerate)
    sd.wait()
    return audio_buffer
