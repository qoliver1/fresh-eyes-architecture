import os
import sys
import glob

def get_file_content(path, label):
    try:
        with open(path, 'r') as f:
            return f"## {label}\n{f.read()}\n\n"
    except FileNotFoundError:
        return f"## {label}\n[FILE NOT FOUND: {path}]\n\n"

def main():
    if len(sys.argv) < 2:
        print("Error: Persona name required.")
        sys.exit(1)

    persona_name = sys.argv[1]
    root = os.path.expanduser('~')
    
    # Define the core hydration hierarchy
    hierarchy = [
        ('persona', f'agents/{persona_name}/{persona_name}.md'),
        ('user-profile', 'user-profile.md'),
        ('brain', f'agents/{persona_name}/{persona_name}-brain.md'),
        ('summary', f'agents/{persona_name}/{persona_name}-summary.md'),
    ]
    
    final_payload = f"# Hydration Payload: {persona_name}\n\n"
    
    # Aggregate Core Hierarchy
    for label, path in hierarchy:
        full_path = os.path.join(root, path)
        final_payload += get_file_content(full_path, label)

    # Resolve and Aggregate Snapshot
    snapshot_pointer = os.path.join(root, f'agents/{persona_name}/latest-snapshot.md')
    try:
        with open(snapshot_pointer, 'r') as f:
            snapshot_path = f.read().strip()
            if not snapshot_path.startswith('/'):
                snapshot_path = os.path.join(root, snapshot_path)
            final_payload += get_file_content(snapshot_path, "Latest Snapshot")
    except (FileNotFoundError, IOError):
        final_payload += f"## Latest Snapshot\n[FILE NOT FOUND: {snapshot_pointer}]\n\n"

    # Handle Hot Start (Chronological Clone Stream)
    if len(sys.argv) > 2 and sys.argv[2] == 'hot':
        clones_dir = os.path.join(root, f'agents/{persona_name}/clones')
        if os.path.exists(clones_dir):
            clone_files = sorted(glob.glob(os.path.join(clones_dir, '*_clone.md')))
            if clone_files:
                latest_clone = clone_files[-1]
                final_payload += get_file_content(latest_clone, "Cognitive Clone (Latest)")
            else:
                final_payload += f"## Cognitive Clone\n[NO CLONE FILES FOUND IN {clones_dir}]\n\n"
        else:
            final_payload += f"## Cognitive Clone\n[CLONES DIRECTORY NOT FOUND: {clones_dir}]\n\n"

    # Write the payload
    payload_path = os.path.join(root, f'hydration_payload_{persona_name}.md')
    with open(payload_path, 'w') as f:
        f.write(final_payload)
    
    print(f"Payload created: {payload_path}")

if __name__ == "__main__":
    main()
