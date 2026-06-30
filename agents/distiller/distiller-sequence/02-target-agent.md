## GATE 02: TARGET AGENT (WORK ORDER SELECTION)
**Target Persona:** Distiller
**Objective:** Select the next agent from the manifest to process.

**Action:**
1. **Read Manifest:** Load `distiller/active-manifest.md`.
2. **Select:** Pick the **first** line (the first agent) from the list.
3. **Set Context:** Store this agent's path as the `CURRENT_TARGET`.
4. **Update Manifest:** Remove the selected agent from `distiller/active-manifest.md` (or mark it as "in-progress").

**Verification:**
- State clearly: "Current Target: [agent-path]".
