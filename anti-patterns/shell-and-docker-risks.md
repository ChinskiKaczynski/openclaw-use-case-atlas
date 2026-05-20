# Anti-Pattern: Shell and Docker Risks

## What it looks like
Giving OpenClaw unrestricted shell access or Docker socket access.

## Why It Matters

### Shell access = full machine control
With shell access, the agent can:
- Read any file (including secrets, credentials, databases)
- Delete anything
- Install software
- Modify system configuration
- Access network resources
- Create backdoors

### Docker socket = container escape
With `/var/run/docker.sock` access, the agent can:
- Start/stop/restart any container
- Create new containers with host access
- Mount host filesystem into containers
- Escape the container entirely
- Access other containers' data

## Examples

### ❌ Mounting docker.sock
```yaml
# docker-compose.yml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
```
**Risk:** Agent can control all containers. This is root-level access to the host.

### ❌ Running as root
```yaml
# docker-compose.yml
user: root
```
**Risk:** Any shell command runs as root. No privilege separation.

### ❌ Unrestricted exec
```
"You can run any command you need"
```
**Risk:** One mistake or prompt injection = full system compromise.

### ❌ Storing secrets in workspace files
```
# MEMORY.md
API_KEY=sk-1234567890abcdef
```
**Risk:** Agent sends this to LLM context. LLM logs may store it. Workspace may be backed up unencrypted.

## The Fix

### Shell Access Rules
1. **Use a dedicated low-privilege user** for the agent
2. **Create wrapper scripts** for allowed commands
3. **Maintain a command allowlist** — agent can only run approved commands
4. **Log all commands** — audit trail
5. **Never allow:** `rm -rf`, `chmod 777`, `curl | bash`, `wget | sh`

### Docker Access Rules
1. **Never mount docker.sock** into OpenClaw container
2. **Use SSH** to a dedicated monitoring user on the host
3. **Use wrapper scripts** on the host for allowed Docker commands
4. **Read-only Docker access** via `docker ps`, `docker logs`, `docker stats` only
5. **Separate user** for Docker commands with limited permissions

### Secret Management Rules
1. **Use OpenClaw secrets** for API keys and credentials
2. **Never store secrets** in workspace files (MEMORY.md, TOOLS.md, etc.)
3. **Never print secrets** in chat
4. **Use environment variables** injected at runtime, not stored in files
5. **Rotate credentials** if they may have been exposed

## Rule of Thumb
> Shell access is root access. Docker socket is root access. Treat both as the highest-risk permissions you can grant.
