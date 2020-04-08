
# --- Imports --- #

import logging
import telegram
import telegram.ext
import pickle
import logging
import const


# --- Functions --- #

def choose_question(update, context):
    """Is called when user chooses a question. Stores the choice and gives user appropriate further options.
    """
    # Set up short vars
    bot = context.bot
    choice = update.message.text
    chat_id = update.effective_user.id

    # Store choice

    # Understand what question was chosen
    if choice == "Pro 1000 Einwohner":
        keyboard = const.category_keyboard
        text = "Wähle jetzt eine Kategorie"
        next_state = const.States.CHOOSE_CATEGORY

    elif choice == "Ab 100. Fall":
        keyboard = const.category_keyboard
        text = "Wähle jetzt eine Kategorie"
        next_state = const.States.CHOOSE_CATEGORY

    elif choice == "Corona / durchschnittliche Tote":
        keyboard = const.remove_keyboard
        text = "Wähle jetzt Länder, die du vergleichen willst"
        next_state = const.States.CHOOSE_COUNTRIES

    else:
        # User chose invalid category
        keyboard = const.question_keyboard
        text = "Das ist keine gültige Kategorie"
        next_state = const.States.CHOOSE_QUESTION

    # Reply to user
    bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)
    return next_state

def choose_category(update, context):
    """Is called when user chooses a category. Stores the choice and gives user appropriate further options.
    """
    # Short vars
    bot = context.bot
    chat_id = update.effective_user.id
    text = "Wähle jetzt Länder, die du vergleichen willst"

    # Store choice

    # Reply to user
    keyboard = const.remove_keyboard
    bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)
    return const.States.CHOOSE_COUNTRIES

def choose_countries(update, context):
    # Short vars
    bot = context.bot
    chat_id = update.effective_user.id
    text1 = "Danke! Hier sind deine Daten:"
    text2 = "Wähle gerne eine nächste Frage aus"
    keyboard = const.question_keyboard

    # Reply to user
    bot.send_message(chat_id=chat_id, text=text1)
    bot.send_message(chat_id=chat_id, text=text2, reply_markup=keyboard)
    return const.States.CHOOSE_QUESTION

def cancel(update, context):
    # Short vars
    bot = context.bot
    chat_id = update.effective_user.id
    text= "Was willst du wissen?"
    keyboard = const.question_keyboard

    # Reply to user
    bot.send_message(chat_id=chat_id, text=text2, reply_markup=keyboard)
    return const.States.CHOOSE_QUESTION

def start(update, context):
    keyboard = const.question_keyboard
    context.bot.send_message(chat_id=update.effective_user.id, text="Willkommen! Ich bin der CoronaBot. Klick dich gerne durch meine Menüs.", reply_markup=keyboard)

    return const.States.CHOOSE_QUESTION


def main():
    logging.basicConfig(level=logging.INFO)

    # set up updater & dispatcher
    with open("storage/token.pkl", "rb") as f:
        token = pickle.load(f)
    updater = telegram.ext.Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Create ConversationHandler
    entry_points = [telegram.ext.CommandHandler("start", start)]
    states = {
        const.States.CHOOSE_QUESTION : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_question)],
        const.States.CHOOSE_COUNTRIES : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_countries)],
        const.States.CHOOSE_CATEGORY : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_category)]
    }

    fallbacks = [telegram.ext.CommandHandler("abbrechen", cancel)]
    conv = telegram.ext.ConversationHandler(entry_points, states, fallbacks)
    dispatcher.add_handler(conv)

    logging.info("Waiting for updates...")
    updater.start_polling()
    updater.idle()

# Run main function when opened as script
if __name__ == "__main__":
    main()