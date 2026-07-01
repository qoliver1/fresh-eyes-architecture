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

### ⚡ Medium Priority (Efficiency & Flow)

**[Priority: Med] | [Category: Architecture] | Block-Based Orchestration (Save, Boot, & General)**
- **Description:** Replace manual, procedural loops in the Save Session, Boot Sequence, and other repetitive harness processes with a "Compartmentalized Execution" model. This involves grouping gates into logical blocks (e.g., Synthesis $\rightarrow$ Payload $\rightarrow$ Commit) and using Python-based orchestrators to handle mechanical writes.
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

**[Priority: Low] | [Category: Research] | Hermes Native Skill Audit**
- **Description:** Review pre-installed Hermes Agent skills to identify patterns or workflows that can be adapted into the custom harness.
- **Potential Impact:** Prevents "reinventing the wheel" and leverages professionally developed skill patterns.

**[Priority: Low] | [Category: Architecture] | Polish Searcher Persona Files**
- **Description:** Refine `searcher.md` and `searcher-brain.md` based on performance, specifically hardening "Scraping Blockers" and "Multi-Platform Pivot" instructions.
- **Potential Impact:** Improves resilience to anti-bot defenses and ensures high-signal intelligence gathering.
