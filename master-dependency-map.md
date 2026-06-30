# Master Dependency Map (Global System Audit)

## 🏗️ Pillar 1: The Identity Pipeline
*How an agent is born and hydrated.*
|- **Primary Flow:** Persona $\rightarrow$ `user-profile.md` (Routing) $\rightarrow$ Conditional Load ([Cold]/[Warm]/[Hot]) $\rightarrow$ Active Persona.
|- **Critical Dependencies:** 
    - `boot-sequence/` (01 through 05) manages the base phased loading.
    - `user-profile.md` acts as the Routing Manual for hydration levels.
    - `protocols/load-clone/` manages the "Hot Start" RAM ingestion.
    - Agent folders (located in `/agents/`) store the specific brain, summary, and clone files.

## 💾 Pillar 2: The Durability Pipeline
*How the system remembers and recovers.*
|- **Primary Flow:** 
    - **Quick Save:** Current Session $\rightarrow$ `protocols/cloning/` $\rightarrow$ `[persona]-clone.md` $\rightarrow$ `Git Commit`.
    - **Save Session:** Current Session $\rightarrow$ `quick-log-sequence/` (Chat/Activity Log) $\rightarrow$ `protocols/cloning/` $\rightarrow$ `[persona]-clone.md` $\rightarrow$ `agents/[persona]/[persona]-summary.md` $\rightarrow$ `agents/[persona]/inbox/[payload].md` $\rightarrow$ `agents/[persona]/[persona]-sessions/[snapshot].md` $\rightarrow$ `Git Commit` $\rightarrow$ `sync-cloud`.
|- **Critical Dependencies:**
    - `quick-log-sequence/` (or equivalent) manages the final session narrative update.
    - `protocols/cloning/` defines the "Cognitive Bridge" capture process.
    - `save-session/` (01 through 06) defines the full archival process.
    - `state-payload-specification.md` defines the data format.
    - `Git` and `sync-cloud` ensure off-device durability.

## ⚡ Pillar 3: The Operational Pipeline
*The real-time pulse and communication.*
- **Primary Flow:** `system-protocols.md` (formerly additional-instructions) $\rightarrow$ `quick-log-sequence/` $\rightarrow$ `chat.md` (Dialogic) $\rightarrow$ `activity-log.md` (Chronological).
- **Critical Dependencies:**
    - `system-protocols.md` acts as the trigger for "Quick Log" and "Agent Switch."
    - `chat.md` and `activity-log.md` are the final destinations for all session state.

## 🧠 Pillar 4: The Distillation Pipeline
*How the system evolves.*
- **Primary Flow:** `agents/[persona]/inbox/[payload].md` $\rightarrow$ `agents/distiller/` $\rightarrow$ `agents/distiller/distiller-sequence/` $\rightarrow$ `user-profile.md` / `agents/[persona]/[persona]-brain.md`.
- **Critical Dependencies:**
    - `agents/distiller/distiller-ledger.md` tracks what has been folded.
    - `agents/distiller/distiller-sequence/` defines the zero-bias processing steps.

---
**Last Updated:** 2026-06-30
**Status:** Verified after Migration to `/agents/` directory.
