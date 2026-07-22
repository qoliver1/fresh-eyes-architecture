# Git & Backup Reference

Last updated: July 22, 2026

---

## REPOS OVERVIEW

### 1. Fresh Eyes Framework (home dir)
- Location: ~/
- Remote: github.com/qoliver1/fresh-eyes-architecture.git
- Branch: main (ONLY branch, simple)
- Contains: markdown docs, backlog, journal, framework specs, scripts/
- This is YOUR work, pushed to YOUR GitHub repo

### 2. Hermes Agent Source Code
- Location: ~/hermes-agent/
- Remote: github.com/NousResearch/hermes-agent.git (upstream, READ-ONLY)
- Version: 0.18.2
- Clone date: Jul 20, 2026
- Behind upstream by 438 commits (as of Jul 22)
- This is upstream code you experiment with locally

---

## HERMES-AGENT SOURCE: TAGS & BRANCHES

### Tag: fresh-install-baseline
- Marks the exact clean state from your Jul 20 reinstall
- Use this to revert if you break something
- Revert command:
  ```
  cd ~/hermes-agent
  git reset --hard fresh-install-baseline
  ```

### Branch: main
- Tracks upstream (NousResearch)
- Use for pulling fresh updates:
  ```
  cd ~/hermes-agent
  git checkout main
  git pull origin main
  ```

### Branch: feature/android-tts (ACTIVE)
- This is where you hack on TTS / Termux API integration
- Currently checked out and ready for work
- Changes here stay local (upstream is read-only)
- To see what you've changed vs baseline:
  ```
  cd ~/hermes-agent
  git diff fresh-install-baseline..feature/android-tts
  ```

---

## BACKUP SCRIPT

### Location
- Script: ~/scripts/backup-checkpoint.sh
- Symlink: /usr/bin/backup-checkpoint (run from anywhere)

### Commands
```
backup-checkpoint                          # commit + push both repos
backup-checkpoint "custom message"         # commit + push with your message
backup-checkpoint --local                  # commit only, don't push
backup-checkpoint --status                 # show status of both repos (no commit)
backup-checkpoint --help                   # show usage
```

### What it does
1. Commits changes in ~/ (fresh-eyes framework docs) on main branch, pushes to GitHub
2. Switches to feature/android-tts in ~/hermes-agent/, commits source changes (local only)
3. Skips venv/, node_modules/, __pycache__, *.pyc

### .gitignore (home dir)
Excludes: .hermes/, .cache/, .cargo/, .config/, .local/, .npm/, .ssh/, .termux/, storage/, *.log, hermes-agent/, and an empty file called "No"

---

## THE TTS WORKFLOW

When you want to hack on TTS (sending Hermes messages to Android Termux TTS API):

1. Make sure you're on the right branch:
   ```
   cd ~/hermes-agent
   git checkout feature/android-tts
   ```

2. Edit the source code (the message loop, API calls, etc.)

3. Test it. If it works, checkpoint:
   ```
   backup-checkpoint --local "TTS experiment - what I changed"
   ```

4. If you break it and want to start over:
   ```
   cd ~/hermes-agent
   git reset --hard fresh-install-baseline
   ```

5. If you want to pull fresh upstream code (get latest from NousResearch):
   ```
   cd ~/hermes-agent
   git checkout main
   git pull origin main
   git checkout feature/android-tts   # switch back to your work branch
   git rebase main                    # optional: replay your changes on top
   ```

---

## CLEANUP HISTORY (Jul 22, 2026)

- Deleted ~/.hermes/hermes-agent/ (old dead copy from Jul 11 first install, 240 MB freed)
- Confirmed active copy is ~/hermes-agent/ (via shebang + running process PID)
- Set git global identity: Scribe Agent <scribe@hermes.local>
- Fixed .gitignore to exclude hermes-agent/ from framework repo
- Consolidated framework repo to single "main" branch (deleted master, feature/android-tts, experimental/voice-integration)
- Changed GitHub default branch to main
- Created feature/android-tts branch in hermes-agent source for TTS hacking
- Removed my-changes branch (replaced by feature/android-tts)

---

## GIT IDENTITY

- Name: Scribe Agent
- Email: scribe@hermes.local
- GitHub account: qoliver1
- Credentials: via gh CLI auth (gh auth git-credential)

---

## QUICK REFERENCE

| Task                          | Command                                              |
|-------------------------------|------------------------------------------------------|
| Checkpoint both repos          | `backup-checkpoint`                                  |
| Checkpoint (no push)          | `backup-checkpoint --local`                          |
| Check status of both          | `backup-checkpoint --status`                         |
| Revert source to baseline     | `cd ~/hermes-agent && git reset --hard fresh-install-baseline` |
| Pull upstream source updates  | `cd ~/hermes-agent && git checkout main && git pull` |
| Switch to TTS hacking branch  | `cd ~/hermes-agent && git checkout feature/android-tts` |
| See source changes vs baseline| `cd ~/hermes-agent && git diff fresh-install-baseline..feature/android-tts` |
| See all tags                  | `cd ~/hermes-agent && git tag -l`                    |
| See all branches              | `cd ~/hermes-agent && git branch -vv`                |
| See framework branches        | `cd ~ && git branch -vv`                             |

---

## NOTES

- Framework repo: ONE branch (main). Keep it simple. Docs only.
- Source repo: TWO branches (main = upstream, feature/android-tts = your TTS work).
- The hermes-agent source remote is NousResearch (upstream). You cannot push to it.
- If you want to push source experiments online, create your own fork on GitHub and add it as a second remote.
- The 438 commits behind is normal — the upstream repo is very active (100+ commits/day).
- ~/hermes-agent/ is 961 MB but most of that is venv/ and node_modules/.
