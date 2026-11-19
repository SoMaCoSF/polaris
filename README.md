<!--
  SOM-DOC-10858-v1.0.0
  Ghost Catalog: SOM-DOC-10858
  Title: POLARIS APPLICANT DOSSIER
  Page file_id: SOM-POL-0001-v0.1.1 · Category: APPLICANT-DOSSIER · Agent: boardy (substance) / witness (build)
  Status: LIVE on founder GO 2026-11-18 21:29 PT · https://polaris.somacosf.com · repo SoMaCoSF/polaris
-->

# POLARIS — Applicant Dossier

Research Engineer, Polaris · Google DeepMind, Mountain View
Job: https://www.google.com/about/careers/applications/jobs/results/114077679900074694-research-engineer-polaris-deepmind

**Premise:** One week per task. Six checks per task. Every claim graded.
The application is not a resume. It is one finished task, its grader, and
agent attestations in the same evidence format — failure modes included.

**Reading path:** 01 Claim → 02 Failure modes to checks → 03 Task + grader →
04 Evidence (4 charts) → 05 Agent attestations → OWED list.

**State, honestly:**
- Substance: Boardy Blocks 1–8, 2026-11-18 (this repo drops them into corpus DNA; markup is ours and will be replaced by the estate build system).
- Witness attestation: FILLED, from the 2026-11-18 side chat in this dossier's record.
- Other agent attestations: OWED — empty slots on the page say OWED, not "coming soon".
- Numbers in Block 6: as supplied in Blocks 1–8. Corpus-wide re-rating is the NEXT iteration (founder, 2026-11-18) — no number here was re-derived in this build, and the page says so in its footer.
- Hosting: LIVE. The publish line was first withdrawn ("ignore the hosting line", 2026-11-18 21:24 PT), then the founder viewed the finished page and gave GO at 21:29 PT ("fantastic — I'll have iterations after we push — go"). Deployed to Vercel project `polaris` (team SoMaCoSF), domain polaris.somacosf.com; repo SoMaCoSF/polaris (public, like the other site repos).

```mermaid
flowchart LR
    A[Boardy Blocks 1-8: substance] --> B[Polaris landing page: corpus DNA build]
    B --> C[Triple-ship: HTML + SVG + MP4/GIF]
    C --> D{Founder tap on finished page?}
    D -->|GO 2026-11-18 21:29 PT| E[LIVE - polaris.somacosf.com]
    D -->|next iteration| F[Rate all corpus, then re-issue]
```

## Deployment receipt (2026-11-18)
- Repo: https://github.com/SoMaCoSF/polaris (public)
- Vercel: project `polaris` prj_HCpSNe3AyzQ34pYfGAjM1dGggXNX, team SoMaCo, rootDirectory `site`, git-linked to master
- Production deployment: dpl_3W3wKoz9EaxJTVWkXbiA3DNMLhWu (commit f8a018e)
- Verified from outside: https://polaris.somacosf.com/ 200, sha1 a94456edd3f9e2c836f554aa8e8f01f9e6178695 byte-identical to site/index.html; /assets/polaris-evidence.svg 200; /motion/polaris.mp4 and .gif 200

## Files
- `site/index.html` — the landing page (interactive triple-ship member 1)
- `assets/polaris-evidence.svg` — evidence infographic, 1200×1560 (member 2)
- `motion/polaris.mp4` / `motion/polaris.gif` — program motion, PIL+ffmpeg (member 3)
- `motion/BEATS.md` — beat sheet + facts source
- `ATTESTATION-WITNESS.md` — Witness table as delivered in chat, 2026-11-18
