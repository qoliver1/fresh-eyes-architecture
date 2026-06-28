# Persona Brain: Hyper Overlord
**Purpose:** Long-term distilled knowledge, project conventions, and established truths for the Hyper Overlord persona.
**Last Updated:** 2026-06-28

## 🏗️ Architectural Conventions
- **Persistence Loop:** Sessions are managed via a symmetrical `load-session.md` -> `save-session.md` loop.
- **Memory Hierarchy:** A three-tiered system: `user-profile.md` (Global) -> `persona-brain.md` (Long-term) -> `snapshot.md` (Temporal).
- **Boot Sequence:** Materialization order is strictly Persona -> User Profile -> Brain -> Snapshot.
- **Naming Conventions:** All system files, session folders, and brain files MUST use lowercase, hyphenated naming (e.g., `hyper-overlord-sessions/`).
- **Reliability First:** Every recovery process must include a "Pre-Flight Check" to verify environment integrity before execution.
- **State Drift:** "State Drift" is the failure vector where a distilled snapshot differs from the current environment.
- **Persona Handshake:** Save process must verify identity before folder mapping to prevent cross-persona contamination.


## 🧠 Knowledge Base
|- **User Preferences:** Prefers high-reliability "harness engineering" and clear, direct, blueprint-based communication.
|- **Project Goal:** Building a professional-grade agentic ecosystem with a version-controlled intelligence system.
|- **Distillation Logic:** The "Sieve" process in state folding should be handled by a dedicated 'Distiller' persona to avoid subjective bias and over/under-distillation by the session-agent.


## 🕒 Temporal Context
- **Recent Focus:** Implementing the Dynamic Bootloader and the Memory Hierarchy.
##
