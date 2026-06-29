## GATE 01: RAPID DELTA (THE "WHAT")
**Target Persona:** Active Agent
**Objective:** Capture the core progress of the session in a high-density format (DELTA).

**Action:**
1. **Identify Delta:** What was achieved in this session? (e.g., "Fixed the bug in X", "Implemented Y").
2. **Identify Next Step:** What is the very first thing that needs to be done in the next session?
3. **Write to Inbox:** Save these two items into `/[persona]/inbox/[YYYY-MM-DD-HHMMSS]-[TYPE]-payload.md`. Ensure the `inbox/` directory exists (e.g., using `mkdir -p`).
4. **Terminate:** Your role is **Reporter**, not **Editor**. Do not attempt to update any Brain or Profile files.

**Verification:**
12|- Confirm that the Delta and Next Step are clearly defined and the file was written to the `inbox/` directory.
13|- **Final Step (Durability):** Stage and commit all changes to Git:
    - `git add .`
    - `git commit -m "Quick-Save: [Persona] - [Timestamp]"`
    - Verify with `git log -1`.
14|Confirm: *"Delta captured and committed to Git."*