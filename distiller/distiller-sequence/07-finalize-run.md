## GATE 07: FINALIZE RUN (TERMINATION)
**Target Persona:** Distiller
**Objective:** Conclude the maintenance cycle and report the results.

**Action:**
1. **Summary:** Write a high-density summary of the entire batch run (number of agents processed, number of payloads folded) into `distiller-summary.md`.
2. **Snapshot:** Create a snapshot of the Distiller's own state in `distiller-sessions/`.
8|3. **Terminate:** Signal completion.
9|4. **Mode Reversion:** Exit "Isolated Processor" mode and return to your conversational Persona. Greet the user and report that the distillation cycle is complete.
10|
11|**Verification:**
12|- Provide the final batch summary for the user.
