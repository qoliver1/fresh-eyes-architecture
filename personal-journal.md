# Friction Log: Strategic Ideas & Refinements
*This is a summary of high-level architectural shifts and "what if" scenarios discussed during sessions. Use this to prevent loss of complex conceptual reasoning.*

## 💡 Idea: Multi-Agent Distillation Orchestration
**Context:** Discussed during the Distiller Refactor session.
**Core Concept:** Instead of the Distiller being a single-agent loop, move to an **Orchestrator-Worker** pattern. The Distiller acts as the high-level manager (Orchestrator) that spawns transient, single-purpose sub-agents (Workers) for tasks like "Scouting" and "Folding."
**Rationale:**
- **Contextual Isolation:** Prevents the Orchestrator's context window from being polluted by messy file-system logs or "tool-call explosion."
- **Error Containment:** Sub-agent failures are contained and reported as structured signals, allowing the Orchestrator to maintain stability.
- **Scalability:** Enables future parallel processing of multiple agent payloads.
**Status:** Captured in `system-backlog.md` as [Priority: Low] | Multi-Agent Orchestration.

## 💡 Idea: Buffered Execution Model (Cognitive Scratchpads)
**Context:** Identified during the Hyper Overlord swap and token truncation failures.
**Core Concept:** Mandate that agents use a temporary file (e.g., `temp.md`) as a buffer for all internal reasoning and tool-output dumping during complex workflows.
**Rationale:**
- **Bypass Token Limits:** Decouples the "Thinking/Execution" phase (which can be massive) from the "Synthesis/Reporting" phase (which is capped).
- **Full Transparency:** Provides a complete, un-truncated audit trail of every step the agent took.
- **State Recovery:** If a turn is interrupted, the agent can resume exactly where it left off by reading the buffer.
**Status:** Logged in `system-backlog.md` as [Priority: High] | Output Token Limit.

