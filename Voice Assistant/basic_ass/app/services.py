import os
import openai
from fastapi.responses import StreamingResponse
from app.utils import save_upload_file

openai.api_key = os.getenv("OPENAI_API_KEY")

async def process_audio(audio_file):
    # 1. Save file
    file_path = await save_upload_file(audio_file)

    # 2. Speech-to-Text (Whisper)
    with open(file_path, "rb") as f:
        stt = openai.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    user_text = stt.text

    # 3. Agent (GPT reply)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": user_text}
        ]
    )
    reply_text = response.choices[0].message.content

    # 4. Text-to-Speech
    speech = openai.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=reply_text
    )

    return StreamingResponse(
        speech.iter_bytes(),
        media_type="audio/mpeg"
    )
