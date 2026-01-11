# ASHA Sahayi – Telegram Bot for Frontline Health Workers

ASHA Sahayi is a lightweight Telegram-based assistant built to support **ASHA workers** during their day-to-day field visits.  
The bot combines **Generative AI**, **local-language interaction**, and **structured data logging** to make community healthcare work simpler, faster, and more traceable — without replacing human judgment.

This project was developed as part of a technical task focused on applying **AI responsibly for social good**, particularly in rural and community healthcare settings.

---

## Why ASHA Sahayi?

ASHA workers work under real constraints:
- Many household visits in a single day  
- Repeated symptom-related questions  
- Manual note-taking and follow-up tracking  
- Communication in local languages  

ASHA Sahayi is designed to **assist, not automate**.  
It acts as a digital companion that helps ASHA workers:
- Get quick, safe health guidance
- Log patient visits without extra effort
- Track follow-up needs clearly
- Work comfortably in their **own language**

---

## What the Bot Does

### 🧠 AI-Assisted Medical Guidance
- Uses a **Generative AI backend** to provide *basic, informational* health guidance
- Focuses on common primary symptoms (fever, cold, fatigue, etc.)
- Responses are intentionally conservative and safety-focused
- The bot clearly states it is **not a doctor** and encourages medical consultation when needed

### 📝 Patient Visit Logging (Database Integration)
For every patient interaction, the bot automatically stores:
- Patient name  
- Age  
- Location / ward  
- Reported symptoms  
- AI-generated response  
- Timestamp  

All data is stored locally using **SQLite**, demonstrating clear database design and management.

### 🔁 Follow-up Tracking (Innovative Element)
After each visit, the ASHA worker explicitly decides whether follow-up is needed using:

/followup yes
or
/followup no


Follow-ups are stored in a **separate table**, linked to the original visit.  
This mirrors real ASHA workflows and highlights cases that need continued attention.

### 🌐 Multilingual Capability
- Designed to communicate in **Malayalam**
- Handles English input correctly
- Easily extensible to other Indian languages (Tamil / Hindi)
- Ensures culturally and linguistically appropriate interaction

---

## Simple Example Flow

**ASHA worker enters patient details:**

- പേര്: അനു
- പ്രായം: 6
- സ്ഥലം: ഹരിപ്പാട് വാർഡ് 3
- ലക്ഷണം: രണ്ട് ദിവസമായി പനി


**Bot response (in the regional language : here Malayalam ):**
- Gives basic care advice  
- Clearly states it is **not a doctor** 
- Advises visiting a health center if symptoms continue
- Asks the ASHA worker if a followup cheacking is required or not

**ASHA worker marks follow-up decision** as /followup yes or /followup no
The visit will be stored in the **patient_visits** table  and the follow-up decision in the **followups** table respectively.


## Ethical AI Statement

ASHA Sahayi follows a **responsible and human-centered AI approach**:

- The bot does **not diagnose illnesses or prescribe medication**
- All responses are **informational support only**
- Users are always encouraged to consult doctors or health centers
- Patient data is stored locally and not shared publicly
- API keys and sensitive data are protected using environment variables
- The system is designed to **support ASHA workers’ judgment**, not override it

---

## Technology Stack

- Python  
- python-telegram-bot  
- SQLite (local database)  
- Generative AI API (Groq)  
- Pandas (for Excel export)

---

## Purpose

This project demonstrates how **lightweight AI systems** can be thoughtfully applied in real-world healthcare contexts.  
The focus is not just on building a chatbot, but on **designing technology that respects community workflows, ethical boundaries, and local realities**, while genuinely supporting frontline healthcare workers.

