# ===============================
# ASHA SAHAYI – Telegram Bot
# Multilingual + GenAI Backend
# ===============================

import sqlite3
from datetime import datetime, timedelta
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ai_handler import get_ai_reply

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ai_handler import get_ai_reply
from db import init_db, insert_visit, insert_followup

BOT_TOKEN = ""



# Store last visit per chat
last_visit_id = {}

def start(update, context):
    update.message.reply_text(
        "🙏 നമസ്കാരം!\n"
        "ഞാൻ ASHA Sahayi.\n\n"
        "രോഗിയുടെ വിവരങ്ങൾ ഇങ്ങനെ അയയ്ക്കുക:\n"
        "പേര്:\nപ്രായം:\nസ്ഥലം:\nലക്ഷണം:"
    )

def parse_patient_message(text):
    data = {"name": "Unknown", "age": 0, "location": "Not specified", "symptoms": text}

    for line in text.split("\n"):
        if "പേര്" in line:
            data["name"] = line.split(":")[-1].strip()
        elif "പ്രായം" in line:
            try:
                data["age"] = int(line.split(":")[-1].strip())
            except:
                data["age"] = 0
        elif "സ്ഥലം" in line:
            data["location"] = line.split(":")[-1].strip()
        elif "ലക്ഷണം" in line:
            data["symptoms"] = line.split(":")[-1].strip()

    return data

def handle_message(update, context):
    chat_id = str(update.message.chat_id)
    text = update.message.text

    patient = parse_patient_message(text)
    ai_reply = get_ai_reply(patient["symptoms"])

    visit_id = insert_visit(
        chat_id,
        patient["name"],
        patient["age"],
        patient["location"],
        patient["symptoms"],
        ai_reply
    )

    last_visit_id[chat_id] = visit_id

    update.message.reply_text(
        ai_reply +
        "\n\n❓ ഈ രോഗിക്ക് follow-up ആവശ്യമുണ്ടോ?\n"
        "👉 /followup_yes അല്ലെങ്കിൽ /followup_no\n\n"
        "⚠️ ഇത് വിവര സഹായം മാത്രമാണ്. ഡോക്ടറെ സമീപിക്കുക."
    )

def followup_yes(update, context):
    chat_id = str(update.message.chat_id)

    if chat_id in last_visit_id:
        insert_followup(last_visit_id[chat_id], "YES")
        update.message.reply_text("✅ Follow-up ആവശ്യമാണ് എന്ന് രേഖപ്പെടുത്തി.")
    else:
        update.message.reply_text("⚠️ ആദ്യം രോഗിയുടെ വിവരങ്ങൾ നൽകുക.")

def followup_no(update, context):
    chat_id = str(update.message.chat_id)

    if chat_id in last_visit_id:
        insert_followup(last_visit_id[chat_id], "NO")
        update.message.reply_text("✅ Follow-up ആവശ്യമില്ല എന്ന് രേഖപ്പെടുത്തി.")
    else:
        update.message.reply_text("⚠️ ആദ്യം രോഗിയുടെ വിവരങ്ങൾ നൽകുക.")

def parse_patient_data(text):
    name = "Unknown"
    age = 0
    location = "Not specified"
    symptoms = text

    lines = text.split("\n")

    for line in lines:
        if "പേര്" in line:
            name = line.split(":")[-1].strip()
        elif "പ്രായം" in line:
            try:
                age = int(line.split(":")[-1].strip())
            except:
                age = 0
        elif "സ്ഥലം" in line:
            location = line.split(":")[-1].strip()
        elif "ലക്ഷണം" in line:
            symptoms = line.split(":")[-1].strip()

    return name, age, location, symptoms



def main():
    init_db()

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("followup_yes", followup_yes))
    dp.add_handler(CommandHandler("followup_no", followup_no))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
