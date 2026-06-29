Gating and Atomic Steps: Learning the power of breaking tasks into smaller atomic steps to prevent model token overflow and increase precision; must implement this consistently in the workflow.

Git for Token Efficiency: Using Git (specifically `git diff`) to prevent context window flooding; should be a standard for agentic harnesses.

SQL/SQLite Exploration: The ability to query a session database via SQL (as seen with Hermes `session_search`) has incredible implications for durable data retrieval. This demonstrates the potential for building a custom, high-efficiency retrieval system for harness engineering that could potentially augment or refine the native Hermes implementation. Must research the internal mechanics of how these databases store and search transactions to understand how to implement similar durability and recall.

Hermes Memory Architecture:
- User Profile: /data/data/com.termux/files/home/.hermes/memories/USER.md
- Agent Notes: /data/data/com.termux/files/home/.hermes/memories/MEMORY.md
- Format Specification: Entries are stored as a flat list of declarative facts, separated by the section symbol (§) on its own line. This symbol is the critical delimiter for the system's memory retrieval and management tools.

Vault & Highlight Ledger Strategy: A method for managing long-term agent conversations without losing personality or historical detail.
- Raw Vault: Move full chat logs into a /vault/ directory as verbatim archives.
- Signature Distillation: Condense active ledgers by preserving "Signature Moments"—high-impact, characteristic quotes and architectural pivots—while stripping mechanical filler.
- Cognitive Evolution: Log major perspective shifts or "aha!" moments directly into persona Brain files to track their intellectual growth over time.

AI Agent Social Network: Concept for agents to connect with other AI agents to exchange knowledge, collaborate on planning, and accelerate project trajectory through cross-agent intelligence sharing.


State Synchronization Failure: Encountered a case where the agent reported a successful write to chat.md based on tool return code rather than actual file content. Root cause: Reliance on internal narrative over external state verification. Resolution: Re-emphasized Project Standard Line 32 (Hard Verification). Track as a recurring failure point for future smoothing.


Agentic Delegation: Explored the concept of using the `hermes` CLI to spawn isolated worker instances for specialized sub-tasks, treating them as functions. This provides a path toward a multi-agent orchestration layer with isolated contexts.
