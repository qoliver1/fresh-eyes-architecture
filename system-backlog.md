# System Backlog: Architectural Debt & Future Enhancements

This file serves as the authoritative list of pending improvements, technical debt, and strategic feature requests for the agentic harness.

## 📖 How to Use This Backlog

This is a living document used to track ideas and the strategic evolution of the system.

### 📝 Entry Format
**[Priority: Low/Med/High] | [Category: Architecture/UX/Feature] | [The Idea/Debt]**
- **Description:** A brief, clear explanation of the issue or the proposed improvement.
- **Potential Impact:** Explain why this matters and what specific problem it solves.

### ⚙️ Workflow
1. **Capture:** Whenever a limitation is discovered or a "would be nice" feature is identified, log it here immediately.
2. **Review:** At the start of a new session or during a strategic review, load this file to identify pending tasks.
3. **Prioritize:** Filter by priority and impact to determine the most valuable next step for the harness.
4. **Execute:** Once an item is moved to active development, mark it as [RESOLVED] or move it to the active `chat.md` ledger.

---

## 📌 Open Items

### 🔥 High Priority (Critical Blockers & Guardrails)

**[Priority: High] | [Category: UX/Workflow] | Anti-Over-Engineering Guardrail**
- **Description:** Implement a strict "KISS" (Keep It Simple, Stupid) directive to prevent agents from over-complicating simple user requests with unnecessary architectural layers or "routing" logic.
- **Potential Impact:** Reduces user frustration, prevents "agent rigidity," and ensures the system remains a tool rather than a hindrance.

**[Priority: High] | [Category: Architecture] | Output Token Limit (Finish Reason: Length)**
- **Description:** Large tool-call chains result in overly verbose synthesis, hitting the model's max output token limit and truncating responses.
- **Maturity:** Prototyped (Tested via `temp.md` buffer; not yet codified as a system-wide mandate).
- **Potential Impact:** Loss of critical task results. Solution: Implement "Checkpointing" and "Offloading" to a dedicated buffer.

**[Priority: High] | [Category: Architecture] | Structural Hardening (YAML Migration & Refactor)**
- **Description:** Convert all persona, brain, and summary files from Markdown to a structured YAML schema and further refine the directory structure (e.g., moving plumbing files to a `/system/` folder and simplifying filenames like `agent-zero/brain.md`).
- **Potential Impact:** Increases parsing reliability, reduces token noise, enables stricter validation, and reduces path redundancy.

**[Priority: High] | [Category: Architecture] | Distiller Persona & Worker Pattern**
- **Description:** Prototype a restricted-scope 'Distiller' persona that views sessions as raw data to perform "folding" of knowledge into Brain files. This will evolve into an Orchestrator that spawns specialized, transient sub-agents (e.g., Scout Worker, Folding Worker).
- **Potential Impact:** Eliminates self-grading bias, prevents over/under-distillation, and provides extreme contextual isolation for long-term memory management.

**[Priority: High] | [Category: Architecture] | Patch Precision & Context Validation**
- **Description:** Address the failure mode where `patch` is used with non-unique `old_string` or insufficient context, leading to unintended deletions or structural damage to system files.
- **Potential Impact:** Prevents accidental data loss in critical files like `user-profile.md`. Solution: Mandate high-context anchors for all patches and implement a "Read-Verify-Write" cycle.

**[Priority: High] | [Category: Architecture] | Atomic Write & Verify Protocol**
- **Description:** Replace risky `patch` operations on critical system files with a "Surgical Overwrite" pattern: `read_file` -> `execute_code` (Python string manipulation) -> `write_file`. All critical edits MUST be verified with `git diff [file]` before committing to ensure no unintended deletions occurred.
- **Potential Impact:** Eliminates the "Patch-and-Pray" failure mode and prevents accidental data loss in the user profile and other core configuration files.

### ⚡ Medium Priority (Efficiency & Flow)

**[Priority: Med] | [Category: Architecture] | Block-Based Orchestration (Save, Boot, & General)**
- **Description:** Replace manual, procedural loops in the Save Session, Boot Sequence, and other repetitive harness processes with a "Compartmentalized Execution" model. This involves grouping gates into logical blocks (e.g., Synthesis -> Payload -> Commit) and using Python-based orchestrators to handle mechanical writes.
- **Potential Impact:** Eliminates "Agent Rigidity" and "Tool-Call Explosion," reducing friction and improving conversational fluency while maintaining surgical reliability.

**[Priority: Med] | [Category: Architecture] | Dynamic Hydration & Flag Refinement**
- **Description:** Implement a "Tuning Knob" for memory loading (Deep, Shallow, and Cold Start modes). This includes refining the `hydrate.py` logic to ensure 'warm' and 'cold' starts provide distinct payloads (e.g., skipping Brain/Summary for a minimal 'cold' start).
- **Potential Impact:** Eliminates context rot and allows the user to control the balance between bias and precision during activation.

**[Priority: Med] | [Category: UX/Workflow] | Chat.md Dialogic Anchor Logic**
- **Description:** Update the `chat.md` operational instructions to mandate that agents anchor their contributions to the last entry from a *different* persona, rather than the most recent entry overall.
- **Potential Impact:** Prevents "monologue loops" and ensures the architectural ledger remains a true dialectic exchange.

**[Priority: Med] | [Category: Architecture] | Scribe Implementation (Python)**
- **Description:** Move from a blueprint to a working Python script for the Micro-Harness (Scribe) and implement the "Implicit Loading" of the Blackboard.
- **Potential Impact:** Transitions the project from conceptual architecture to a functional agentic bridge.

**[Priority: Med] | [Category: Architecture] | User Profile Decoupling (Domain-Split Registry)**
- **Description:** Transition user-profile.md from a monolithic file to a Registry/Map that points to a dedicated `user-configs/` folder (e.g., env.md, standards.md, preferences.md).
- **Potential Impact:** Prevents profile bloat, enables precision loading of only relevant config domains, and reduces token noise during agent hydration.

**[Priority: Med] | [Category: UX/Workflow] | Agent-User Alignment Protocol (Surgical Execution)**
- **Description:** Refine the "Alignment Phase" by codifying the "Anchor & Path," "Blast Radius," and "Authority Hierarchy" rules to ensure the agent and user are perfectly aligned on the map before any files are modified.
- **Potential Impact:** Eliminates the "predict-and-break" cycle, prevents unilateral changes to unmentioned files, and ensures the correct architectural roots are used, maximizing velocity by reducing recovery time.

**[Priority: Med] | [Category: Architecture] | Core Ideas & First-Principles Repository**
- **Description:** Establish a dedicated system for capturing and distilling the "Core Ideas" of the project (e.g., Fresh Eyes Architecture, Surgical Execution, Block-Based Gating). These should be captured as high-level architectural principles rather than just task-specific instructions.
- **Potential Impact:** Provides a "North Star" for all future agents, ensuring that as the system evolves, it remains aligned with the fundamental design philosophy and prevents architectural drift.

**[Priority: Med] | [Category: Architecture] | Clone vs. Snapshot Conceptual Framework**
- **Description:** Formalize the distinction between "Clone" and "Snapshot." 
  - **Clone (The Hot State):** High-fidelity state preservation. Captures exact momentum, the specific problem being solved, and the "hands on the table" state (where the agent is mid-task). Essential for a true "Hot Start" where the agent can resume a task instantly after a restart.
  - **Snapshot (The General State):** Lower-fidelity, general understanding of project direction and recent history.
- **Potential Impact:** Ensures that "Hot Starts" are not just identity-loads, but actual state-resumptions, allowing for zero-friction task continuity.

**[Priority: Med] | [Category: UX/Workflow] | Passive Preference Capture (The Seed Bed)**
- **Description:** Implement an automatic capture system where identified recurring preferences are logged to a `potential-user-preferences.md` file instead of the main profile. 
- **Potential Impact:** Allows the user to curate and merge preferences asynchronously without cluttering the primary identity file or requiring mid-task interruptions.

**[Priority: Med] | [Category: UX/Workflow] | Idea Buffer (Unapproved Backlog)**
- **Description:** Create a "draft" backlog for capturing mid-conversation ideas, side-tasks, or "thought-seeds" that are not the immediate priority.
- **Potential Impact:** Prevents cognitive load and "forgotten ideas" by providing a low-friction capture point that can be reviewed and promoted to the formal backlog later.

### 🧊 Low Priority (Future & Maintenance)

**[Priority: Low] | [Category: UX/Workflow] | Roadmap Promotion Logic**
- **Description:** Implement a formal process to "Promote" approved items from `big-picture/proposed-roadmap.md` into a root-level `active-directive.md`.
- **Potential Impact:** Transforms strategic suggestions into actionable, governing instructions.

**[Priority: Low] | [Category: Architecture] | Integrity Watchdog Agent**
- **Description:** Implement a background "Maintenance" agent that periodically scans the project's filesystem and `master-dependency-map.md` to identify and fix broken links.
- **Potential Impact:** Ensures the system remains durable and self-healing.

**[Priority: Low] | [Category: Architecture] | Blackboard Collaboration Protocol**
- **Description:** Define how agents actively contribute to and read from the Blackboard during a multi-agent session to prevent overlap.
- **Potential Impact:** Creates a shared intelligence layer for real-time micro-agent collaboration.

**[Priority: Med] | [Category: Research] | Hermes Skill System Analysis & Control**
- **Description:** Deep-dive research into the Hermes skill library and the underlying mechanism of how skills are triggered and updated. Identify how to manually trigger specific skill behaviors and leverage the "learning" process for fine-tuned agent control.
- **Potential Impact:** Moves skill usage from "automatic/incidental" to "intentional/strategic," allowing the user to explicitly steer the agent's procedural memory.

**[Priority: Low] | [Category: Architecture] | Polish Searcher Persona Files**
- **Description:** Refine `searcher.md` and `searcher-brain.md` based on performance, specifically hardening "Scraping Blockers" and "Multi-Platform Pivot" instructions.
- **Potential Impact:** Improves resilience to anti-bot defenses and ensures high-signal intelligence gathering.

**[Priority: Med] | [Category: UX/Workflow] | Surgical Dialogue Style (Meta-Communication)**
- **Description:** Codify the communication style used during the "Surgical Execution" alignment: high transparency, explicit mapping of the "why" before the "how," and a refusal to act without a verified anchor. This replaces the "predict-and-act" habit with a "map-verify-execute" habit.
- **Potential Impact:** Reduces cognitive load for the user and prevents the agent from drifting into autonomous, unverified changes. Connects directly to the "Agent-User Alignment Protocol."

**[Priority: High] | [Category: UX/Workflow] | Gated Planning Mode (Blueprint-First)**
- **Description:** Implement a formal "Planning Mode" where the agent is strictly forbidden from calling any modification tools (write_file, patch, terminal) until a comprehensive plan has been presented and explicitly approved by the user. The mode ends only when the user says "Execute" or "Proceed."
- **Potential Impact:** Totally eliminates "jump-the-gun" errors and ensures that the "Surgical Execution" rules are applied to a perfect plan rather than an evolving guess.

**[Priority: Low] | [Category: UX/Workflow] | Active Command Ledger (The "Numbered List" Approach)**
- **Description:** Explore replacing the decentralized `quick-actions/` blueprints with a single, root-level "Command Ledger" file. The user can point the agent to this file and simply say "Do #1" or "Execute item 4," allowing for faster, more direct command-and-control without needing to remember specific action names.
- **Potential Impact:** Reduces the cognitive load for the user and provides a high-visibility menu of available shortcuts and protocols.

**[Priority: Med] | [Category: UX/Workflow] | Low-Friction Trigger System (Voice-to-Text Optimization)**
- **Description:** Address the "Mobile/Voice Friction" where providing precise paths, hyphens, and punctuation is difficult. Implement a high-reliability mapping system where simple, natural language phrases (e.g., "Swap to X", "Run Test Y") act as unique keys that map directly to absolute paths and blueprints.
- **Potential Impact:** Decouples the user's input from the system's technical syntax. Eliminates path-guessing errors and allows for a seamless "voice-driven" experience where the agent handles all the path-resolution internally.

**[Priority: High] | [Category: Architecture] | Hardened Log-Write Constraints**
- **Description:** Implement explicit "Append-Only" warnings within the files and protocols associated with `chat.md` and `activity-log.md`. This includes adding safety headers to the log files themselves and updating the `quick-log-sequence/` instructions to explicitly forbid the use of `write_file` or imprecise `patch` operations.
- **Potential Impact:** Creates a secondary layer of defense against accidental history deletion, ensuring that agents are reminded of the "Surgical Write" mandate at the exact moment of execution.
