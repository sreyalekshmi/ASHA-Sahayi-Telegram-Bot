# Ethical AI Statement – ASHA Sahayi

ASHA Sahayi is designed as a **support tool for ASHA workers**, not as a replacement for medical professionals or human judgment. Ethical considerations were central to both the design and implementation of this system.

## Medical Safety
- The bot provides **informational health guidance only**
- It does **not diagnose illnesses or prescribe medication**
- Every response encourages consultation with a doctor or health center when symptoms persist or worsen

## Human-in-the-Loop Design
- Final decisions, including follow-up requirements, are made **explicitly by the ASHA worker**
- The system supports decision-making but never automates medical conclusions

## Data Privacy & Protection
- Patient data is stored **locally using SQLite**
- No personal health data is shared publicly or reused beyond the current interaction
- API keys and sensitive credentials are managed using environment variables and excluded from version control

## Responsible Use of Generative AI
- AI outputs are constrained to conservative, safety-focused guidance
- Responses are framed to avoid panic, misinformation, or overconfidence
- The system is designed to respect local healthcare workflows and cultural context

ASHA Sahayi aims to demonstrate how **ethical, community-centered AI systems** can meaningfully support frontline healthcare workers while respecting trust, safety, and accountability.
