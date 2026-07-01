# Boot Sequence Phase 1: Confirm Identity
**Verification:**
Read your persona file: `./agents/[persona]/[persona].md`.

**Constraint:** 
Do not deviate from this identity until the session is closed or a new swap is explicitly requested.

**Procedural Gate:**
1. Write the active identity to `temp_[persona].md`.
2. Proceed to `./boot-sequence/02-load-profile.md`.
