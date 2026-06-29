## GATE 05: ARCHIVE PAYLOAD (CLEANUP)
**Target Persona:** Distiller
**Objective:** Move the processed payload to the target agent's archive to prevent re-processing.

**Action:**
1. **Locate:** Identify the `[persona]-latest-payload.md` that was just processed.
2. **Create Archive:** Create `[CURRENT_TARGET]/archived/` if it doesn't exist.
3. **Move:** Move the payload to `[CURRENT_TARGET]/archived/[timestamp]-payload.md`.

**Verification:**
- Confirm the file has been moved and the `latest-payload.md` is gone from the target's root.
