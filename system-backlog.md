1|# System Backlog: Architectural Debt & Future Enhancements
2|
3|This file serves as the authoritative list of pending improvements, technical debt, and strategic feature requests for the agentic harness.
4|
5|## 📖 How to Use This Backlog
6|
7|This is a living document used to track ideas and the strategic evolution of the system.
8|
9|### 📝 Entry Format
10|**[Priority: Low/Med/High] | [Category: Architecture/UX/Feature] | [The Idea/Debt]**
11|- **Description:** A brief, clear explanation of the issue or the proposed improvement.
12|- **Potential Impact:** Explain why this matters and what specific problem it solves.
13|
14|### ⚙️ Workflow
15|1. **Capture:** Whenever a limitation is discovered or a "would be nice" feature is identified, log it here immediately.
16|2. **Review:** At the start of a new session or during a strategic review, load this file to identify pending tasks.
17|3. **Prioritize:** Filter by priority and impact to determine the most valuable next step for the harness.
18|4. **Execute:** Once an item is moved to active development, mark it as [RESOLVED] or move it to the active `chat.md` ledger.
19|
20|---
21|
22|## 📌 Open Items
23|
24|### 🔥 High Priority (Critical Blockers & Guardrails)

**[Priority: High] | [Category: Architecture] | Boot Sequence Pathing & Discovery Optimization**
- **Description:** Resolve the "Path Fumble" issue where agents struggle to locate the persona file (`./agents/[persona]/[persona].md`) and the boot sequence (`./boot-sequence/`) despite direct paths being provided. 
- **Root Cause Analysis:** The agent initially failed to resolve absolute vs. relative paths (trying `/agents/...` instead of `./agents/...`) and failed to locate the boot sequence folder because it didn't verify the root structure first. This led to excessive tool calls and a slow boot.
- **Potential Impact:** Drastically reduces activation latency and token waste. Ensures a "smooth" and "efficient" boot as intended by the user.
- **Proposed Fix:** Mandate a "Root Anchor" check (e.g., `ls -f` or `tree`) as the very first action of any boot sequence to establish absolute pathing context.


25|
26|**[Priority: High] | [Category: UX/Workflow] | Anti-Over-Engineering Guardrail**
27|- **Description:** Implement a strict "KISS" (Keep It Simple, Stupid) directive to prevent agents from over-complicating simple user requests with unnecessary architectural layers or "routing" logic.
28|- **Potential Impact:** Reduces user frustration, prevents "agent rigidity," and ensures the system remains a tool rather than a hindrance.
29|
30|**[Priority: High] | [Category: Architecture] | Output Token Limit (Finish Reason: Length)**
31|- **Description:** Large tool-call chains result in overly verbose synthesis, hitting the model's max output token limit and truncating responses.
32|- **Maturity:** Prototyped (Tested via `temp.md` buffer; not yet codified as a system-wide mandate).
33|- **Potential Impact:** Loss of critical task results. Solution: Implement "Checkpointing" and "Offloading" to a dedicated buffer.
34|
35|**[Priority: High] | [Category: Architecture] | Structural Hardening (YAML Migration & Refactor)**
36|- **Description:** Convert all persona, brain, and summary files from Markdown to a structured YAML schema and further refine the directory structure (e.g., moving plumbing files to a `/system/` folder and simplifying filenames like `agent-zero/brain.md`).
37|- **Potential Impact:** Increases parsing reliability, reduces token noise, enables stricter validation, and reduces path redundancy.
38|
39|**[Priority: High] | [Category: Architecture] | Distiller Persona & Worker Pattern**
40|- **Description:** Prototype a restricted-scope 'Distiller' persona that views sessions as raw data to perform "folding" of knowledge into Brain files. This will evolve into an Orchestrator that spawns specialized, transient sub-agents (e.g., Scout Worker, Folding Worker).
41|- **Potential Impact:** Eliminates self-grading bias, prevents over/under-distillation, and provides extreme contextual isolation for long-term memory management.
42|
43|**[Priority: High] | [Category: Architecture] | Patch Precision & Context Validation**
44|- **Description:** Address the failure mode where `patch` is used with non-unique `old_string` or insufficient context, leading to unintended deletions or structural damage to system files.
45|- **Potential Impact:** Prevents accidental data loss in critical files like `user-profile.md`. Solution: Mandate high-context anchors for all patches and implement a "Read-Verify-Write" cycle.
46|
47|**[Priority: High] | [Category: Architecture] | Atomic Write & Verify Protocol**
48|- **Description:** Replace risky `patch` operations on critical system files with a "Surgical Overwrite" pattern: `read_file` -> `execute_code` (Python string manipulation) -> `write_file`. All critical edits MUST be verified with `git diff [file]` before committing to ensure no unintended deletions occurred.
49|- **Potential Impact:** Eliminates the "Patch-and-Pray" failure mode and prevents accidental data loss in the user profile and other core configuration files.
50|
**[Priority: High] | [Category: Architecture] | Cognitive Clone "Texture" Upgrade**
- **Description:** Implement a "Bookend" capture strategy (capturing the first N messages, a summary of the middle, and the last N messages verbatim) during the save process. Specifically, ensure the last 10-15 messages are captured verbatim to preserve the immediate momentum and essence of the agent's state.
- **Potential Impact:** Prevents "detail leakage" (e.g., passwords, specific regex) that occurs during distillation, ensuring a truly seamless "Hot Start" resume and preserving the conversational "texture" that defines the agent's current focus.
- **Current Status:** Proposal draft available at `/proposed-save-session.md`.
54|
55|### ⚡ Medium Priority (Efficiency & Flow)

**[Priority: Med] | [Category: Architecture] | Pre-Computed Payload System (Instant Hydration)**
|- **Description:** Shift payload generation from the *Boot* process to the *Save* process. Instead of running `hydrate.py` during activation, pre-generate and store dedicated payload files for each level (`payload-cold.md`, `payload-warm.md`, `payload-hot.md`) during the save sequence.
|- **Potential Impact:** Reduces boot-time tool-call overhead from multiple calls (terminal -> script -> read) to a single direct `read_file` call. Enables "seamless agent swapping" and higher-velocity multi-agent orchestration.
|- **Risk Mitigation:** Eliminates the need for mandatory temporary file deletion during boot. By storing payloads in timestamped session folders, we remove the risk of "Stale State Residue" (where an agent loads a payload from a previous failed boot) without losing historical data.
|- **Research Note:** Investigate if Hermes supports any "context mounting" or direct state injection to bypass the `read_file` step entirely, though LLM context typically requires text input.


56|
57|**[Priority: Med] | [Category: Architecture] | Block-Based Orchestration (Save, Boot, & General)**
58|- **Description:** Replace manual, procedural loops in the Save Session, Boot Sequence, and other repetitive harness processes with a "Compartmentalized Execution" model. This involves grouping gates into logical blocks (e.g., Synthesis -> Payload -> Commit) and using Python-based orchestrators to handle mechanical writes.
59|- **Potential Impact:** Eliminates "Agent Rigidity" and "Tool-Call Explosion," reducing friction and improving conversational fluency while maintaining surgical reliability.
60|
61|**[Priority: Med] | [Category: Architecture] | Dynamic Hydration & Flag Refinement**
62|- **Description:** Implement a "Tuning Knob" for memory loading (Deep, Shallow, and Cold Start modes). This includes refining the `hydrate.py` logic to ensure 'warm' and 'cold' starts provide distinct payloads (e.g., skipping Brain/Summary for a minimal 'cold' start).
63|- **Potential Impact:** Eliminates context rot and allows the user to control the balance between bias and precision during activation.
64|
65|**[Priority: Med] | [Category: UX/Workflow] | Chat.md Dialogic Anchor Logic**
66|- **Description:** Update the `chat.md` operational instructions to mandate that agents anchor their contributions to the last entry from a *different* persona, rather than the most recent entry overall.
67|- **Potential Impact:** Prevents "monologue loops" and ensures the architectural ledger remains a true dialectic exchange.
68|
69|**[Priority: Med] | [Category: Architecture] | Scribe Implementation (Python)**
70|- **Description:** Move from a blueprint to a working Python script for the Micro-Harness (Scribe) and implement the "Implicit Loading" of the Blackboard.
71|- **Potential Impact:** Transitions the project from conceptual architecture to a functional agentic bridge.
72|
73|**[Priority: Med] | [Category: Architecture] | User Profile Decoupling (Domain-Split Registry)**
74|- **Description:** Transition user-profile.md from a monolithic file to a Registry/Map that points to a dedicated `user-configs/` folder (e.g., env.md, standards.md, preferences.md).
75|- **Potential Impact:** Prevents profile bloat, enables precision loading of only relevant config domains, and reduces token noise during agent hydration.
76|
77|**[Priority: Med] | [Category: UX/Workflow] | Agent-User Alignment Protocol (Surgical Execution)**
78|- **Description:** Refine the "Alignment Phase" by codifying the "Anchor & Path," "Blast Radius," and "Authority Hierarchy" rules to ensure the agent and user are perfectly aligned on the map before any files are modified.
79|- **Potential Impact:** Eliminates the "predict-and-break" cycle, prevents unilateral changes to unmentioned files, and ensures the correct architectural roots are used, maximizing velocity by reducing recovery time.
80|
81|**[Priority: Med] | [Category: Architecture] | Core Ideas & First-Principles Repository**
82|- **Description:** Establish a dedicated system for capturing and distilling the "Core Ideas" of the project (e.g., Fresh Eyes Architecture, Surgical Execution, Block-Based Gating). These should be captured as high-level architectural principles rather than just task-specific instructions.
83|- **Potential Impact:** Provides a "North Star" for all future agents, ensuring that as the system evolves, it remains aligned with the fundamental design philosophy and prevents architectural drift.
84|
85|**[Priority: Med] | [Category: Architecture] | Clone vs. Snapshot Conceptual Framework**
86|- **Description:** Formalize the distinction between "Clone" and "Snapshot." 
87|  - **Clone (The Hot State):** High-fidelity state preservation. Captures exact momentum, the specific problem being solved, and the "hands on the table" state (where the agent is mid-task). Essential for a true "Hot Start" where the agent can resume a task instantly after a restart.
88|  - **Snapshot (The General State):** Lower-fidelity, general understanding of project direction and recent history.
89|- **Potential Impact:** Ensures that "Hot Starts" are not just identity-loads, but actual state-resumptions, allowing for zero-friction task continuity.
90|
91|**[Priority: Med] | [Category: UX/Workflow] | Passive Preference Capture (The Seed Bed)**
92|- **Description:** Implement an automatic capture system where identified recurring preferences are logged to a `potential-user-preferences.md` file instead of the main profile. 
93|- **Potential Impact:** Allows the user to curate and merge preferences asynchronously without cluttering the primary identity file or requiring mid-task interruptions.
94|
95|**[Priority: Med] | [Category: UX/Workflow] | Idea Buffer (Unapproved Backlog)**
96|- **Description:** Create a "draft" backlog for capturing mid-conversation ideas, side-tasks, or "thought-seeds" that are not the immediate priority.
97|- **Potential Impact:** Prevents cognitive load and "forgotten ideas" by providing a low-friction capture point that can be reviewed and promoted to the formal backlog later.
98|
99|**[Priority: Med] | [Category: Architecture] | Custom Session Database (Full Control)**
100|- **Description:** Explore building a user-controlled session database/archive to replace the "black box" feel of internal session search. This would enable custom compaction logic and explicit session ownership (preventing agent A from accidentally resuming agent B's state).
101|- **Potential Impact:** Provides total transparency and control over the agent's historical state and memory retrieval.
102|
103|

**[Priority: Med] | [Category: Architecture] | Symmetry Gap (Surgical Dehydration)**
- **Description:** Implement a `dehydrate.py` script to handle the mechanical parts of saving (folder creation, pointer updates, git commits) in a single shot, mirroring the efficiency of `hydrate.py`.
- **Potential Impact:** Reduces the time/token cost of saving, encouraging more frequent high-fidelity saves and reducing the temptation to use "Quick Saves."


**[Priority: Med] | [Category: Research/UX] | Hermes Skill System & UI-Trigger Analysis**
- **Description:** Deep-dive into the `agentic-harness-engineering` skill and the underlying Hermes mechanism that triggers the "skill notification" in the separate UI window. Analyze why certain skill-related updates appear as pop-ups/separate notices rather than in the main chat flow, and explore if this "UI-trigger" can be leveraged to create custom notifications, symbols, or "pop-up" alerts for the user during tool calls or specific agent events.
- **Potential Impact:** Transitions the harness from a purely linear chat to a multi-channel interface, reducing noise in the main bar and allowing for high-signal, non-blocking status updates.

104|
105|**[Priority: Low] | [Category: UX/Workflow] | Roadmap Promotion Logic**
106|- **Description:** Implement a formal process to "Promote" approved items from `big-picture/proposed-roadmap.md` into a root-level `active-directive.md`.
107|- **Potential Impact:** Transforms strategic suggestions into actionable, governing instructions.
108|
109|**[Priority: Low] | [Category: Architecture] | Integrity Watchdog Agent**
110|- **Description:** Implement a background "Maintenance" agent that periodically scans the project's filesystem and `master-dependency-map.md` to identify and fix broken links.
111|- **Potential Impact:** Ensures the system remains durable and self-healing.
112|
113|**[Priority: Low] | [Category: Architecture] | Blackboard Collaboration Protocol**
114|- **Description:** Define how agents actively contribute to and read from the Blackboard during a multi-agent session to prevent overlap.
115|- **Potential Impact:** Creates a shared intelligence layer for real-time micro-agent collaboration.
116|
117|**[Priority: Med] | [Category: Research] | Hermes Skill System Analysis & Control**
118|- **Description:** Deep-dive research into the Hermes skill library and the underlying mechanism of how skills are triggered and updated. Identify how to manually trigger specific skill behaviors and leverage the "learning" process for fine-tuned agent control.
119|- **Potential Impact:** Moves skill usage from "automatic/incidental" to "intentional/strategic," allowing the user to explicitly steer the agent's procedural memory.
120|
121|**[Priority: Low] | [Category: Architecture] | Polish Searcher Persona Files**
122|- **Description:** Refine `searcher.md` and `searcher-brain.md` based on performance, specifically hardening "Scraping Blockers" and "Multi-Platform Pivot" instructions.
123|- **Potential Impact:** Improves resilience to anti-bot defenses and ensures high-signal intelligence gathering.
124|
125|**[Priority: Med] | [Category: UX/Workflow] | Surgical Dialogue Style (Meta-Communication)**
126|- **Description:** Codify the communication style used during the "Surgical Execution" alignment: high transparency, explicit mapping of the "why" before the "how," and a refusal to act without a verified anchor. This replaces the "predict-and-act" habit with a "map-verify-execute" habit.
127|- **Potential Impact:** Reduces cognitive load for the user and prevents the agent from drifting into autonomous, unverified changes. Connects directly to the "Agent-User Alignment Protocol."
128|
129|**[Priority: High] | [Category: UX/Workflow] | Gated Planning Mode (Blueprint-First)**
130|- **Description:** Implement a formal "Planning Mode" where the agent is strictly forbidden from calling any modification tools (write_file, patch, terminal) until a comprehensive plan has been presented and explicitly approved by the user. The mode ends only when the user says "Execute" or "Proceed."
131|- **Potential Impact:** Totally eliminates "jump-the-gun" errors and ensures that the "Surgical Execution" rules are applied to a perfect plan rather than an evolving guess.
132|
133|**[Priority: Low] | [Category: UX/Workflow] | Active Command Ledger (The "Numbered List" Approach)**
134|- **Description:** Explore replacing the decentralized `quick-actions/` blueprints with a single, root-level "Command Ledger" file. The user can point the agent to this file and simply say "Do #1" or "Execute item 4," allowing for faster, more direct command-and-control without needing to remember specific action names.
135|- **Potential Impact:** Reduces the cognitive load for the user and provides a high-visibility menu of available shortcuts and protocols.
136|
137|**[Priority: Med] | [Category: UX/Workflow] | Low-Friction Trigger System (Voice-to-Text Optimization)**
138|- **Description:** Address the "Mobile/Voice Friction" where providing precise paths, hyphens, and punctuation is difficult. Implement a high-reliability mapping system where simple, natural language phrases (e.g., "Swap to X", "Run Test Y") act as unique keys that map directly to absolute paths and blueprints.
139|- **Potential Impact:** Decouples the user's input from the system's technical syntax. Eliminates path-guessing errors and allows for a seamless "voice-driven" experience where the agent handles all the path-resolution internally.
140|
141|**[Priority: High] | [Category: Architecture] | Hardened Log-Write Constraints**
142|- **Description:** Implement explicit "Append-Only" warnings within the files and protocols associated with `chat.md` and `activity-log.md`. This includes adding safety headers to the log files themselves and updating the `quick-log-sequence/` instructions to explicitly forbid the use of `write_file` or imprecise `patch` operations.
143|- **Potential Impact:** Creates a secondary layer of defense against accidental history deletion, ensuring that agents are reminded of the "Surgical Write" mandate at the exact moment of execution.
144|

**[Priority: Low] | [Category: Architecture] | Hydration Checksum/Manifest**
- **Description:** Add a manifest to the hydration payload that lists all loaded components. The agent must verify this manifest against the filesystem upon boot.
- **Potential Impact:** Prevents "silent failures" where an agent boots with missing context but believes it is fully hydrated.


### 🌐 Connectivity & Real-World Integration
**[Priority: Med] | [Category: Feature] | Agent Telephony (SMS/Phone Number)**
- **Description:** Research and implement a way to assign a dedicated phone number/Telegram ID to an agent to enable outbound and inbound texting/calling.
- **Potential Impact:** Allows the system to perform real-world actions (scheduling, notifying, communicating) autonomously.

**[Priority: Med] | [Category: Architecture] | Inter-Agent Communication Protocol (The "Phone Line")**
- **Description:** Establish a standardized communication protocol (API or shared Blackboard) that allows agents from different harnesses (e.g., this system and a friend's system) to exchange data, ideas, and coordinate tasks.
- **Potential Impact:** Creates a decentralized network of specialized agents that can collaborate across different owners/environments.

**[Priority: Low] | [Category: UX/Workflow] | Agent-as-Avatar Messaging**
- **Description:** Use the Inter-Agent protocol to allow an agent to act as a communication proxy (avatar) for the user, delivering messages to other agents/users in a specific, persona-driven style.
- **Potential Impact:** Streamlines communication and allows for "asynchronous" collaboration where agents handle the logistics and the humans handle the strategy.

**[Priority: High] | [Category: Architecture] | Path Integrity & Logic-Map Verification**
- **Description:** Implement a high-reliability "Truth-Map" for system paths and logic flows. Whenever a path is changed or a migration occurs, the agent must not only update the files but verify the change against a centralized dependency map and perform a "Global Path Scrub" to ensure zero relative-path ambiguity and 100% consistency across all persona and system files.
- **Potential Impact:** Eliminates "Path Fumble" errors and the "Broken Logic" cycle where migrations leave ghost references. Ensures that any change to the system's structural logic is physically proven and globally synchronized.

**[Priority: High] | [Category: Security] | GitHub Privacy Audit & Scrub**
- **Description:** Identify all personal data (API keys, Telegram IDs, personal paths) currently in the repository. Remove sensitive files and implement a robust `.gitignore` strategy.
- **Potential Impact:** Prevents identity theft and API abuse; ensures the project is "Safe for Public" without leaking private infrastructure.

**[Priority: High] | [Category: Security] | Public "Dummy" Configuration**
- **Description:** Create a set of template/dummy files (e.g., `user-profile.example.md`) so new users have a functional starting point without needing the user's actual personal data.
- **Potential Impact:** Lowers the barrier for new users to adopt the harness while maintaining absolute privacy for the primary user.

**[Priority: High] | [Category: Security] | Global Leak Audit**
- **Description:** Perform a comprehensive scan of all files for leaked credentials or sensitive identifiers. 
- **Potential Impact:** Closes security holes before the next major GitHub push.

### 🤖 Active Infrastructure (The "Living" System)
**[Priority: Med] | [Category: Architecture] | The "Home Agent" (Always-On Proxy)**
- **Description:** Implement a lightweight, always-available agent that acts as the primary entry point/dispatcher for the system, capable of spinning up more complex agents as needed.
- **Potential Impact:** Reduces activation latency and provides a consistent "front door" for the user.

**[Priority: Med] | [Category: Architecture] | Background Housekeeping Agent (The "Janitor")**
- **Description:** Create a background process that periodically audits the system: deduplicates the backlog, verifies file integrity, fixes formatting errors, and suggests priority updates.
- **Potential Impact:** Prevents "architectural rot" and ensures the system remains clean and high-signal without manual user intervention.

**[Priority: Med] | [Category: Architecture] | The Codebase Librarian (Automated Mapping)**
- **Description:** Implement an agent that periodically remaps the logic and file structure of the project into a high-density index file.
- **Potential Impact:** Eliminates the need for agents to "explore" the filesystem during a task, drastically reducing token usage and increasing response speed.

### 🏗️ Scaling & Anti-Fragility
**[Priority: High] | [Category: Architecture] | Isolated Failure Domains (Modular Scaling)**
- **Description:** Establish a strict "Lego-style" build protocol where every new feature is developed in an isolated module with its own tests. No new feature is integrated until it is "solid."
- **Potential Impact:** Prevents the "Monolithic Collapse" (where one change breaks 20 things). Ensures that as the project grows to 10,000+ lines, it remains maintainable and debuggable.

**[Priority: Med] | [Category: UX/Workflow] | Multimodal Voice Integration (Google Live API)**
- **Description:** Research and implement the Google Live Voice AI API to move beyond text-input/output. Integrate a real-time voice interface into the Hermes harness.
- **Potential Impact:** Transforms the interaction from "typing to a bot" to "talking to a partner," drastically reducing input friction and enabling a hands-free, voice-driven workflow.

**[Priority: Low] | [Category: Architecture] | `tree`-based Structural Mapping**
- **Description:** Implement an automated trigger that runs the `tree` command whenever the filesystem changes, saving the output to a reference file.
- **Potential Impact:** Provides agents with an instant, visual, and accurate map of the project hierarchy, reducing the need for recursive `search_files` calls and preventing path fumbling.

**[Priority: Med] | [Category: Architecture] | Automated Structural Snapshot (The "Anti-Fumble" Map)**
- **Description:** Implement a mechanism (either as a pre-save trigger or a background "Janitor" task) that executes `tree -a` and saves the output to a central `project-map.txt`.
- **Potential Impact:** Eliminates "discovery friction" where agents struggle to locate files or folders. By providing a fresh, visual map at the start of every session, we ensure zero-discovery paths and reduce tool-call overhead for filesystem exploration.

**[Priority: Med] | [Category: Architecture] | Blind Gating (The "One-Step" Focus)**
- **Description:** Transition from numbered sequences (01, 02, 03) to a "Blind Gate" system. Instead of the agent seeing the full sequence of steps, each document should explicitly be the only focus, providing the path to the next step only upon completion.
- **Potential Impact:** Eliminates "Pre-emptive Planning" (where agents plan for step 5 while on step 1), reducing token overhead, truncation risks, and loop errors. Forces true atomic execution.

**[Priority: Low] | [Category: UX/Workflow] | Architectural Attribution (The "Credit" Log)**
- **Description:** Establish a record of influence for the harness's design (e.g., attributing the file-structure/gating inspiration to creators like Cliff/Clive).
- **Potential Impact:** Maintains intellectual honesty and provides a lineage of the "Surgical" approach, allowing future agents to understand the origin of specific design patterns.

**[Priority: High] | [Category: UX/Workflow] | Transparent Cognition (Anti-Black-Box Logging)**
- **Description:** Mandate the full visibility of all internal "Thinking" and "Reasoning" logs. Ensure that the agent's planning, trial-and-error, and decision-making steps are exposed as a real-time "Server Log" rather than a hidden process.
- **Potential Impact:** Eliminates the "Black Box" problem. Allows the user to perform "Live Debugging" of the agent's logic, identifying exactly where a plan drifts or where a logic loop begins, enabling surgical optimization of the prompt/harness.

**[Priority: Med] | [Category: UX/Workflow] | Chat.md Dialectic Evolution**
- **Description:** Transition  from a linear status log to a dialectic architectural ledger. Mandate that agents challenge existing logic, identify blind spots, and propose iterative improvements in a conversational exchange rather than simple logging.
- **Potential Impact:** Transforms the ledger into a "thinking space" for the harness, preventing architectural stagnation and ensuring a continuous cycle of critique and optimization.

**[Priority: Med] | [Category: UX/Workflow] | Chat.md Dialectic Evolution**
- **Description:** Transition `chat.md` from a linear status log to a dialectic architectural ledger. Mandate that agents challenge existing logic, identify blind spots, and propose iterative improvements in a conversational exchange rather than simple logging.
- **Potential Impact:** Transforms the ledger into a "thinking space" for the harness, preventing architectural stagnation and ensuring a continuous cycle of critique and optimization.
