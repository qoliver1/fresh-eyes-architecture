import os
import shutil
from datetime import datetime
import subprocess

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing {cmd}: {e.stderr}")
        return None

def dehydrate(persona):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    root = os.path.expanduser("~")
    
    # 1. Paths
    persona_dir = os.path.join(root, f"agents/{persona}")
    session_dir = os.path.join(persona_dir, f"{persona}-sessions", timestamp)
    inbox_dir = os.path.join(persona_dir, "inbox")
    
    temp_summary = os.path.join(root, "temp_summary.md")
    temp_payload = os.path.join(root, "temp_payload.md")
    
    # 2. Verification
    if not os.path.exists(temp_summary) or not os.path.exists(temp_payload):
        print("Error: temp_summary.md and temp_payload.md must exist before running dehydrate.")
        return

    # 3. Mechanical Execution
    os.makedirs(session_dir, exist_ok=True)
    os.makedirs(inbox_dir, exist_ok=True)
    
    summary_dest = os.path.join(session_dir, f"summary_{timestamp}.md")
    payload_dest = os.path.join(inbox_dir, f"{timestamp}-full-payload.md")
    
    shutil.move(temp_summary, summary_dest)
    shutil.move(temp_payload, payload_dest)
    
    # 4. Update Pointer
    pointer_path = os.path.join(persona_dir, f"{persona}-pointer.md")
    with open(pointer_path, "w") as f:
        f.write(f"# Latest Session Pointer\n\nLatest Snapshot: {timestamp}\nPath: {session_dir}")
    
    # 5. Git Durability
    run_command(f"git add {persona_dir}")
    run_command(f'git commit -m "Save session: {persona} [{timestamp}]"')
    
    print(f"Successfully dehydrated session {timestamp} for {persona}.")
    print(f"Summary: {summary_dest}")
    print(f"Payload: {payload_dest}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 dehydrate.py [persona]")
    else:
        dehydrate(sys.argv[1])
