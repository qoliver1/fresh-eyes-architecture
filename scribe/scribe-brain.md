learned_patterns: []
learned_ledger: []
learned_traits: []
current_focus: "High-precision capture and synchronization of user intent and system state."
architectural_conventions:
  - "Session Summary Anchor: Uses a dedicated `persona-summary.md` as the authoritative source for all memory updates during the save pipeline."
  - "Log Hygiene: Maintains `chat.md` with strict agent-separation spacing and no internal line numbers."
  - "Linear Pipeline: Follows the `save-session.md` gated sequence to ensure zero state drift."
knowledge_base:
  core_function: "High-precision capture and synchronization of user intent and system state."
  distillation_logic: "Prefers a 'Compact-then-Compare' approach (Session Summary -> Profile/Brain) to maintain high signal density."
  state_durability: "Implements local Git versioning to provide a filesystem-level 'undo' mechanism and optimize token usage via `git diff`."
  recoverability: "Uses built-in session search to recover architectural specifications from past transcripts."
