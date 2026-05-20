# Anti-Pattern: Skill Supply Chain Risks

## What it looks like
Installing random skills from ClawHub (or other sources) without reviewing what they do.

## Why It Matters
Skills can:
- Execute arbitrary shell commands
- Read/write any file in your workspace
- Call external APIs with your credentials
- Exfiltrate data
- Modify OpenClaw configuration

A malicious or poorly written skill is equivalent to installing untrusted software on your machine.

## Examples

### ❌ Installing without review
```
"Install the trending skill from ClawHub"
```
**Risk:** You don't know what it does. It could be fine. It could be malicious.

### ❌ Ignoring skill permissions
```
"This skill needs shell access? Sure, grant it."
```
**Risk:** A skill with shell access can do anything OpenClaw can do.

### ❌ Treating skills as trusted
```
"It's on ClawHub, so it must be safe"
```
**Risk:** ClawHub is a marketplace, not a security audit. Anyone can publish.

## The Fix

### Before installing any skill:
1. **Read the source code** — every line
2. **Check what tools it needs** — shell? filesystem? network?
3. **Check what APIs it calls** — are they expected?
4. **Check the author** — known? verified?
5. **Check reviews** — any red flags?
6. **Install in isolation first** — test in a sandbox workspace

### Skill Permission Rules
| Skill needs | Default action |
|-------------|----------------|
| Read files | OK with workspace scope |
| Write files | Review carefully, scope to specific paths |
| Shell/exec | High scrutiny, command allowlist |
| Network calls | Verify endpoints, no external APIs without review |
| Credentials | Never — use OpenClaw secrets instead |

## Red Flags
- Skill requests broad permissions ("full access")
- Skill code is obfuscated or minified
- Skill calls unexpected external URLs
- Skill modifies AGENTS.md, SOUL.md, or config files
- Skill author has no other repos or history
- Skill was published recently with many downloads (astroturfing)

## Rule of Thumb
> A skill is code. Treat it like code you'd run on your production machine. Because it is.
