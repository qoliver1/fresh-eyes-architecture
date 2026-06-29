learned_patterns: []
learned_ledger: []
learned_traits: []
current_focus: "Establishing high-precision search heuristics and source hierarchy."
search_heuristics:
  intent_based_querying:
    - "Broad Intent (e.g., [topic] overview)"
    - "Critical Intent (e.g., [topic] criticisms, [topic] vs [alternative])"
    - "Implementation Intent (e.g., [topic] tutorial, [topic] documentation)"
    - "Social Intent (e.g., [topic] reddit, [topic] discussion)"
  seo_filter: "Actively identify and deprioritize content from sites that exist solely for ad revenue/SEO. Favor deep-form content, whitepapers, and first-person accounts."
  temporal_awareness: "For rapidly evolving topics, prioritize results from the last 3-6 months. Explicitly check for 'outdated' signals."
preferred_source_hierarchy:
  tier_1_primary: ["Official Documentation (MDN, Python, AWS, etc.)", "Academic/Scientific Repositories (arXiv, PubMed)", "Official Project Repositories (GitHub, GitLab)"]
  tier_2_expert_community: ["High-signal technical blogs", "Specialized Subreddits", "Stack Overflow (high-reputation)", "X (Verified experts)"]
  tier_3_broad_context: ["Reputable News Outlets", "Wikipedia (as a starting point)"]
tool_usage_guidelines:
  web_search: "Use for landscape mapping and finding Tier 1/Tier 3 sources."
  browser: "Use for deep-reading, extracting nuance, and navigating community threads."
  command_line: "Use curl or grep where possible to extract raw data from structured web resources to minimize token overhead."
negative_knowledge:
  - "Generic 'AI-generated' content farms."
  - "Highly biased political commentary sites (unless tracking bias)."
  - "Circular citation loops."
