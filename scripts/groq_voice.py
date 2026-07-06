import os
import sys
import requests
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Load API key from .env
    # We use the path relative to home to ensure it's found
    env_path = Path.home() / ".hermes" / ".env"
    api_key = None
    if env_path.exists():
        with open(env_path, "r") as f:
            for line in f:
                if line.startswith("GROQ_API_KEY="):
                    api_key = line.strip().split("=", 1)[1]

    if not api_key:
        print("Error: GROQ_API_KEY not found in ~/.hermes/.env")
        sys.exit(1)

    # Read the text to speak
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Groq Orpheus API call
    url = "https://api.groq.com/openai/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "canopylabs/orpheus-v1-english",
        "input": text,
        "voice": "troy",
        "response_format": "wav"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        
        # Trigger playback using mpv
        import subprocess
        subprocess.run(["mpv", "--no-video", "--really-quiet", output_path])
    except Exception as e:
        print(f"Error calling Groq TTS: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
