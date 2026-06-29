# Protocol: Session Snapshot & State Save (Hard-Gated Pipeline)

**Objective:** Capture the current session state into a portable snapshot and update long-term memory. 

**CRITICAL RULE:** This is a HARD-GATED pipeline. You MUST complete each gate in order. Do NOT skip, combine, or parallelize steps. You MUST verify the output of the current gate before proceeding to the next.

---

## 🛑 PRE-FLIGHT CHECK
Before starting, you must explicitly state: *"Starting save pipeline for [Persona Name]."*

---

## GATE 1: IDENTITY & MAPPING
**Action:**
1. **Identify:** Confirm the current active persona.
2. **Map:** Assign the corresponding session folder:
   - `agent-zero` -> `agent-zero-sessions/`
   - `hyper-overlord` -> `hyper-overlord-sessions/`
   - `scribe` -> `scribe-sessions/`
   - `big-picture` -> `big-picture-sessions/`
**Verification:** State the persona and the folder path. If ambiguous, STOP and ask the user.

## GATE 2: TEMPORAL DISTILLATION
**Action:** Analyze the current session history and extract the following four elements into your active context:
- **The Delta:** What was achieved? What specifically changed in the project?
- **The Logic:** Why were these decisions made? (The "Reasoning").
- **The Pointer:** The exact last action completed.
- **The Queue:** The immediate next steps/TODOs.
**Verification:** List these four elements briefly in the chat to confirm extraction.

## GATE 3: SESSION SUMMARY (THE HARD COPY)
**Action:**
1. **Locate:** Find or create the persona's summary file in the ROOT directory (e.g., `hyper-overlord-summary.md`).
2. **Synthesize:** Combine the **Temporal Distillation** (Gate 2) with high-level themes and critical goals.
3. **Compact:** Distill this into a high-density summary.
4. **Record:** Append to the file using the format: `[Timestamp]: [Summary]` followed by one empty line.
**Verification:** Read back the last 3 lines of the summary file to confirm the write.

## GATE 4: USER PROFILE UPDATE (GLOBAL MEMORY)
**Action:**
1. **Read:** Load `user-profile.md`.
2. **Compare:** Compare the **last entry** of the summary file (Gate 3) against the current profile.
3. **Update:** Append only new, non-redundant global preferences or environment constraints.
**Verification:** State exactly what was added to the profile, or state "No updates needed."

## GATE 5: PERSONA BRAIN UPDATE (LONG-TERM MEMORY)
**Action:**
1. **Locate:** Find the corresponding brain file (e.g., `hyper-overlord-brain.md`).
2. **Read:** Load the current contents of the brain file.
3. **Compare:** Compare the **last entry** of the summary file (Gate 3) against the brain.
4. **Update:** Append new permanent truths, architectural decisions, or learned lessons.
**Verification:** Read back the appended section of the brain file.

## GATE 6: ENVIRONMENT AUDIT
**Action:**
1. **Scan:** List every file created or modified during this session.
2. **Verify:** Confirm the absolute paths to all key artifacts.
**Verification:** Provide a bulleted list of modified files.

## GATE 7: SNAPSHOT COMMIT (THE SAVE GAME)
**Action:** 
1. **Generate:** Create a file in the persona's session folder (Gate 1) using the format `YYYY-MM-DD_HHmm_snapshot.md`.
2. **Populate:** Use the data from **Gate 2 (Distillation)** and **Gate 6 (Audit)** to fill the template below.

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

**Verification:** Provide the absolute path of the snapshot and confirm: *"State is durable and ready for recovery."*
