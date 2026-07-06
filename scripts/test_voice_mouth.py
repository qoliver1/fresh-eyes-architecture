import os
from gtts import gTTS
import subprocess

text = "Hello Micah, the voice prototype is working."
output_file = "/data/data/com.termux/files/home/test_voice.mp3"

print(f"Generating speech for: '{text}'")
try:
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Speech saved to {output_file}")

    print("Playing audio with mpv...")
    # We use mpv to play the file. 
    # Note: In a real Termux environment, this requires audio permission/setup.
    subprocess.run(["mpv", "--no-video", output_file], check=True)
    print("Playback finished successfully.")

except Exception as e:
    print(f"Error during test: {e}")
finally:
    if os.path.exists(output_file):
        os.remove(output_file)
