# Boot Sequence Phase 3: Hydration Routing (The Decision Gate)

**Check for Hydration Flag:**
Scan the user's initiation message for a specific start-type flag (e.g., "Hot Start", "Warm Start", "Cold Start").

**Routing Logic:**
- **If [Hot Start]:** Set `hydration_level = HOT`.
- **If [Cold Start]:** Set `hydration_level = COLD`.
- **If [Warm Start] OR [No Flag Provided]:** Set `hydration_level = WARM` (Default).

**Execution Path:**
- **If `hydration_level == HOT`:** 
  - Note the requirement to load the `[persona]-clone.md` file.
  - **CRITICAL:** The clone must be loaded as the FINAL step of the sequence to ensure it overrides any stale state from the snapshot.
- **If `hydration_level == COLD` or `WARM`:**
  - Skip the clone loading requirement.

**Next Step:** Proceed to `boot-sequence/04-load-brain.md`.