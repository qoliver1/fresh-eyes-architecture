## GATE 01: SCAN & SORT (THE INTAKE)
**Target Persona:** Distiller
**Objective:** Identify all pending intelligence in the project.

**Action:**
1. **Scan:** Find all agent directories.
2. **Locate Inboxes:** For each agent, check for `/[persona]/inbox/`.
3. **Collect & Sort:** List all files in all inboxes and sort them chronologically (Oldest $\rightarrow$ Newest).
4. **Write Work Order:** Save this sorted list to `distiller/current-work-order.md`.

**Verification:**
- Output the contents of `distiller/current-work-order.md` to confirm the queue is ordered correctly.

**Constraint:**
- If no files are found in any inbox, terminate the sequence and report "No pending intelligence."
