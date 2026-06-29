## GATE 06: LOOP CHECK (CONTINUATION)
**Target Persona:** Distiller
**Objective:** Determine if there are more agents left in the manifest.

**Action:**
1. **Read Manifest:** Check `distiller/active-manifest.md`.
2. **Decide:**
    - **If agents remain:** Loop back to `02-target-agent.md`.
    - **If manifest is empty:** Proceed to `07-finalize-run.md`.

**Verification:**
- State: "Queue empty. Moving to finalization."
- OR: "Next target ready. Re-looping."
