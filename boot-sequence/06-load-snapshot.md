# Boot Sequence Phase 6: Load Point of Departure (The Snapshot & Clone)

**Step 1: Load Environment State (The Snapshot)**
1. List files in the `./agents/[persona]/[persona]-sessions/` directory.
2. Identify and read the most recent snapshot file (the one with the latest timestamp).

**Step 2: Load Cognitive State (The Clone - If Applicable)**
- **Check Routing Gate:** Did `./boot-sequence/03-hydration-routing.md` set the `hydration_level` to **HOT**?
- **If YES:** Read the `./agents/[persona]/[persona]-clone.md` file.
- **Goal:** Use the Clone as the final "last mile" of continuity. It represents the exact train of thought from the last session and must be the dominant signal in your current context.

**Final Step:** Once this is loaded, you are fully hydrated. You may now respond to the user, ensuring that the constraints in `./user-profile.md` govern your output.