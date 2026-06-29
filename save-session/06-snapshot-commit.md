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