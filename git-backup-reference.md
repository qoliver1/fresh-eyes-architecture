# Git & Backup Reference

Last updated: July 22, 2026

---

## REPOS OVERVIEW

### 1. Fresh Eyes Framework (home dir)
- Location: ~/
- Remote: github.com/qoliver1/fresh-eyes-architecture.git
- Branches:
  - feature/android-tts (current, active work)
  - experimental/voice-integration
  - master (older baseline)
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

### Branch: my-changes
- Created for your local experiments
- Branches off from the same commit as main (0144743b2)
- The backup script auto-switches to this branch when committing source changes
- To see what you've changed vs baseline:
  ```
  cd ~/hermes-agent
  git diff fresh-install-baseline..my-changes
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
1. Commits changes in ~/ (fresh-eyes framework docs) and pushes to qoliver1/fresh-eyes-architecture.git
2. Switches to my-changes branch in ~/hermes-agent/, commits source changes (stays local since upstream is read-only)
3. Skips venv/, node_modules/, __pycache__, *.pyc

### .gitignore (home dir)
Excludes: .hermes/, .cache/, .cargo/, .config/, .local/, .npm/, .ssh/, .termux/, storage/, *.log, hermes-agent/, and an empty file called "No"

---

## CLEANUP HISTORY (Jul 22, 2026)

- Deleted ~/.hermes/hermes-agent/ (old dead copy from Jul 11 first install)
  - Was 240 MB, unused, different commit (4281151 from Jul 11)
  - Active copy is ~/hermes-agent/ (confirmed via shebang + running process)
- Set git global identity: Scribe Agent <scribe@hermes.local>
- Fixed .gitignore to exclude hermes-agent/ (was showing as untracked)
- Cleaned up old deleted temp files (cellar.md, helloworld.txt, personal-vault.md, temp.md, test.md, tts_test_input.txt)

---

## GIT IDENTITY

- Name: Scribe Agent
- Email: scribe@hermes.local
- GitHub account: qoliver1
- Credentials: via gh CLI auth (gh auth git-credential)

---

## QUICK REFERENCE

| Task                         | Command                                              |
|------------------------------|------------------------------------------------------|
| Checkpoint both repos        | `backup-checkpoint`                                  |
| Checkpoint (no push)         | `backup-checkpoint --local`                           |
| Check status of both         | `backup-checkpoint --status`                          |
| Revert source to baseline    | `cd ~/hermes-agent && git reset --hard fresh-install-baseline` |
| Pull upstream source updates | `cd ~/hermes-agent && git checkout main && git pull` |
| See source changes vs baseline| `cd ~/hermes-agent && git diff fresh-install-baseline..my-changes` |
| See all tags                 | `cd ~/hermes-agent && git tag -l`                    |
| See all branches             | `cd ~/hermes-agent && git branch -vv`                |
| See framework branches       | `cd ~ && git branch -vv`                             |

---

## NOTES

- The hermes-agent source remote is NousResearch (upstream). You cannot push to it. If you want to push source experiments online, you'd need to create your own fork on GitHub and add it as a second remote.
- The 438 commits behind is normal — the upstream repo is very active (100+ commits/day around Jul 20-21).
- The package-lock.json that showed as modified was just npm auto-fixing platform-specific peer deps on Android. Harmless.
- ~/hermes-agent/ is 961 MB but most of that is venv/ and node_modules/. The actual source is much smaller.
