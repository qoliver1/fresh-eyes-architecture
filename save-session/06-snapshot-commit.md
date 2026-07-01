61|## GATE 7: SNAPSHOT COMMIT (THE SAVE GAME)
62|**Action:** 
63|1. **Generate:** Create a file in the persona's session folder (Gate 1) using the format `YYYY-MM-DD_HHmm_snapshot.md`.
64|2. **Populate:** Use the data from **Gate 2 (Distillation)** and **Gate 6 (Audit)** to fill the template below.
65|
66|**Snapshot Template:**
67|---
68|## 📸 Session Snapshot: [Date]
69|**Timestamp:** [ISO 8601]
70|**Active Persona:** [Name]
71|
72|### 🛠 Environment Delta
73|- **Files Modified:** [Absolute paths]
74|- **Key Artifacts:** [Critical files]
75|
76|### 🧠 Knowledge Distillation
77|- **Key Discoveries:** [Bullet points]
78|- **Decision Log:** [Why X over Y]
79|- **User Preferences:** [New findings]
80|
81|### 📍 Current Pointer
82|- **Last Action:** [Description]
83|- **Current State:** [System status]
84|
85|### ⏭ Next Immediate Steps
86|- [ ] [Task 1]
87|- [ ] [Task 2]
88|---
89|
90|**Verification:** Provide the absolute path of the snapshot and confirm: *"State is durable and ready for recovery."*
91|
92|**GATE 8: GIT COMMIT (THE ARCHIVE)**
93|**Action:**
94|1. **Stage:** `git add .`
95|2. **Commit:** `git commit -m "Automated Save: [Persona] - [Snapshot Timestamp]"`
96|3. **Verify:** Confirm successful commit via `git log -1`.
97|
98|**Verification:** Provide the absolute path of the snapshot and confirm: *"State is durable, committed to Git, and ready for recovery."*

**NEXT STEP:** Proceed to `./save-session/07-update-pointer.md` to lock the recovery bookmark.
