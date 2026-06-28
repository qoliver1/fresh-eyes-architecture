# Specification: Automated State Folding (v0.1)

## 1. Objective
To automatically extract high-density intelligence from a session transcript and integrate it into the tiered memory hierarchy without manual intervention, ensuring zero loss of "negative knowledge" (failures) and zero accumulation of "semantic noise" (triviality).

## 2. The Folding Taxonomy (Signal Detection)
The system will scan the session for specific **Information Classes**. If a piece of data fits a class, it is flagged for folding.

| Information Class | Definition | Target Destination |
| :--- | :--- | :--- |
| **User Constraint** | A preference, habit, or hard limit specified by the user. | `USER.md` |
| **Architectural Pivot** | A fundamental change in *how* the system works or is structured. | `Brain.md` $\rightarrow$ Architecture Section |
| **Environment Fact** | A discovered technical truth about the host (OS, paths, tool quirks). | `Brain.md` $\rightarrow$ Environment Section |
| **Negative Knowledge** | A failed attempt, a dead-end, or a bug that was resolved. | `Ledger.md` (The "Anti-Pattern" log) |
| **Pointer/State** | The exact location where the task stopped and the next immediate goal. | `Snapshot.md` |

## 3. The Folding Algorithm (The Pipeline)

**Step 1: Trigger**
- **Event:** Session termination or receipt of a `<<<FOLD>>>` signal.

**Step 2: Extraction (The Sieve)**
- The agent performs a "Reverse-Chronological Scan" of the current session.
- It identifies clusters of dialogue that resulted in a **State Change** (e.g., a file was written, a bug was fixed, a preference was stated).
- It discards "Conversational Glue" (e.g., "Okay," "I understand," "Let me try that").

**Step 3: Conflict Resolution (The Merge)**
- **Check for Redundancy:** Does this information already exist in the Brain?
- **Check for Contradiction:** Does this new info invalidate a previous Brain entry? 
    - *If yes:* Mark the old entry as "Deprecated" and record the reason in the Ledger.
    - *If no:* Append or update the entry.

**Step 4: Verification (The Hash)**
- The agent generates a 1-sentence summary of the "Fold."
- It compares the summary against the raw logs to ensure no critical "Negative Knowledge" was erased during distillation.

---

## 4. Example "Dry Run"

**Raw Input (Session Log):**
> "I tried using `sed` to fix the path but it messed up the indentation. I realized that the `patch` tool is much safer for this. Also, Micah mentioned he hates it when I use LaTeX for arrows."

**Folding Logic Execution:**
1. **Detection:** 
   - "Hates LaTeX arrows" $\rightarrow$ **User Constraint**.
   - "sed messed up indentation / patch is safer" $\rightarrow$ **Negative Knowledge**.
2. **Mapping:**
   - `USER.md` $\rightarrow$ Add: "User prefers plain text arrows over LaTeX."
   - `Ledger.md` $\rightarrow$ Add: "Avoid `sed` for multi-line path edits due to indentation risk; use `patch` tool instead."
3. **Result:** The Brain is updated; the session is killed. The next agent starts with a "Fresh Eye" but knows exactly why `sed` is forbidden.
