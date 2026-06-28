# Protocol: Session Snapshot & State Save (Linear Pipeline)
**Objective:** Capture the current session state into a portable snapshot while updating long-term memory. Follow this pipeline sequentially. Do NOT skip or combine steps.

## 🛠 Linear Execution Pipeline

### Gate 1: Identity Verification
1. **Identify:** Determine the current active persona.
2. **Map:** Assign the correct session folder (e.g., `hyper-overlord-sessions/` or `agent-zero-sessions/`).
3. **Guardrail:** If identity is ambiguous, STOP and ask the user before proceeding.

### Gate 2: Temporal Distillation (Operational Extraction)
Extract the following from the session history to create a structured operational record:
- **The Delta:** What was achieved? What changed?
- **The Logic:** The reasoning behind specific decisions.
- **The Pointer:** The exact last action completed.
- **The Queue:** The immediate next steps/TODOs.
*Keep this data active in context for the next gates.*

### Gate 3: Session Summary (The Hard Copy)
1. **Locate:** Find or create the persona's summary file based on the identity established in Gate 1 (e.g., `hyper-overlord-summary.md`).
2. **Synthesize:** Combine the **Temporal Distillation** (Gate 2) with high-level imperative themes, critical contacts, and high-value project/goal data found in the session.
3. **Compact:** Distill this synthesis into a concise, high-density summary.
4. **Record:** Append to the file using the format: `[Timestamp]: [Summary]` followed by one empty line. This is now the primary reference for all subsequent updates.

### Gate 4: User Profile Update (Global Memory)
1. **Read:** Load `user-profile.md`.
2. **Compare:** Compare the **last entry** of the persona's summary file (established in Gate 3) against the user profile.
3. **Update:** Append only new, non-redundant global preferences or environment constraints to `user-profile.md`.

### Gate 5: Persona Brain Update (Long-term Memory)
1. **Locate:** Find the corresponding brain file (e.g., `hyper-overlord-brain.md`).
2. **Read:** Load the current contents of the brain file.
3. **Compare:** Compare the **last entry** of the persona's summary file (established in Gate 3) against the brain file.
4. **Update:** Append new permanent truths or architectural decisions to the brain file.

### Gate 6: Environment Audit
1. **Scan:** List all files created or modified during this session.
2. **Verify:** Confirm the paths to all key artifacts created.

### Gate 7: Snapshot Commit
Generate a file in the persona's session folder using the format `YYYY-MM-DD_HHmm_snapshot.md`. Use the data extracted in **Gate 2** and **Gate 6** to fill the template.

**Snapshot Template:**
---
## 📸 Session Snapshot: [Date]
**Timestamp:** [ISO 8601]
**Active Persona:** [Name]

### 🛠 Environment Delta
- **Files Modified:** [Absolute paths]
- **Key Artifacts:** [Critical files]

### 🧠 Knowledge Distillation
- **Key Discoveries:** [Bullet points]
- **Decision Log:** [Why X over Y]
- **User Preferences:** [New findings]

### 📍 Current Pointer
- **Last Action:** [Description]
- **Current State:** [System status]

### ⏭ Next Immediate Steps
- [ ] [Task 1]
- [ ] [Task 2]
---

### Finalization
1. Provide the absolute path of the snapshot.
2. Confirm the state is durable and ready for recovery.
