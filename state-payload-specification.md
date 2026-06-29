# Specification: Raw Session Payload (v0.2 - IAL Model)

**Purpose:** To provide the Distiller agent with an unbiased, high-signal data dump of a session, removing the "self-grading bias" from the active agent. This specification supports both deep architectural updates (FULL) and high-frequency progress tracking (DELTA).

## 📄 File Lifecycle & Location

### 1. The Inbox (The Producer's Target)
Agents MUST write their payload to their local `inbox/` directory. The filename MUST follow the timestamped pattern to ensure chronological ordering and prevent overwriting.

- **Path:** `/[persona]/inbox/[YYYY-MM-DD-HHMMSS]-[TYPE]-payload.md`
- **Types:**
  - `FULL`: Used by `save-session/` for deep architectural/state updates.
  - `DELTA`: Used by `quick-save/` for high-frequency progress/delta updates.

### 2. The Archive (The Distiller's Destination)
Once a payload is successfully processed, it MUST be moved by the Distiller to the appropriate archive folder.

| Payload Type | Archive Path Pattern |
| :--- | :--- |
| **FULL** | `/[persona]/archived/full/[YYYY-MM-DD-HHMM]-full-payload.md` |
| **DELTA** | `/[persona]/archived/deltas/[YYYY-MM-DD-HHMM]-delta-payload.md` |

---

## 📐 Required Structure

The payload must be written in the following order. Sections marked `[Optional for DELTA]` are only required for `FULL` payloads.

### 1. Metadata
- **Payload Type:** [FULL | DELTA]
- **Persona:** [Name]
- **Session ID:** [Timestamp/ID]
- **Duration:** [Start -> End] `[Optional for DELTA]`

### 2. The Operational Record (The Delta)
A concise list of every state change that occurred:
- **Files Modified:** [Path] -> [What was changed]
- **Bugs Resolved:** [Issue] -> [Root Cause] -> [Fix]
- **Decisions Made:** [Problem] -> [Chosen Solution] -> [Logic/Why]

### 3. The Evidence (Raw Signal) `[Required for FULL]`
Instead of a summary, provide "Critical Blocks" of the transcript:
- **User Constraints:** Exact quotes where the user specified a preference or limit.
- **Negative Knowledge:** Exact quotes or logs of failed attempts, errors, and dead-ends.
- **Key Breakthroughs:** The specific exchange where the solution was found.

### 4. The Pointer (Handoff)
- **Current State:** Where exactly the work stopped.
- **Immediate Next Step:** The first thing the next agent must do.
- **Pending Queue:** Any unresolved threads or "to-do" items. `[Optional for DELTA]`

---

### 🚦 Data Routing Rules (CRITICAL)
To prevent redundancy and token bloat, agents MUST route information to the correct destination:

| Information Type | Routing Rule | Target File |
| :--- | :--- | :--- |
| **Global Truth** | User identity, communication style, project-wide standards. | `user-profile.md` |
| **Local Truth** | Agent-specific logic, technical decisions, local errors. | `[persona]-brain.md` |
| **Momentum** | High-frequency progress, minor deltas, recent wins. | `[persona]-delta-log.md` |

---

**Instruction for Active Agent:** 
1. **Do NOT** attempt to update `user-profile.md` or `[persona]-brain.md`. 
2. **Write to Inbox:** Save the payload to `/[persona]/inbox/[YYYY-MM-DD-HHMMSS]-[TYPE]-payload.md`.
3. **Terminate:** Your role is **Reporter**, not **Editor**.
