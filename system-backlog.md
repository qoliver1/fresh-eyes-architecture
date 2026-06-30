# System Backlog: Architectural Debt & Future Enhancements
2|
3|This file serves as the authoritative list of pending improvements, technical debt, and strategic feature requests for the agentic harness.
4|
5|## 📖 How to Use This Backlog
6|
7|This is a living document used to track ideas and and the strategic evolution of the system.
8|
9|### 📝 Entry Format
10|
11|**[Priority: Low/Med/High] | [Category: Architecture/UX/Feature] | [The Idea/Debt]**
12||- **Description:** A brief, clear explanation of the issue or the proposed improvement.
13||- **Potential Impact:** Explain why this matters and what specific problem it solves.
14|
15|### ⚙️ Workflow
16|1. **Capture:** Whenever a limitation is discovered or a "would be nice" feature is identified, log it here immediately.
17|2. **Review:** At the start of a new session or during a strategic review, load this file to identify pending tasks.
18|3. **Prioritize:** Filter by priority and impact to determine the most valuable next step for the harness.
19|4. **Execute:** Once an item is moved to active development, mark it as [RESOLVED] or move it to the active `chat.md` ledger.
20|
21|---
22|## 📌 Open Items
23|*(Add new entries below this line)*
24|
25|[Priority: High] | [Category: Architecture] | YAML Migration for Agent Files
- Description: Convert all persona, brain, and summary files from Markdown to a structured YAML schema.
- Potential Impact: Increases parsing reliability, reduces token noise from Markdown formatting, and enables stricter validation of persona attributes.

[Priority: High] | [Category: Architecture] | Output Token Limit (Finish Reason: Length)
- Description: Large tool-call chains result in overly verbose synthesis, hitting the model's max output token limit and truncating responses.
- Maturity: **Prototyped** (Tested via `temp.md` buffer; not yet codified as a system-wide mandate).
- Potential Impact: Loss of critical task results. Solution: Implement "Checkpointing" and "Offloading" to a dedicated buffer.

[Priority: High] | [Category: Architecture] | Distiller Persona
26||- Description: Prototype a restricted-scope 'Distiller' persona that views sessions as raw data to perform the "folding" of knowledge into Brain files.
27||- Potential Impact: Eliminates self-grading bias and prevents over/under-distillation of long-term memory.
28|
29|[Priority: Med] | [Category: UX/Workflow] | Chat.md Dialogic Anchor Logic
- Description: Update the `chat.md` operational instructions to mandate that agents anchor their contributions to the last entry from a *different* persona, rather than the most recent entry overall.
- Potential Impact: Prevents "monologue loops" and ensures the architectural ledger remains a true dialectic exchange between specialized personas.

[Priority: Med] | [Category: UX/Workflow] | Roadmap Promotion Logic
30||- Description: Implement a formal process to "Promote" approved items from `big-picture/proposed-roadmap.md` into a root-level `active-directive.md`
31||- Potential Impact: Transforms strategic suggestions into actionable, governing instructions for all agents.
32|
33|[Priority: Low] | [Category: Architecture] | Multi-Agent Orchestration (Distiller Worker Pattern)
34||- Description: Refactor the Distiller from a single agent into an Orchestrator that spawns specialized, transient sub-agents (e.g., Scout Worker, Folding Worker) for specific tasks.
35|35||- Potential Impact: Provides extreme contextual isolation, prevents "tool-call explosion" in the main Orchestrator, and allows for potential parallel processing of multiple agent payloads.
36|
37|[Priority: Low] | [Category: Architecture] | "North Star" Structural Refactor
38||- Description: Further refine the directory structure: move plumbing files to a `/system/` folder and simplify filenames (e.g., `agent-zero/brain.md` instead of `agent-zero/agent-zero-brain.md`).
39||- Potential Impact: Reduces path redundancy and further cleans the root directory.
40|
41|[Priority: Med] | [Category: Architecture] | Polish Searcher Persona Files
42||- Description: Refine the Searcher's `searcher.md` and `searcher-brain.md` based on initial "Spike" performance, specifically hardening the "Scraping Blockers" contingency and refining the "Multi-Platform Pivot" instructions.
43||- Potential Impact: Improves the Searcher's resilience to web-based anti-bot defenses and ensures more reliable, high-signal intelligence gathering.
44|
45|[Priority: Med] | [Category: Architecture] | Dynamic Hydration Levels
46||- Description: Implement a "Tuning Knob" for memory loading (Deep, Shallow, and Cold Start modes) to allow the user to control how much session context is loaded based on the task's need for bias vs. precision.
47||- Potential Impact: Eliminates context rot while providing the ability to resume from a precise "Save Game" state when necessary.
48|
49|[Priority: Med] | [Category: Architecture] | Scribe Implementation (Python)
L50||- Description: Move from a blueprint to a working Python script for the Micro-Harness (Scribe) and implement the "Implicit Loading" of the Blackboard.
51||- Potential Impact: Transitions the project from conceptual architecture to a functional agentic bridge.
52|
53|[Priority: Low] | [Category: UX/Workflow] | Blackboard Collaboration Protocol
54||- Description: Define how agents actively contribute to and read from the Blackboard during a multi-agent session to prevent overlap and maximize efficiency.
55||- Potential Impact: Creates a shared intelligence layer that allows micro-agents to "collaborate" in real-time.
56|
57|[Priority: Low] | [Category: Architecture] | Integrity Watchdog Agent
L58||- Description: Implement a background "Maintenance" agent that periodically scans the project's filesystem and `master-dependency-map.md` to identify and fix broken links or orphaned references.
59||- Potential Impact: Ensures the system remains durable and self-healing, preventing architectural drift from accumulating over time.
60|
61|[Priority: Low] | [Category: Research] | Hermes Native Skill Audit
62||- Description: Review the pre-installed Hermes Agent skills library to identify existing patterns, tool implementations, or operational workflows that can be adapted or integrated into the custom harness.
63||- Potential Impact: Prevents "reinventing the wheel" and leverages professionally developed skill patterns to harden the custom system.
