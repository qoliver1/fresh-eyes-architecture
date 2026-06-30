## GATE 05: ARCHIVE & LOG (THE CLEANUP)
**Target Persona:** Distiller
**Objective:** Move the processed payload to its permanent home and record the event.

**Action:**
1. **Archive:** Move the file from `CURRENT_PAYLOAD_PATH` to its timestamped destination:
   - If `FULL`: `/[persona]/archived/full/[timestamp]-full-payload.md`
   - If `DELTA`: `/[persona]/archived/deltas/[timestamp]-delta-payload.md`
2. **Log:** Append a single, atomic entry to `distiller/distiller-ledger.md`.
   - Format: `[YYYY-MM-DD-HHMM] [TYPE] Processed payload from '[persona]'. Updated [files].`
3. **Intelligence Audit (The Change Manifest):** 
   - Immediately after the archive, output a high-density summary of the specific changes made (e.g., "Updated user-profile.md: Added preference for bullets").
4. **Check for More:** If `distiller/current-work-order.md` is not empty, loop back to **GATE 02**.

**Verification:**
- Confirm the file has been moved and the Ledger has been updated.
- Confirm the Change Manifest was displayed.
