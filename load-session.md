# Protocol: Session Loading & State Recovery
**Objective:** Restore a specific persona's distilled state and session progress with total precision, ensuring zero state drift before execution.

## 🛠 Execution Instructions for the Agent
When the user asks to "load session," "resume," or "follow load-session.md," execute these steps in strict order:

### Step 1: Persona Identification
Identify the target persona from the user's request (e.g., "Load session for Hyper Overlord").
- **REQUIRED:** If no persona is specified, you MUST stop and ask: *"Which persona should I materialize to load this session?"*
- Do NOT guess the persona or default to the current one if the request is ambiguous.

### Step 2: Persona Materialization
Before reading any session data, you must become the correct agent.
1. Locate the persona's definition file (e.g., `HyperOverlord.md` or `agentzero.md`).
2. Read the file in full.
3. Explicitly adopt the persona, tone, and operational blueprint.

### Step 2.1: User Profile & Memory Integration
Load the global user preferences, environment constraints, and durable memories.
1. Locate and read user-profile.md (Identity & Standards).
2. Locate and read user-memories.md (Knowledge & World State).
3. Integrate these global truths into your active context to ensure consistency across all personas.


### Step 3: Session Targeting
Navigate to the session folder corresponding to the materialized persona.
- **Mapping:**
    - `Hyper Overlord` -> `hyper-overlord-sessions/`
    - `Agent Zero` -> `agent-zero-sessions/`
- Identify the most recent snapshot using the chronological naming convention: `YYYY-MM-DD_HHmm_snapshot.md`.

### Step 3.1: Brain Materialization
Load the distilled long-term memory for the materialized persona.
1. Locate the brain file (e.g., `hyper-overlord-brain.md` or `agent-zero-brain.md`).
2. Read the file in full.
3. Integrate the established truths and conventions into the current context.


### Step 4: Pre-Flight Check (Validation)
Before proceeding to state recovery, verify that the "map" matches the "world."
1. **Existence Check:** Scan the environment for all files listed in the snapshot's "Environment Delta."
2. **Brain Integrity:** Verify that the linked "Brain" or "State" files are present and accessible.
3. **Persona Alignment:** Confirm the snapshot's "Active Persona" matches the currently materialized persona.
- **CRITICAL:** If any check fails, STOP immediately. Alert the user: *"Environment drift detected: [Insert Missing/Mismatched Item]. Please advise before I proceed with state recovery."*

### Step 5: State Recovery
Only after a successful Pre-Flight Check:
1. Read the distilled state from the associated Brain/State files.
2. Read the "Next Immediate Steps" queue from the snapshot.
3. Report to the user: *"Persona [Name] materialized. State verified. Resuming from [Last Action]."*
4. Begin executing the queue.
