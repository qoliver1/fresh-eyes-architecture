# GATE 6: SNAPSHOT COMMIT (BLOCK 3: COMMIT)

**Action:**
1. **Capture State:** Generate the final session snapshot and the cognitive clone.
2. **Archive Clone:** Write the current cognitive state to `agents/[persona]/clones/[timestamp]_clone.md`.
3. **Archive Snapshot:** Save the general session snapshot to the timestamped session folder.
4. **Commit:** Perform a Git commit of the persona directory to lock the state.

**Verification:** Confirm both the snapshot and the timestamped clone were written.

**Next Step:** Proceed to `./save-session/07-update-pointer.md`.
