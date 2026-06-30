# Hermes Context Compaction & Handoff Mechanism

## 1. Overview
As conversations grow in length, they eventually hit the LLM's context window limit. To prevent data loss and avoid "context rot," Hermes employs an automatic **Context Compaction** system. Instead of simply deleting old messages, it summarizes the history into a high-density "Handoff Summary" that is injected into new turns.

## 2. How it Works
When a session exceeds a specific token threshold, the system triggers a compaction event:
- **Synthesis:** Recent turns are analyzed and compressed into a structured summary.
- **State Capture:** The summary preserves key goals, active constraints, completed actions, and pending "TBD" items.
- **Injection:** This summary is prepended to the current context window, acting as a "save-state" for the agent.

## 3. The Handoff Logic (The "Truth" Hierarchy)
To prevent the agent from getting confused between the summary and the current conversation, the following priority rules are applied:

1. **The Latest Message Wins:** The most recent user message is the absolute source of truth. If the summary says "Do X" but the latest message says "Stop X and do Y," the agent must immediately pivot to Y.
2. **Summary as Background:** The compaction block is treated as "background reference" or "historical context," NOT as active, immediate instructions.
3. **Persistent Memory Overrides:** Data in `USER_PROFILE` or `MEMORY` always takes precedence over a session summary, as those are durable facts rather than transient session state.

## 4. Benefits of Compaction
- **Window Efficiency:** Drastically reduces token overhead, allowing for much longer total sessions.
- **Signal Preservation:** Captures the *outcome* of a long technical struggle without requiring the agent to re-read every failed attempt.
- **Cognitive Reset:** Helps the agent "forget" the noise of the process while "remembering" the result of the work.

## 5. User Interaction
Users can see when this happens via the `[CONTEXT COMPACTION]` marker. If the compaction has missed a critical detail, the user can simply provide that detail again in the chat, which will then be incorporated into the next compaction cycle.
