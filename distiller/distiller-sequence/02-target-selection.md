## GATE 02: TARGET SELECTION (THE PICK)
**Target Persona:** Distiller
**Objective:** Select the next item from the work order.

**Action:**
1. **Read Work Order:** Load `distiller/current-work-order.md`.
2. **Pick Oldest:** Select the first (oldest) file path from the list.
3. **Set Context:** Store this path as `CURRENT_PAYLOAD_PATH`.
4. **Update Work Order:** Remove the selected line from `distiller/current-work-order.md`.

**Verification:**
- State clearly: "Targeting payload: [path]".
