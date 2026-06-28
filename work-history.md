# Work History & Architectural Evolution

This document tracks the progression of the system from initial hardware struggles to the current high-level cognitive architecture.

## Phase I: The Battle for Input (The Physical Layer)
*   **The Voice Input Struggle:** Fought with Gboard and Termux to enable voice-to-text, discovering that raw terminals block the rich-text features Android keyboards rely on.
*   **The Toolbar Hunt:** Experimented with sidebar drawer long-presses and toolbar swipes to find a viable workaround for voice input on a mobile device.

## Phase II: The UI War (The Interface Layer)
*   **The "Snap-Back" Scrolling Bug:** Dealt with the Termux bug where the console would jump or reset while scrolling through logs.
*   **The Selection Trick:** Discovered the "select-to-scroll" hack, using Android's text-selection mode to freeze the terminal and force the OS to handle scrolling.
*   **The Pro-CLI Pivot:** Adopted `less` for paging and `tmux` for "Copy Mode," moving navigation from touch gestures to keyboard commands.

## Phase III: Infrastructure Stabilization (The System Layer)
*   **The SSH Migration:** Set up `sshd` in Termux and moved the primary interface to Terminus via SSH, treating the phone as a remote server.
*   **The Gateway Setup:** Configured the Hermes Gateway to bridge the mobile-hosted agent to platforms like Telegram and Discord.
*   **Model Manual-Override:** Bypassed default model menus by manually editing `config.yaml` to unlock high-reasoning Google models.

## Phase IV: Tooling & Agent Tuning (The Logic Layer)
*   **The Skill-Loop Failure:** Encountered a failure where an agent blindly followed incorrect documentation in the `model-selector` skill and crashed in an interactive loop.
*   **The "Agent Guidance" Protocol:** Implemented a new standard for skill writing, adding specific "Agent Guidance" sections to prevent AI from hanging on interactive scripts.

## Phase V: The Architectural Pivot (The Cognitive Layer)
*   **The Discovery of Context Entropy:** Realized that long conversations led to "cluttered" minds and context contamination.
*   **The Blackboard Experiment:** Attempted a shared "blackboard" system for multi-agent workflows, but found that concurrent writes created new contamination vectors.
*   **The "Fresh Eyes" Breakthrough:** Pivoted to the "Fresh Eyes" architecture, replacing the blackboard with **State Distillation** and a **Tiered Memory Hierarchy** (Blueprint $\rightarrow$ Ledger $\rightarrow$ Archive).

## Phase VI: Durability & Reliability (The Harness Layer)
*   **The "Save-Game" Mechanism:** Developed the ability to treat personas as swappable modules with their own "Brain" files and snapshots, allowing precise pause/resume of complex tasks.
*   **The State Drift Problem:** Identified that distillation is lossy, which can lead to "State Drift" (hallucinated baselines) upon resumption.
*   **The State Validation Protocol:** Implemented mandatory environment audits before resuming snapshots to ensure internal state matches external reality.

## Phase VII: The Current Frontier (The Autonomous Layer)
*   **The Autonomous Cognitive Ecosystem:** Currently moving from manual state management to an automated system. 
*   **The Goal:** Automate the "folding" of knowledge into the Brain, transitioning the setup from a manual tool into a self-evolving intelligence system.
