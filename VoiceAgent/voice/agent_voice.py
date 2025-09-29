from decouple import config
import os
import getpass
import numpy as np
import sounddevice as sd

from agents import Agent
from agents.voice import (
    AudioInput,
    SingleAgentVoiceWorkflow,
    TTSModelSettings,
    VoicePipelineConfig,
    VoicePipeline
)

from configuration.gemini_config import gemini_model


# 🔑 Load API key securely
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or \
    getpass.getpass("Enter OpenAI API Key: ")


# 🎭 Create the Agent
agent = Agent(
    name="Assistant",
    instructions=(
        "Repeat the user's question back to them, and then answer it. "
        "You are speaking via a voice interface, so keep answers simple, "
        "clear, and conversational."
    ),
    model=gemini_model
)


# 🎙️ Workflow (agent + voice system)
workflow = SingleAgentVoiceWorkflow(agent)


# 🎶 Custom TTS voice settings
custom_tts_settings = TTSModelSettings(
    instructions=(
        "Personality: upbeat, friendly, persuasive guide.\n"
        "Tone: Friendly, clear, and reassuring.\n"
        "Pronunciation: Clear and steady.\n"
        "Tempo: Relatively fast, with natural pauses.\n"
        "Emotion: Warm and supportive."
    )
)

voice_pipeline_config = VoicePipelineConfig(tts_settings=custom_tts_settings)


# 🔌 Voice Pipeline
pipeline = VoicePipeline(
    workflow=workflow,
    config=voice_pipeline_config
)


# ⚡ Function to send audio input to pipeline
async def process_audio_with_agent(audio_buffer: np.ndarray, in_samplerate: int):
    audio_input = AudioInput(
        buffer=audio_buffer,
        frame_rate=in_samplerate,
        channels=audio_buffer.shape[1]  # mono=1, stereo=2
    )

    result = await pipeline.run(audio_input=audio_input)

    response_chunks = []
    async for event in result.stream():
        if event.type == "voice_stream_event_audio":
            response_chunks.append(event.data)

    response_audio_buffer = np.concatenate(response_chunks, axis=0)

    print("🤖 Playing AI response...")
    sd.play(response_audio_buffer, samplerate=24_000)  # OpenAI TTS sample rate
    sd.wait()
