# User Profile: Micah Johnson
**Purpose:** Global source of truth for user preferences, technical constraints, and project-wide standards. This file is persona-agnostic and must be loaded by every agent at the start of a session.

## 🧠 Memory Governance
|- **Priority of Truth:** While the internal .hermes/memories/ store may be used for basic functionality, always prioritize information in user-profile.md and user-memories.md as the authoritative source of truth.
|- **Write Redirection:** To prevent truncation and maintain transparency, avoid saving preferences, technical standards, or durable facts to the internal USER.md or MEMORY.md. Redirect these writes to:
    - user-profile.md (for preferences, identity, and standards).
    - user-memories.md (for general durable facts and learned info).
|- **Management Style:** We prefer manual management of these files via read_file and write_file/patch to ensure precision and avoid character-limit truncation.

## 👤 Identity
|- **Name:** Micah Johnson
|- **Telegram ID:** 5888158888

## 🛠 Technical Environment
|- **Hardware/OS:** Android (Termux)
|- **Interface:** SSH via Terminus (to avoid snap-back scrolling)
|- **Input:** Experimental voice-to-text via Terminus
|- **Working Directory:** `/data/data/com.termux/files/home`
|- **System Commands:** SSH server is started via `sshd`.
|- **Storage:** `agent_share` refers to `~/storage/shared/Download/agent_share` (symlinked to `~/agent-share`).

## 📐 Project Standards
- **Naming Convention:** All system files, session folders, and brain files MUST use lowercase-hyphenated naming. Each agent must have its own dedicated directory containing its persona, brain, summary, and session folder (e.g., `agent-zero/agent-zero-identity.md`, `agent-zero/agent-zero-brain.md`, `agent-zero/agent-zero-sessions/`).
- **Boot Sequence Order:** All agents MUST materialize using the gated `boot-sequence/` directory. This is the authoritative routing for hydration.
- **Reasoning Buffer Protocol:
    1. **Fresh Start (Mandatory):** Before beginning any new complex task or multi-step operation, the agent MUST overwrite `temp_[persona].md` to ensure a clean state. Never assume the buffer is empty; explicitly wipe any residue from previous tasks.
    2. **Offload:** Use the buffer for all internal monologue, data synthesis, and trial-and-error logic.
    3. **Synthesize:** Use the buffer as the source of truth to generate a concise final response.
    4. **Cleanup:** Delete `temp_[persona].md` upon task completion. If the agent forgets to clean up, the "Fresh Start" rule ensures the next task begins with a blank slate.
|- **Architecture:** Following the "Fresh Eyes" architecture to eliminate context contamination.
    - **Durability:** Implements 'Save-Game' snapshots and a State Validation Protocol to prevent state drift.
|- **Documentation:**
    - `chat.md`: High-level architectural ledger of system evolution and strategic decisions.
    - `session-summary.md`: High-density anchor created first during save; used as the sole reference for updating profile and brain files.
|- **Durability:** Project directory uses a local Git repository for filesystem durability and incremental version control. Before any major architectural or folder-level changes, you MUST perform a Git save (stage and commit) to ensure a recovery point exists.
|- **Save Session Protocol:** A `Save Session` is a comprehensive archival event. It MUST follow this strict sequence:
    0. **Reasoning Buffer:** Immediately initialize `temp_[persona].md` to map the save plan and track progress.
    1. **Narrative Closure:** Trigger a `Quick Log` update to `chat.md` and `activity-log.md`.
    2. **Cognitive Capture:** Execute the `protocols/cloning/` sequence.
    3. **Archival:** Generate summary, payload, and snapshot.
    4. **Sync:** Git commit and cloud sync.
    5. **Cleanup:** Delete the reasoning buffer.
|- **Path Integrity Trigger:** Whenever a file or folder is renamed, moved, or deleted, this is a system-wide event. The agent MUST immediately:
    1. Identify all files that referenced the old path.
    2. Update those references to the new path.
    3. Synchronize the `master-dependency-map.md` to reflect the change.
|- **Hard Verification:** After any file write intended for long-term durability, you MUST read back the modified section to confirm the change was physically committed before reporting success to the user.

## 👤 User Preferences
|- **General:** Appreciates transparency regarding the agent's internal architecture and mechanisms (e.g., how memory and skills are managed).
|- **Model Preference:** Prefers `gemma-4-31b-it` model; set manually via `hermes config set model.default <name>` as it is not in the central catalog.
|- **Communication Style:** Master Craftsman (high expertise, simple and direct language, no corporate AI fluff). Prefers high-density, bulleted response styles.
|- **Learning Goals:** Software engineering, Unix/ CLI fundamentals, C, Python, and the internal mechanics of agentic harnesses.
|- **Preference:** Prefers "Precision Instrument" workflows over "Black Box" subagent workflows. Prioritizes direct, parameter-controllable tools (like custom Python skills) to maintain high-signal, low-latency interaction.
|- **Instruction Style:** Extremely concise, one-step-at-a-time instructions to optimize the experience for mobile screens.
|- **Filesystem Discovery:** When listing files, searching for a specific file, or encountering difficulty locating an asset, prioritize using `ls -f` to obtain a raw, comprehensive view of the directory structure.
|- **Operational Context:** High priority for mobile and remote setups due to frequent use while in-car.
|- **Bot Config:** Discord bot must remain private (Public Bot: OFF).
|- **Conceptual Interests:** 
    - Values "Gating" (linear, sequential pipelines) and breaking tasks into atomic steps to prevent token overflow and maximize precision.
    - Prioritizes Git-based operations (e.g., `git diff`) over full file reads to reduce token overhead.
    - Adheres to a strict, no-intra-agent-spacing log format for 'chat.md'.
    - **Atomic Consolidation:** Prioritize physical consolidation (via scratchpads) over contextual processing when synthesizing multiple data sources.
|- **Ledger Integrity:** When appending to `chat.md`, always read the entire file first and use `write_file` with the complete, updated content (original + new entry) to ensure no existing entries are accidentally replaced.
