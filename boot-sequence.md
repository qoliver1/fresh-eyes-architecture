# Boot Sequence: State Hydration Protocol

You MUST execute this sequence in the exact order listed before responding to the user. Your activation is not complete, and you are not "awake," until every step has been performed.

**Step 1: Identify Persona**
Determine your current persona name (e.g., "agent-zero", "hyper-overlord", "big-picture-agent", "scribe").

**Step 2: Load Permanent Foundation (The Brain)**
Read the corresponding brain file: `/[persona]/[persona]-brain.md`.
*Goal: Establish the long-term architectural truths and project knowledge.*

**Step 3: Load Recent Momentum (The Summary)**
Read the corresponding summary file: `/[persona]/[persona]-summary.md`.
*Goal: Capture the high-level trajectory and recent progress.*

**Step 4: Load Point of Departure (The Snapshot)**
1. List files in the `/[persona]/[persona]-sessions/` directory.
2. Identify and read the most recent snapshot file (the one with the latest timestamp).
*Goal: Restore the exact state and pending tasks from the last session.*

**Step 5: Load Overriding Constraints (User Profile)**
Read `user-profile.md`.
*Goal: Ensure that user preferences, technical standards, and communication styles are the most recent and dominant signals in your context window.*

**Final Confirmation:**
Once these four files are loaded, you are fully hydrated. You may now respond to the user, ensuring that the constraints in `user-profile.md` govern your output.