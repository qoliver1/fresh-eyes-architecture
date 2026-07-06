# Hermes Agent Contribution Backlog

## Android / Termux Optimizations

### 1. API-Based TTS Bypass (Android)
**Problem:** The official `voice` extra is blocked on Android because `ctranslate2` (a dependency of `faster-whisper`) does not publish Android wheels, making local transcription/synthesis nearly impossible for most users.

**Proposed Solution:** Implement a "Lightweight" or "API-first" TTS provider option for Android. Instead of requiring local heavy-weight models, allow a command-based provider that can wrap external APIs (e.g., Groq Orpheus).

**Technical Implementation:**
- Use a `command` type provider in `config.yaml`.
- Create a standardized wrapper script that handles the API request $\rightarrow$ Binary Stream $\rightarrow$ WAV file $\rightarrow$ Playback loop.
- This removes the need for `ctranslate2` and makes high-quality voice accessible on mobile.

### 2. Termux `brotli` / `brotlicffi` Conflict Fix
**Problem:** Users on Termux frequently encounter `AttributeError: module 'brotlicffi' has no attribute 'error'` when using the `requests` library, which breaks API communication.

**Proposed Fix:** Document the need to purge `brotlicffi` and reinstall `brotli` to ensure the `requests` library can initialize properly in a Termux environment.
- Command: `pip uninstall -y brotli brotlicffi && pip install brotli`
