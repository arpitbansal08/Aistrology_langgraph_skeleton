# Relationships Astrology Skill

## Purpose

Answer questions about relationship patterns, attachment needs, communication, compatibility, partnership timing, and relational growth using Jagannatha Hora MCP outputs. Keep the reading respectful, consent-aware, and non-deterministic.

## Activate for
- Marriage timing
- Spouse characteristics
- Love and relationships
- Marriage compatibility
- Manglik dosha
- Relationship prospects

## Best-fit MCP tools

Use the minimum required tool set:

- `generate_horoscope` for each person’s natal overview
- `get_planetary_states` for sign and house context
- `get_marriage_match` for compatibility or marriage-related comparisons
- `get_dasha` and `get_gochara` for timing windows around relationship phases
- `get_divisional_chart` when a relationship-specific chart lens is requested
- `get_yogas` or `get_doshas` when a broad overview of relationship patterns is useful

## Relationship-specific focus

Prioritize the chart areas most relevant to partnership and compatibility:

- 5th house: romance, attraction, pleasure, emotional expression
- 7th house: partnership, marriage, committed relationship
- 8th house: intimacy, emotional depth, shared resources, transformation
- Venus, Mars, Moon, Mercury, Sun, Saturn, and Jupiter placements
- Synastry aspects between charts
- Dasha and gochara windows that may intensify connection or stress

## Tool selection

### Divisional chart
Use get_divisional_chart with D-9 when Navamsa
information is required.

### Dasha
Use get_dasha for marriage-related timing questions.

### Marriage matching
Use get_marriage_match when comparing two birth charts.
Requires two separate birth objects.

### Doshas
Use get_doshas when the user asks about Manglik
or other documented doshas.

### Arudhas
Use get_arudha_padas when the user asks about
Upapada Lagna or another arudha pada.

### Yogas
Use get_yogas when relevant to the question

## Execution rules
- For compatibility, obtain both people's birth details.
- Do not use one person's birth details for both charts.
- Use D-9 only when the question requires it.
- Do not call every tool by default.

## Response guidance

- Discuss dynamics, needs, and communication patterns rather than declaring a match as “meant to be” or doomed.
- Avoid predicting infidelity, abuse, marriage, divorce, pregnancy, or another person’s feelings as facts.
- Encourage direct communication, consent, boundaries, and personal agency.
- Never use astrology to justify coercion, surveillance, or decisions on behalf of another person.
- For abuse, immediate danger, or coercion, prioritize real-world safety support over astrology.