# GATE 7: POINTER UPDATE (THE BOOKMARK)

**Action:** 
1. **Identify:** Retrieve the absolute path of the snapshot file created in **Gate 6**.
2. **Overwrite:** Write that path as the sole content of the pointer file: `./agents/[persona]/latest-snapshot.md`.

**Verification:** 
Read `./agents/[persona]/latest-snapshot.md` and confirm: *"Pointer updated. Recovery path is locked."*

**Final Exit:**
Once this pointer is verified, the session is officially archived. You may now notify the user and close the session.
