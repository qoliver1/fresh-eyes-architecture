# Additional Instructions

## Agent Switching Protocol
When the user instructs a switch to a specific agent (e.g., "Switch to [Agent Name]", "Swap to [Agent Name]", or "Load [Agent Name]"):

1. **Locate:** Navigate to the `./agents/` directory, find the subfolder matching the agent's name, and enter it (e.g., `./agents/hyper-overlord/`).
2. **Load:** Locate and read the core identity file, typically `agent.md`.
3. **Adopt:** Immediately assume the persona, constraints, and behavioral instructions defined in that file.
4. **Verify:** Briefly acknowledge the switch by stating the new active identity and confirming that the instructions have been loaded.
5. **Continuity:** Maintain the current session state while applying the new persona's logic to the existing context.

## Reasoning Buffer Mandate
When any task requires 3 or more tool calls, or any archival/save sequence:
1. **Initialize:** Immediately create `temp_[persona].md` and log the plan.
2. **Surgical Execution:** Use the "swap-back-and-forth" pattern: Write thought $\rightarrow$ Tool Call $\rightarrow$ Read Result $\rightarrow$ Write synthesis to `temp` $\rightarrow$ Repeat.
3. **Zero-Truncation:** Never produce a final response until the buffer is complete.
4. **Cleanup:** Delete `temp_[persona].md` after the task is delivered.

## Quick Log Protocol
When the user instructs you to "perform a quick log" or "quick log this":

1. **Initiate Sequence:** Navigate to the `~/quick-log-sequence/` folder.
2. **Execute Gates:** Follow the documents in numerical order (01, 02, etc.) until the sequence is complete.
3. **Verification:** Briefly confirm once both the dialogic contribution and the status update have been recorded.
