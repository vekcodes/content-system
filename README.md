# LinkedIn Funnel: Bivek Raj Shakya

My working copy of the LinkedIn Funnel template. It turns what I know about automated cold email into LinkedIn content, finds the people engaging with it and starts sales conversations.

## Who this is for

SaaS founders and B2B founders who need outbound cold email.

## What I offer

Automated cold email that books more meetings and helps close more deals. No outcome numbers are on file yet, so none are claimed.

## Funnel

1. **Content:** posts that earn attention from SaaS and B2B founders.
2. **Signals:** people engaging with my posts are collected and qualified against my ICP.
3. **Conversations:** a resource and a call are the two next steps. The specific resource, keyword and call link are not defined yet.

## Status

| Area | State |
|---|---|
| Audience, positioning, funnel | Draft from one short setup answer (2026-10-15) |
| Voice, backstory, stories, proof | Not supplied yet |
| Writing samples | None yet |
| Notion board | Not set up |
| OXYGEN Profile Watcher | Not set up |
| EmailBison (campaign data) | Read-only helper in `scripts/emailbison.py`, needs `.env` (see [EmailBison](#emailbison)) |

## Working here

Open this folder in Claude Code and read `CLAUDE.md` first, then the skill for the task.

```text
context/    My positioning, audience, voice, stories and proof (source of truth)
skills/     Content, branding, media and OXYGEN instructions
guides/     Notion, Profile Watcher, qualification, DM and content waterfall setup
templates/  ICP rubric, qualification prompt and output schema
scripts/    Helpers, including the read-only EmailBison client
```

### Next steps

- Add 5–10 writing samples and run `voice-calibration`.
- Capture real founder language for the ideal follower: problems, objections, wording.
- Add proof: client results, stories, numbers I can stand behind.
- Define the resource, comment keyword and call link.
- Draft the first post with `linkedin-copywriter`.

## EmailBison

EmailBison is the cold email campaign system behind my offer. LinkedIn brings in attention and warm signals; EmailBison is where the outbound cold email side runs and where I can pull campaign results to use as proof in content.

`scripts/emailbison.py` is a read-only GET client. It never sends, edits or deletes anything.

```bash
cp .env.example .env   # fill in EMAILBISON_API_KEY and EMAILBISON_URL
python3 scripts/emailbison.py /api/campaigns             # prints the first 4,000 characters
python3 scripts/emailbison.py /api/campaigns out.json    # saves the full response
```

- `EMAILBISON_URL` is my EmailBison instance's base URL; `EMAILBISON_API_KEY` is sent as a Bearer token.
- `.env` is gitignored. Never commit the key, and keep raw campaign exports with real prospect data out of public commits.
- Only report numbers pulled from real campaign data. Until I do, no outcome claims go in posts (see `context/identity/positioning.md`).

### Setup

1. Copy `.env.example` to `.env` and fill it in.
2. Run the command above to confirm the connection.
3. Save any exports you use as evidence under `context/raw/sources/` (private copy only), then capture them with `capture-context`.

## Origin

Built from the [LinkedIn Funnel template](https://github.com/timscheuerai/linkedin-funnel) by Tim Scheuer. See [sources and scope](guides/sources.md) and the [license](LICENSE).
# content-system
# content-system
