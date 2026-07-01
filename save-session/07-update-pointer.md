# GATE 7: POINTER UPDATE (BLOCK 3: COMMIT)

**Action:** 
1. **Identify:** Retrieve the absolute path of the snapshot file created in **Gate 6**.
2. **Overwrite:** Write that path as the sole content of the pointer file: `./agents/[persona]/latest-snapshot.md`.

**Verification:** Read `./agents/[persona]/latest-snapshot.md` and confirm: *"Pointer updated. Recovery path is locked."*

**Block Completion:** 
1. Write a final synthesis of **Block 3** to `temp_[persona].md`.
2. **Finalize:** Perform the Git commit, delete `temp_[persona].md`, and notify the user.
