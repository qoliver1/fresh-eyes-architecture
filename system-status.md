# System Status: The Truth Map
**Purpose:** The authoritative source of truth for feature maturity. This prevents "narrative drift" in `chat.md` where prototypes are mistaken for governing laws.

## 🗺️ Feature Maturity Matrix

| Feature | Status | Maturity | Reference | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Gated Boot Sequence | Active | Governing | `boot-sequence/` | Mandatory for all persona materialization. |
| Memory Hierarchy | Active | Governing | `user-profile.md` | Tiered: Profile $\rightarrow$ Brain $\rightarrow$ Snapshot. |
| Custom Memory Stack | Active | Governing | `user-profile.md` | Decoupled from internal Hermes store. |
| Path Integrity Trigger | Active | Governing | `user-profile.md` | Mandatory audit on structural changes. |
| Buffered Execution | Testing | Prototyped | `temp.md` | Used to bypass output token limits. Not yet mandatory. |
| Distiller Persona | Testing | Prototyped | `agents/distiller/` | Decoupled identity/process for zero-bias folding. |
| Dialogic Anchor | Proposed | Idea | `chat.md` | Mandating responses to different personas to prevent monologues. |
| Roadmap Promotion | Proposed | Idea | `system-backlog.md` | Formal process to move proposals to directives. |
| Truth Map (`system-status.md`) | Active | Governing | `system-status.md` | This file itself. |

## 📈 Maturity Definitions
- **Idea:** A conceptual suggestion in the backlog or chat.
- **Prototyped:** Working in a limited capacity or a single session. Not a system-wide rule.
- **Beta:** Implemented across multiple personas but still being refined.
- **Governing:** A codified law of the harness. All agents MUST follow this.
