## GATE 7: PROFILE FOLDING (GLOBAL MEMORY INTEGRATION)
**Target Persona:** Distiller
**Objective:** Integrate new user constraints and preferences from the Raw Payload into the global truth.

**Action:**
1. **Ingest:** Read the `[persona]-latest-payload.md` file.
2. **Extract:** Isolate the "User Constraints" section from the payload.
3. **Compare:** Compare these new constraints against the current `user-profile.md`.
4. **Surgical Update:** Use `patch` or `write_file` to append/update the global `user-profile.md`.
5. **Verification:** Read back the modified section of `user-profile.md` to ensure the change is physically committed.

**Constraint:**
- Use only the information provided in the Payload. 
- Do not use conversational context from the session.
