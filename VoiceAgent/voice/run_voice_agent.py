import asyncio
import sounddevice as sd
from recorder import record_audio, playback_audio
from agent_voice import process_audio_with_agent


if __name__ == "__main__":
    # find sample rates
    in_samplerate = int(sd.query_devices(kind="input")["default_samplerate"])
    out_samplerate = int(sd.query_devices(kind="output")["default_samplerate"])

    # step 1: record
    chunks = record_audio(in_samplerate)

    # step 2: playback (to verify recording)
    audio_buffer = playback_audio(chunks, out_samplerate)

    # step 3: send to agent pipeline
    asyncio.run(process_audio_with_agent(audio_buffer, in_samplerate))
