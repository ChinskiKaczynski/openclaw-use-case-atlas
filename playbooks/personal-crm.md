# Personal CRM Playbook

## Purpose
Set up an agent-managed contact index that tracks your professional relationships and makes them queryable in natural language.

## Prerequisites
- OpenClaw with email skill configured (Gmail or Outlook)
- Calendar skill configured (Google Calendar, iCloud, or CalDAV)
- Memory tools or file-based storage enabled
- Telegram or similar chat channel for queries

## Setup

### Step 1: Configure Data Sources
```
Skills needed:
- Email skill (read-only OAuth)
- Calendar skill (read-only)
- Memory Tools or file-based memory
```

### Step 2: Create Contact Index Structure
Store in `memory/contacts/`:
```
memory/contacts/
  _index.md          # Master index with last-updated timestamp
  sarah-chen.md      # Individual contact file
  john-doe.md        # Individual contact file
```

Each contact file format:
```markdown
# Sarah Chen

## Company
Acme Corp

## Role
Engineering Manager

## Last Contact
2026-05-15

## Topics
- API integration project
- Partnership discussion
- Hiring pipeline

## Interaction History
- 2026-05-15: Email about API integration timeline
- 2026-05-01: Calendar meeting: Q2 planning
- 2026-04-20: Email: introduced to team

## Relationship Strength
Warm (regular contact)
```

### Step 3: Set Up Daily Indexing Cron
```
Schedule: Daily at 2:00 AM
Prompt: "Scan yesterday's emails and calendar events. Update memory/contacts/ index with any new interactions. Create new contact files for first-time contacts. Update last-contact dates and topics for existing contacts."
```

### Step 4: Set Up Pre-Meeting Context Cron
```
Schedule: 30 minutes before each calendar event (or hourly batch)
Prompt: "Check upcoming calendar events in next 1 hour. For each attendee, pull context from memory/contacts/ and send me a brief: last contact date, topics discussed, and any open action items."
```

### Step 5: Query Interface
Users can now ask:
- "When did I last talk to Sarah?"
- "Who do I know at Acme Corp?"
- "What was my last discussion with John about?"
- "Show me all contacts I haven't talked to in 30+ days"

## Maintenance

### Weekly
- Review auto-created contact files for accuracy
- Remove or merge duplicate entries
- Update relationship strength labels

### Monthly
- Export contact index for backup
- Review stale contacts (90+ days no contact)
- Clean up interaction history older than 1 year

## Safety Notes
- Email access must be read-only
- Contact data stays local — no cloud sync without encryption
- No automated outbound messages without user approval
- Health/financial contacts should be tagged with extra privacy flags

## Related Use Cases
- OC-020: Personal CRM
- OC-001-email: Email Triage Agent
- OC-004: Daily Ops Briefing
- OC-011: Memory Vault
