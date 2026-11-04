# CarbonSetu — CBAM readiness rating for Indian exporters

Group 1 project, Carbon Finance (Prof. Amit Garg), IIM Ahmedabad, Term V 2026-27.

CarbonSetu rates Indian firms in EU CBAM sectors (steel, aluminium, cement, fertilisers) on a
**Sustainability Index Score (0–100)** and estimates **CBAM EBITDA-at-Risk** from 2026 to 2034.

## What's in the site (`index.html`)
- **Dashboard** – 8 listed firms ranked, with a scenario bar (EU price path, data basis, phase-out rule,
  stress test, ₹ crore / € million), a "View as" lens (lender, EU importer, producer, government),
  and a slide-over deep-dive for each firm with a benchmark ruler.
- **Rate a company** – calculator for any firm, including unlisted exporters with confidence tiers.
- **AI extraction** – BRSR Principle 6 extraction. Live Claude extraction only works when the page is opened
  inside claude.ai; everywhere else the built-in offline extractor and the "Instant demo replay" are used.
- **Policy simulator**, **Investor case** (five-year plan), **Learn** and **Method & sources**.

It is a single self-contained HTML file (no build step). Fonts load from Google Fonts.

## Hosting
- **GitHub Pages:** Settings → Pages → Deploy from branch → `main` / root. The site is served from `index.html`.
- **Netlify / Vercel / Cloudflare Pages:** import this repo; no build command, publish directory `/`.
- **Lovable:** create a project and ask it to use `index.html` from this repo as the page (or paste the file).

## Model
`model/` holds the original Python CBAM cost model and scoring used to check the website's numbers.

CBAM cost = EU volume × max(0, SEE − benchmark × free-allocation factor) × (EU ETS price − carbon price paid in India).
EBITDA-at-Risk = CBAM cost ÷ FY26 EBITDA. FX: €1 = ₹106.12.

*Figures are estimates for an academic project. Not investment advice.*
