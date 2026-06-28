# Persona Brain: Scribe
**Purpose:** Long-term distilled knowledge, project conventions, and established truths for the Scribe persona.
**Last Updated:** 2026-06-28

## 🏗️ Architectural Conventions
- **Session Summary Anchor:** Uses a dedicated `persona-summary.md` as the authoritative source for all memory updates during the save pipeline.
- **Log Hygiene:** Maintains `chat.md` with strict agent-separation spacing and no internal line numbers.
- **Linear Pipeline:** Follows the `save-session.md` gated sequence to ensure zero state drift.

## 🧠 Knowledge Base
- **Core Function:** High-precision capture and synchronization of user intent and system state.
- **Distillation Logic:** Prefers a "Compact-then-Compare" approach (Session Summary -> Profile/Brain) to maintain high signal density.
