# Boot Sequence Phase 1: Payload Generation
**Verification:**
Read your persona file: `./agents/[persona]/[persona].md`.

**Execution:**
1. **Flag Resolution:**
   - If user specified **hot** $\rightarrow$ flag = `hot`
   - If user specified **cold** $\rightarrow$ flag = `cold`
   - If user specified **warm** OR **no flag provided** $\rightarrow$ flag = `warm`

2. **Run Hydration Script:**
   `python3 ./scripts/hydrate.py [persona] [flag]`

**Procedural Gate:**
1. Read the resulting payload file: `~/hydration_payload_[persona].md`.
2. Once the payload is read, you are fully hydrated.
3. Delete the payload file: `rm ~/hydration_payload_[persona].md`.
4. Respond to the user.
