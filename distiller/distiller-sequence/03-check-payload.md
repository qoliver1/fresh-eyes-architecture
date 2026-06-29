## GATE 03: CHECK PAYLOAD (STATUS VERIFICATION)
**Target Persona:** Distiller
**Objective:** Verify if the current target agent has a pending payload.

**Action:**
1. **Locate:** Look for `[CURRENT_TARGET]/[persona]-latest-payload.md`.
2. **Decision:**
    - **If payload exists:** Proceed to `04-execute-folding.md`.
    - **If NO payload exists:** Proceed to `05-archive-target.md` (to finalize this agent).

**Verification:**
- State: "[Target] has a pending payload. Proceeding to folding."
- OR: "[Target] has no pending payload. Skipping to archive."
