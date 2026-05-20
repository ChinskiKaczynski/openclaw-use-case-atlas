# Playbook: Synology NAS Read-Only Monitor

## Overview
Monitor your Synology NAS health without giving OpenClaw any write access. This is the safest way to start with infrastructure monitoring.

## Prerequisites
- Synology NAS with DSM 7+
- OpenClaw running on the NAS (Docker) or on a machine with network access
- SSH access to NAS (for initial setup only)

## Setup

### Step 1: Create a read-only monitoring user
On Synology DSM:
1. Control Panel → User & Group → Create user: `openclaw-monitor`
2. Assign to group: `users` (no admin)
3. Permissions: read-only access to:
   - Resource Monitor
   - Log Center
   - Storage Manager
4. **Do NOT grant:** Docker, Package Center, File Station write, Terminal

### Step 2: Create wrapper scripts on the NAS
```bash
#!/bin/bash
# /volume1/scripts/nas-health.sh
# Read-only health check — safe for OpenClaw

echo "=== DISK ==="
df -h /volume1 /volume2 2>/dev/null
echo ""
echo "=== SMART ==="
for disk in /dev/sata1 /dev/sata2 /dev/sata3 /dev/sata4; do
  if [ -e "$disk" ]; then
    smartctl -H "$disk" 2>/dev/null | grep -i "result"
  fi
done
echo ""
echo "=== CPU/MEM ==="
top -bn1 | head -5
echo ""
echo "=== DOCKER ==="
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || echo "Docker not accessible"
echo ""
echo "=== UPTIME ==="
uptime
```

### Step 3: Configure OpenClaw
Add to your agent's TOOLS.md or standing orders:
```
To check NAS health, run:
ssh openclaw-monitor@NAS_IP "bash /volume1/scripts/nas-health.sh"

Do NOT run any other commands on the NAS.
Do NOT use docker.sock.
Do NOT run as root.
```

### Step 4: Test
```
Check my NAS health.
```

### Step 5: Add cron
```
Every day at 8:00 AM, check NAS health and send me a summary.
Flag any: disk >80% full, SMART failure, container down, CPU >90%.
```

## Safety Checklist
- [ ] Dedicated read-only user
- [ ] No docker.sock access
- [ ] No root / no sudo
- [ ] Wrapper scripts only (no free-form commands)
- [ ] SSH key-based auth (no password)
- [ ] Command allowlist in agent config
- [ ] No write permissions on any NAS resource

## What NOT to Do
- Do NOT give OpenClaw your admin credentials
- Do NOT mount docker.sock into OpenClaw container
- Do NOT allow `sudo` or `su` commands
- Do NOT grant write access to shared folders
- Do NOT allow package installation

## Next Steps
After reliable monitoring:
- Add alert routing (notify on anomalies)
- Add draft action suggestions (L1)
- Add approval-based container restart (L2) — only after extensive testing
