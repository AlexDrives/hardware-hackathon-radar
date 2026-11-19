# AGENTS.md — Continuation Protocol for AI Research Agents

This repository is an open, structured knowledge base tracking **hardware, robotics, and embodied HMI hackathons** (domestic and international), along with product/engineering design notes.

If you are an AI agent asked to expand, verify, or update this repository, follow the rules below.

## 1. Core Grounding Rules
1. **Always check the current date before judging deadlines.** Never assume a hackathon is "open" or "upcoming" from training memory.
2. **Verify every URL and date directly** against official pages, GitHub repositories, or official announcements. If a page cannot be fetched (e.g., HTTP 403 / SPA without SSR / DNS failure), explicitly mark the field as `unverified` or record the last confirmed state—do not guess.
3. **Never fabricate hardware quotas, GPU VRAM allocations, or scoring rubrics** when organizers have not published them publicly. Clearly separate official facts from engineering assumptions.

## 2. Repository Structure
- `README.md`: Human-facing overview, currently-open radar table, categorized hackathon index, and quick links.
- `data/hackathons.json`: Canonical machine-readable dataset. Update this file first whenever adding or refreshing events, then sync `README.md`.
- `docs/d-robotics-2026.md`: Deep dive on the 2026 D-Robotics Hackathon (hardware limits, judge profile, edge-cloud split).
- `docs/makemit-and-benchmarks.md`: Benchmark analysis of MakeMIT, Build18, MIT Reality Hack, and similar prestigious hardware hackathons.
- `docs/project-proposals.md`: Product-oriented embodied HMI proposals derived from hardware constraints and narrative design.

## 3. `data/hackathons.json` Schema
Each entry in `events` must preserve the following fields:
- `id`: kebab-case unique identifier (e.g. `d-robotics-2026`)
- `name`: Official event name
- `region`: `China` | `North America` | `Europe` | `Global`
- `format`: `in-person` | `online` | `hybrid`
- `category`: array of tags (e.g. `["robotics", "hardware", "embodied-ai", "hmi"]`)
- `url`: Primary official URL
- `event_dates`: ISO range or verified description (e.g. `2026-12-05 to 2026-12-07` or `TBD 2027`)
- `registration_window`: Verified registration open/close dates or status string
- `registration_status`: `open` | `opening_soon` | `closed` | `interest_only` | `ended` | `unverified`
- `eligibility`: Who can join (open to all, students only, specific university required, etc.)
- `hardware_or_stack`: Provided hardware, dev kits, or required platforms
- `prize_pool`: Verified prize info or `unspecified`
- `last_verified`: `YYYY-MM-DD`
- `notes`: Concise factual caveats (e.g., signup button behavior, travel coverage, anti-bot fetch notes)

## 4. Known Scraping / Access Quirks
- `devpost.com`, `makemit.org`, `hack.osu.edu`, and `seeedstudio.com/blog` frequently return HTTP `403` to automated `curl`/fetch clients. Use GitHub repository metadata, official mirrors, or browser inspection when researching those events.
- `hackjunction.com`, `hackmit.org`, and `gallery.adventure-x.cn` are client-rendered SPAs; plain HTML fetches only return shell markup.
- For Chinese domestic events (e.g., `hackathon.d-robotics.cc`), official signup links are sometimes published via WeChat Official Accounts or partner communities even when the landing page button shows loading/placeholder text.

## 5. Research Backlog (Good Next Tasks for Agents)
- [ ] Verify the actual registration form URL / WeChat QR entry for `d-robotics-2026` before `2026-11-30`.
- [ ] Pull specific winning hardware project case studies from `Build18 Garage` (`https://www.build18.org/garage`) and `MIT Reality Hack` Devpost/GitHub archives.
- [ ] Track European & Asian university hardware makeathons (ETH Zurich, UnternehmerTUM Makeathon, SUTD/NUS, Tsinghua/SJTU/HKUST XbotPark camps).
- [ ] Add a `projects/` or `case-studies/` index linking open-source hardware hackathon repos with BOMs and FSM architectures.
