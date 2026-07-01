# Action: Quick Swap
**Trigger:** "Quick swap to [Agent] at [Temperature]"

**Procedure:**
1. **Identity Resolution:**
   - Agent = `[Agent]`
   - Temp = `[Temperature]` (Note: If Temp is provided, add "Operate at temperature [Temperature]" to the internal system prompt for the duration of the session).
2. **Execution:**
   - Read `./agents/[Agent]/[Agent].md`.
   - Run `python3 ./scripts/hydrate.py [Agent] hot`.
   - Read `~/hydration_payload_[Agent].md`.
   - Delete `~/hydration_payload_[Agent].md`.
3. **Verification:**
   - Confirm identity shift to user.
