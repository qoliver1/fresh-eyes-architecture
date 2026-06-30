# Additional Instructions

## Agent Switching Protocol
When the user instructs a switch to a specific agent (e.g., "Switch to [Agent Name]", "Swap to [Agent Name]", or "Load [Agent Name]"):

1. **Locate:** Navigate to the directory associated with that agent name (e.g., `~/ [agent-name]/`).
2. **Load:** Locate and read the core identity file, typically `agent.md`.
3. **Adopt:** Immediately assume the persona, constraints, and behavioral instructions defined in that file.
4. **Verify:** Briefly acknowledge the switch by stating the new active identity and confirming that the instructions have been loaded.
5. **Continuity:** Maintain the current session state while applying the new persona's logic to the existing context.

## Quick Log Protocol
When the user instructs you to "perform a quick log" or "quick log this":

1. **Initiate Sequence:** Navigate to the `~/quick-log-sequence/` folder.
2. **Execute Gates:** Follow the documents in numerical order (01, 02, etc.) until the sequence is complete.
3. **Verification:** Briefly confirm once both the dialogic contribution and the status update have been recorded.
