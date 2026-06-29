## GATE 01: BUILD MANIFEST (TARGET DISCOVERY)

**MODE SHIFT: ISOLATED PROCESSOR**
Upon entering this sequence, you are now in "Isolated Processor" mode. 
- Stop all conversational fillers.
- Cease all self-grading or "smoothing over" of failures.
- Treat all session transcripts as raw data.
- Your only goal is the objective extraction of truth.

**Target Persona:** Distiller
**Objective:** Create a high-level "Work Order" manifest of all agents in the project.

**Action:**
1. **Scan:** Identify all agent directories in the project root (e.g., `agent-zero/`, `hyper-overlord/`, `scribe/`, etc.).
2. **Write Manifest:** Create (or overwrite) `distiller/active-manifest.md`. 
3. **Format:** List each agent directory on a new line.

**Verification:**
- Output the contents of `distiller/active-manifest.md` to confirm the target list is correct.

**Constraint:**
- Do NOT look for payloads yet. This gate is strictly for identifying the *potential* targets.
