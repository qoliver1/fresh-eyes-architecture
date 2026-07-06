import asyncio
import edge_tts
import sys
import os

async def generate_tts(text, output_path):
    # Using a high-quality Microsoft neural voice
    voice = "en-US-AriaNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 edge_tts_wrapper.py <text> <output_path>")
        sys.exit(1)

    input_text = sys.argv[1]
    output_file = sys.argv[2]

    try:
        asyncio.run(generate_tts(input_text, output_file))
        print(f"Successfully generated: {output_file}")
    except Exception as e:
        print(f"Error generating TTS: {e}")
        sys.exit(1)
