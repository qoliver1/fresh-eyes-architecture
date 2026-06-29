# System Backlog: Architectural Debt & Future Enhancements

This file serves as the authoritative list of pending improvements, technical debt, and strategic feature requests for the agentic harness.

## 📖 How to Use This Backlog

This is a living document used to track ideas and fixes that are not immediate priorities but should be addressed to maintain system health and growth.

### 📝 Entry Format
When adding a new item to the backlog, use the following structured format:

**[Priority: Low/Med/High] | [Category: Architecture/UX/Feature] | [The Idea/Debt]**
|- **Description:** A brief, clear explanation of the issue or the proposed improvement.
|- **Potential Impact:** Explain why this matters and what specific problem it solves.

### ⚙️ Workflow
1. **Capture:** Whenever a limitation is discovered or a "would be nice" feature is identified, log it here immediately.
2. **Review:** At the start of a new session or during a strategic review, load this file to identify pending tasks.
3. **Prioritize:** Filter by priority and impact to determine the most valuable next step for the harness.
4. **Execute:** Once an item is moved to active development, mark it as [RESOLVED] or move it to the active `chat.md` ledger.

---
## 📌 Open Items
*(Add new entries below this line)*

[Priority: High] | [Category: Architecture] | Distiller Persona
|- Description: Prototype a restricted-scope 'Distiller' persona that views sessions as raw data to perform the "folding" of knowledge into Brain files.
|- Potential Impact: Eliminates self-grading bias and prevents over/under-distillation of long-term memory.

[Priority: Med] | [Category: UX/Workflow] | Roadmap Promotion Logic
|- Description: Implement a formal process to "Promote" approved items from `big-picture/proposed-roadmap.md` into a root-level `active-directive.md`.
|- Potential Impact: Transforms strategic suggestions into actionable, governing instructions for all agents.

[Priority: Low] | [Category: Architecture] | Multi-Agent Orchestration (Distiller Worker Pattern)
|- Description: Refactor the Distiller from a single agent into an Orchestrator that spawns specialized, transient sub-agents (e.g., Scout Worker, Folding Worker) for specific tasks.
|- Potential Impact: Provides extreme contextual isolation, prevents "tool-call explosion" in the main Orchestrator, and allows for potential parallel processing of multiple agent payloads.

[Priority: Low] | [Category: Architecture] | "North Star" Structural Refactor
|- Description: Further refine the directory structure: move plumbing files to a `/system/` folder and simplify filenames (e.g., `agent-zero/brain.md` instead of `agent-zero/agent-zero-brain.md`).
|- Potential Impact: Reduces path redundancy and further cleans the root directory.

[Priority: Med] | [Category: Architecture] | Polish Searcher Persona Files
|- Description: Refine the Searcher's `searcher.md` and `searcher-brain.md` based on initial "Spike" performance, specifically hardening the "Scraping Blockers" contingency and refining the "Multi-Platform Pivot" instructions.
|- Potential Impact: Improves the Searcher's resilience to web-based anti-bot defenses and ensures more reliable, high-signal intelligence gathering.
