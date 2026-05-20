# Track: Homelab Operator

## Profile
You run a home server (Synology, Proxmox, etc.) with Docker containers for media, automation, and services. You want visibility and control without risking your infrastructure.

## Best First Use Cases

### 1. NAS Read-Only Monitor [L0]
**Why:** See everything, break nothing. The safest starting point.
**Time to value:** 4 hours
**Playbook:** [Synology Read-Only Monitor](../playbooks/synology-readonly-monitor.md)

### 2. Daily Ops Briefing [L0]
**Why:** Combine NAS health with calendar and other sources.
**Time to value:** 2 hours
**Playbook:** [Daily Ops Briefing](../playbooks/daily-ops-briefing.md)

### 3. Smart Home Control [L0/L1]
**Why:** Control devices by chat. Start with reads, add control gradually.
**Time to value:** 2 hours
**Use case:** [Smart Home Control](../use-cases/devops-homelab/oc-017-smart-home-control.md)

### 4. Docker Log Digest [L0]
**Why:** Stop grepping logs manually. Agent summarizes for you.
**Time to value:** 1 hour

### 5. Backup Audit [L0]
**Why:** Know your backups actually work. Read-only verification.
**Time to value:** 2 hours

## Avoid at the Beginning
- Docker socket access [L4]
- Auto-restart containers [L2 — later]
- Auto-delete/cleanup [L3]
- Root SSH [L4]
- Modifying production configs [L3]

## Recommended Progression
```
Week 1: NAS read-only monitor
Week 2: Daily briefing + log digest
Week 3: Smart home read-only
Week 4: Backup audit
Month 2+: Add approval-based container restart
```

## Key Safety Rules
- **Never mount docker.sock**
- Dedicated read-only monitoring user
- Wrapper scripts for any commands
- No root access
- SSH key-based auth only
- Command allowlist enforced
