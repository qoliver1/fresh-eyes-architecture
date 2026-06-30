# Delta Folding Logic (Lightweight Integration)

**Target Persona:** Distiller
**Objective:** Extract progress signals from a DELTA payload and append them to the persona's high-density log.

**Action:**
1. **Read Payload:** Read the content of `CURRENT_PAYLOAD_PATH`.
2. **Identify Target Log:** Determine the persona from the path and target `[persona]-delta-log.md`.
3. **Extract Signal:** Extract the "Operational Record" (Delta) section from the payload.
4. **Append to Log:** Append the extracted signal to `[persona]-delta-log.md` with a timestamp.
5. **Update Summary:** Add a one-line summary of this delta to `distiller/distiller-summary.md`.

**Verification:**
- Confirm the delta log was updated and the summary was refreshed.
