#!/data/data/com.termux/files/usr/bin/bash
#
# backup-checkpoint.sh — Checkpoint both repos (fresh-eyes framework + hermes-agent source)
#
# Usage:
#   backup-checkpoint.sh              # commit + push both repos
#   backup-checkpoint.sh "message"    # commit + push with custom message
#   backup-checkpoint.sh --local      # commit only, don't push
#   backup-checkpoint.sh --status     # show status of both repos without committing
#
# What it does:
#   1. Commits any changes in ~/ (fresh-eyes framework docs)
#   2. Commits any changes in ~/hermes-agent/ (Hermes source code — on my-changes branch)
#   3. Pushes both to their remotes (unless --local)
#
# Repos:
#   ~/              -> github.com/qoliver1/fresh-eyes-architecture.git
#   ~/hermes-agent/ -> github.com/NousResearch/hermes-agent.git (upstream, read-only)

set -euo pipefail

HOME_DIR="/data/data/com.termux/files/home"
HERMES_DIR="$HOME_DIR/hermes-agent"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
PUSH=true
STATUS_ONLY=false
CUSTOM_MSG=""

# Parse args
for arg in "$@"; do
  case "$arg" in
    --local)   PUSH=false ;;
    --status)  STATUS_ONLY=true ;;
    -h|--help)
      echo "Usage: backup-checkpoint.sh [message] [--local] [--status]"
      echo ""
      echo "  no args       commit + push both repos"
      echo "  'message'     commit + push with custom message"
      echo "  --local       commit only, don't push"
      echo "  --status      show status of both repos"
      exit 0
      ;;
    *) CUSTOM_MSG="$arg" ;;
  esac
done

# Colors (if terminal supports)
if [ -t 1 ]; then
  GREEN='\033[0;32m'
  YELLOW='\033[1;33m'
  RED='\033[0;31m'
  NC='\033[0m'
else
  GREEN='' YELLOW='' RED='' NC=''
fi

ok()    { echo -e "${GREEN}[OK]${NC}    $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $1"; }
fail()  { echo -e "${RED}[FAIL]${NC}  $1"; }

echo "============================================"
echo "  HERMES BACKUP CHECKPOINT — $TIMESTAMP"
echo "============================================"
echo ""

# ----------------------------------------------------------------------------
# STATUS ONLY MODE
# ----------------------------------------------------------------------------
if [ "$STATUS_ONLY" = true ]; then
  echo "--- FRESH EYES FRAMEWORK (~) ---"
  cd "$HOME_DIR"
  git status -s
  echo ""
  echo "--- HERMES SOURCE (~/hermes-agent, branch: my-changes) ---"
  cd "$HERMES_DIR"
  git checkout my-changes 2>/dev/null || true
  git status -s
  git checkout main 2>/dev/null || true
  echo ""
  exit 0
fi

MSG="${CUSTOM_MSG:-Checkpoint $TIMESTAMP}"

# ----------------------------------------------------------------------------
# REPO 1: FRESH EYES FRAMEWORK (home dir)
# ----------------------------------------------------------------------------
echo "--- FRESH EYES FRAMEWORK (~/) ---"
cd "$HOME_DIR"

# Add and commit
git add -A 2>/dev/null || true
if git diff --cached --quiet 2>/dev/null; then
  echo "  No changes to commit."
else
  git commit -m "$MSG" --no-verify 2>/dev/null
  ok "Committed framework docs"
fi

if [ "$PUSH" = true ]; then
  if git push origin main 2>/dev/null; then
    ok "Pushed to github.com/qoliver1/fresh-eyes-architecture.git"
  else
    warn "Push failed (network? credentials?) — commits are still local"
  fi
fi

echo ""

# ----------------------------------------------------------------------------
# REPO 2: HERMES AGENT SOURCE (~/hermes-agent)
# ----------------------------------------------------------------------------
echo "--- HERMES SOURCE (~/hermes-agent) ---"
cd "$HERMES_DIR"

# Switch to feature/android-tts branch (where personal source edits go)
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "feature/android-tts" ]; then
  git checkout feature/android-tts 2>/dev/null || true
  CURRENT_BRANCH=$(git branch --show-current)
fi
echo "  Branch: $CURRENT_BRANCH"

# Add and commit (only tracked source files, skip venv/node_modules)
git add -A -- . ':!venv' ':!node_modules' ':!__pycache__' ':!*.pyc' 2>/dev/null || true

if git diff --cached --quiet 2>/dev/null; then
  echo "  No source changes to commit."
else
  git commit -m "$MSG" 2>/dev/null
  ok "Committed source changes"
fi

if [ "$PUSH" = true ]; then
  # If you set up your own fork remote later, this would push there
  # For now we do local-only since upstream is read-only NousResearch
  echo "  Source stays local (upstream is NousResearch, read-only)"
fi

echo ""

# ----------------------------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------------------------
echo "============================================"
echo "  CHECKPOINT COMPLETE"
echo "============================================"
echo ""
echo "  To revert src: cd ~/hermes-agent && git reset --hard fresh-install-baseline"
echo ""
