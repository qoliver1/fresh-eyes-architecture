## GATE 4: PAYLOAD GENERATION (THE RAW SIGNAL)
**Target Persona:** Active Agent
**Objective:** Create a high-fidelity, unbiased "Raw Session Payload" (FULL) for the Distiller.

**Action:**
1. **Follow Specification:** Adhere strictly to `state-payload-specification.md` for **FULL** payloads.
2. **Capture the Mess:** Do NOT curate. Include exact error logs, failed command attempts, and raw user quotes.
3. **Write to Inbox:** Save the payload to `/[persona]/inbox/[YYYY-MM-DD-HHMMSS]-[TYPE]-payload.md`. Ensure the `inbox/` directory exists (e.g., using `mkdir -p`).
4. **Terminate:** Your role is **Reporter**, not **Editor**. Do not attempt to update any Brain or Profile files.

**Verification:**
- Provide the absolute path to the created payload file in the session summary.
