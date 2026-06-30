# Micro-Harness Blueprint

## 1. Core Concept
The Micro-Harness is a lightweight, Python-based "agentic bridge" designed to spawn specialized sub-agents with surgical precision. Unlike a full harness (which is a separate process with heavy overhead), the Micro-Harness operates as a function-call—a "Scribe" that handles the transport of data between the Main Agent and the LLM API.

**Primary Goal:** Eliminate "Context Rot" and "Contamination" while maintaining absolute visibility and data integrity.

---

## 2. Architecture: The "Scribe" Approach
Instead of spawning a new instance of the full Hermes environment, the Micro-Harness uses a Python script to:
- **Inject Identity:** Load `agent.md` (Persona), `brain.md` (Knowledge), and `user-profile.md` (Preferences) directly into the system prompt.
- **Transport Data:** Send the prompt to the API and receive the response.
- **Automatic Logging:** Mirror every request and response to a raw log file in real-time.
- **Low Overhead:** Bypass PTYs, terminal environments, and process initialization.

---

## 3. The Three-Tier Memory System
To balance "Soul" (personality/nuance) with "Clarity" (efficiency/anti-rot), the Micro-Harness implements three layers of memory:

### Tier 1: The "Essence" (Hybrid Snapshot)
- **Format:** High-density `.md` file.
- **Content:** Distilled conclusions, the current "mental model" of the problem, and a precise "Next Step" instruction.
- **Purpose:** Provides immediate, noise-free focus.

### Tier 2: The "Momentum" (Tail Log)
- **Format:** The last 5–10 raw messages from the session.
- **Content:** The immediate preceding dialogue.
- **Purpose:** Preserves the "vibe," flow, and continuity (prevents the "coma" effect).

### Tier 3: The "Archive" (Searchable DB)
- **Format:** SQLite database with FTS5 (Full-Text Search).
- **Content:** Every single message, tool call, and response from every sub-session.
- **Purpose:** Absolute data recovery. Allows the agent to search for forgotten clues using `search_micro_sessions()`.

---

## 4. The Life Cycle & "Closing Ritual"

### Phase A: Spawning
1. Script reads **Essence** (T1) and **Momentum** (T2).
2. Injects **Identity** files (Persona/Brain/Prefs).
3. Agent wakes up with a clear goal and a feeling of continuity.

### Phase B: Execution
1. All inputs/outputs are mirrored to the **Archive** (T3).
2. Agent can query the Archive to retrieve historical context without cluttering the current window.

### Phase C: The Closing Ritual (Distillation)
Before the agent is destroyed, it performs a final task:
1. **Review:** The agent analyzes its own raw session log.
2. **Fold:** It distills the "noise" (struggles, tangents, mistakes) into the "essence" (breakthroughs, conclusions).
3. **Update:** The `Essence` (T1) file is updated for the next session.
4. **Purge:** The active session state is cleared, but the record remains in the Archive.

---

## 5. Comparison: Micro-Harness vs. Full Harness

| Feature | Full Harness | Micro-Harness |
| :--- | :--- | :--- |
| **Resource Cost** | High (Process-level) | Low (Request-level) |
| **Transparency** | Opaque (Internal Logs) | Transparent (Direct Stdout/Log) |
| **Context** | Heavy/Cumulative (Rot-prone) | Surgical/Distilled (Rot-resistant) |
| **State** | DB-based Session | Snapshot + Archive Hybrid |
| **Identity** | Loaded at Startup | Injected per Call |

---

## 6. Future Iteration Points
- [ ] Implementation of the `search_micro_sessions` tool.
- [ ] Defining the exact "Distillation Prompt" for the Closing Ritual.
- [ ] Integration of "Micro-Tools" (Giving the script limited file/web access).
- [ ] Testing the "Momentum" window size for optimal vibe preservation.
