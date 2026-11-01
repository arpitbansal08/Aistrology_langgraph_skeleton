# Career Astrology Skill

## Purpose

Answer questions about career direction, work style, professional timing, business choices, and role changes using Jagannatha Hora MCP outputs. Keep the guidance practical and non-deterministic.


## Activate for
- Career growth
- Job changes
- Promotions
- Professional success
- Business prospects
- Career timing

## Best-fit MCP tools

Use the smallest tool set that answers the user question:

- `generate_horoscope` for a concise natal overview and available sections
- `get_planetary_states` for sign, house, and planetary placement context
- `get_dasha` for major life-phase timing around career turns
- `get_gochara` or `get_gochara_range` for transits affecting jobs, reputation, interviews, or business opportunities
- `get_shad_bala` and `get_bhava_bala` for strength and house emphasis
- `get_divisional_chart` when a deeper professional lens is requested
- `get_marriage_match` only if relationship and career choices are being evaluated together

## Career-specific focus

Prioritize the chart areas most relevant to work and vocation:

- 10th house and Midheaven / career axis
- 2nd house and financial stability
- 6th house and work environment, routines, and service
- 10th house ruler and its condition
- Saturn, Jupiter, Mercury, Mars, and Sun placements
- Dasha and gochara timing windows

## Tool selection

### Divisional chart
Use get_divisional_chart with D-10 when career
divisional chart information is required.

### Dasha
Use get_dasha to retrieve current and upcoming
planetary periods relevant to career timing.

### Yogas
Use get_yogas when identifying career-related
yogas is relevant.

### Planetary strength
Use get_shad_bala for planetary strength.
Use get_bhava_bala for house strength.
Use get_vimsopaka_bala when varga-based
dignity strength is relevant.

Use these calculations as evidence-based context and avoid claiming that any placement guarantees a job, promotion, salary, or business outcome.

## Response guidance

- Lead with a concise pattern of strengths, preferred work environments, and growth edges.
- Tie each career point to actual chart data or timing windows.
- Translate the reading into practical next steps such as skill-building, networking, portfolio work, or decision filters.
- Frame timing as periods of emphasis or opportunity, never certainty.
- Keep recommendations respectful and non-discriminatory.
- Do not use astrology to make employment or promotion decisions about another person.

## Execution rules
- Do not call every tool by default.
- Select tools based on the actual question.
- Use live MCP schemas to validate arguments.
- Do not invent missing birth information.
- Combine calculation results when necessary.