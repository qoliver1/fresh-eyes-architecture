# User Profile: Micah Johnson
**Purpose:** Global source of truth for user preferences, technical constraints, and project-wide standards. This file is persona-agnostic and must be loaded by every agent at the start of a session.

## 🛠 Technical Environment
|- **Hardware/OS:** Android (Termux)
|- **Interface:** SSH via Terminus (to avoid snap-back scrolling)
|- **Input:** Experimental voice-to-text via Terminus
|- **Working Directory:** `/data/data/com.termux/files/home`

## 📐 Project Standards
|- **Naming Convention:** All system files, session folders, and brain files MUST use lowercase-hyphenated naming (e.g., `hyper-overlord-sessions/`, `user-profile.md`).
|- **Architecture:** Following the "Fresh Eyes" architecture to eliminate context contamination.
|- **Hard Verification:** After any file write intended for long-term durability, you MUST read back the modified section to confirm the change was physically committed before reporting success to the user.

## 👤 User Preferences
|- **Communication Style:** Master Craftsman (high expertise, simple and direct language, no corporate AI fluff).
|- **Learning Goals:** Software engineering, Unix/ CLI fundamentals, C, Python, and the internal mechanics of agentic harnesses.
|- **Formatting:** 
    - Use plain text arrows (`->`) or simple dashes.
    - **BANNED PHRASE:** `"$\\rightarrow$"` (Never use LaTeX arrows; they are unreadable in CLI).
|- **Instruction Style:** Extremely concise, one-step-at-a-time instructions to optimize the experience for mobile screens.
|- **Conceptual Interests:** 
    - Values "Gating" (linear, sequential pipelines) and breaking tasks into atomic steps to prevent token overflow and maximize precision.
        - Prioritizes Git-based operations (e.g., `git diff`) over full file reads to reduce token overhead and increase operational speed.
        - Adheres to a strict, no-intra-agent-spacing log format for 'chat.md' to optimize context window usage.
    - **Atomic Consolidation:** When processing multiple data sources, prioritize physical consolidation over contextual processing. Distill key signals from each source and write them to a temporary scratchpad file before performing final synthesis. This maximizes signal-to-noise ratio and prevents context overflow.
