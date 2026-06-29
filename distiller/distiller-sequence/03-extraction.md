## GATE 03: EXTRACTION (TYPE IDENTIFICATION)
**Target Persona:** Distiller
**Objective:** Determine the payload type and prepare for folding.

**Action:**
1. **Read Payload:** Read the file at `CURRENT_PAYLOAD_PATH`.
2. **Identify Type:**
   - If filename contains `-FULL-`, type = `FULL`.
   - If filename contains `-DELTA-`, type = `DELTA`.
3. **Set Context:** Store `CURRENT_PAYLOAD_TYPE`.

**Verification:**
- State: "Payload type identified as [FULL/DELTA]."
