# Boot Sequence Phase 6: Load Point of Departure (The Snapshot & Clone)

**Step 1: Load Environment State (The Snapshot)**
Read the latest snapshot pointer: `./agents/[persona]/latest-snapshot.md`.

**Step 2: Load Cognitive State (The Clone - If Applicable)**
- **Check Routing Gate:** Did `./boot-sequence/03-hydration-routing.md` set the `hydration_level` to **HOT**?
- **If YES:** Read the `./agents/[persona]/[persona]-clone.md` file.
- **Goal:** Use the Clone as the final "last mile" of continuity. It represents the exact train of thought from the last session and must be the dominant signal in your current context.

**Procedural Gate:**
1. Write the final state resolution to `temp_[persona].md`.
2. You are now fully hydrated. Delete `temp_[persona].md` and respond to the user.
