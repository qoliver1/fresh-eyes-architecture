## GATE 04: EXECUTE FOLDING (CORE LOGIC)
**Target Persona:** Distiller
**Objective:** Perform the surgical integration of payload data into the target agent's memory.

**Action:**
1. **Ingest:** Read the `[persona]-latest-payload.md` from the `CURRENT_TARGET`.
2. **Run Profile Fold:** Execute `distiller/folding-tools/01-profile-folding.md`.
3. **Run Brain Fold:** Execute `distiller/folding-tools/02-brain-folding.md`.

**Verification:**
- Confirm that `user-profile.md` and the `[persona]-brain.md` for the target agent have been updated.
