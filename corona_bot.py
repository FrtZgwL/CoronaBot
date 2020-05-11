
# --- Imports --- #

import logging
import telegram
import telegram.ext
import pickle
import logging
import const
import data_manager


# --- Functions --- #

def choose_question(update, context):
    """Is called when user chooses a question. Stores the choice and gives user appropriate further options.
    """
    # Set up short vars
    bot = context.bot
    chat_id = update.effective_user.id
    choice = update.message.text

    # Store choice
    context.user_data["question"] = choice

    # Understand what question was chosen
    if choice == "Bevölkerung":
        keyboard = const.category_keyboard
        text = "Wähle jetzt eine Kategorie"
        next_state = const.States.CHOOSE_CATEGORY

    elif choice == "Beginn":
        keyboard = const.category_keyboard
        text = "Wähle jetzt eine Kategorie"
        next_state = const.States.CHOOSE_CATEGORY

    elif choice == "Kuchen":
        keyboard = const.contries_keyboard
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
    choice = update.message.text

    if choice == "Zurück":
        keyboard = const.question_keyboard
        text = "Was willst du wissen?"
        bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)

        return const.States.CHOOSE_QUESTION
    else:
        # Store choice
        context.user_data["category"] = const.translate_category[choice]

  # Reply to user
        keyboard = const.contries_keyboard
        text = "Wähle jetzt Länder, die du vergleichen willst"
        bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)

        return const.States.CHOOSE_COUNTRIES

def choose_countries(update, context):
    logging.basicConfig(leve=logging.INFO)

    # Short vars
    bot = context.bot
    chat_id = update.effective_user.id
    choice = update.message.text
    try:
        country = const.emoji_to_country[choice]
    except KeyError:
        country = ""
    

    if choice == "Zurück":
        text = "Was willst du wissen?"
        keyboard = const.question_keyboard
        bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)

        return const.States.CHOOSE_QUESTION

    elif choice == "Andere Länder":
        print("WIP")

    elif choice == "Bestätigen":
        question = context.user_data["question"]

        # Send data
        if "category" in context.user_data:
            category = context.user_data["category"]

        countries = context.user_data["countries"]
        photos = []

        logging.info(f"Sending graph for question:{question}; category:{category}; countries:{countries}.")

        # TODO: Move this down when function is fixed: Reset user storage
        context.user_data["question"] = ""
        context.user_data["category"] = ""
        context.user_data["countries"] = []

        if question == "Bevölkerung":
            photos = [data_manager.per_population(category=category, countries=countries)]

        elif question == "Beginn":
            photos = [data_manager.since_outbreak(category=category, countries=countries)]

        elif question == "Kuchen":
            photos = data_manager.compare_deaths(countries=countries)

        # Send data to user
            # Construct last_update string
        try:
            with open("storage/last_update.pkl", "rb") as f:
                last_update = pickle.load(f)
            last_update_str = f"{last_update.day}.{last_update.month}.{last_update.year}"
        except FileNotFoundError as e:
            last_update_str = "Noch keine Updates"
        

        text = f"Hier sind deine Daten:\n_(letztes Update am {last_update_str})_"
        bot.send_message(chat_id=chat_id, text=text, parse_mode="Markdown")
        for photo in photos:
            bot.send_photo(chat_id=chat_id, photo=photo)

        text = "Was willst du wissen?"
        keyboard = const.question_keyboard
        bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)

        return const.States.CHOOSE_QUESTION

    elif country != "":
        # keep asking until done
        context.user_data["countries"].append(country)
        text = "Danke! Was sind weitere Länder, die du vergleichen willst?"
        bot.send_message(chat_id=chat_id, text=text)

        return const.States.CHOOSE_COUNTRIES

    else:
        text = "Das verstehe ich nicht. Bitte sende mir nur einzelne Flaggen."
        bot.send_message(chat_id=chat_id, text=text)

        return const.States.CHOOSE_COUNTRIES

def start(update, context):
    # Set up user storage
    context.user_data["countries"] = []

    # Short vars
    chat_id = update.effective_user.id
    text = const.welcome_message

    keyboard = const.question_keyboard
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard, parse_mode="Markdown")

    return const.States.CHOOSE_QUESTION


def main():
    logging.basicConfig(level=logging.INFO)

    # set up updater & dispatcher
    with open("storage/token.pkl", "rb") as f:
        token = pickle.load(f)
    persistence = telegram.ext.PicklePersistence(filename="storage/bot_storage.pkl") # The states of the ConversationHandler, user_data and bot_data are stored here
    updater = telegram.ext.Updater(token=token, use_context=True, persistence=persistence)
    dispatcher = updater.dispatcher

    # Create ConversationHandler
    entry_points = [telegram.ext.CommandHandler("start", start)]
    states = {
        const.States.CHOOSE_QUESTION : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_question)],
        const.States.CHOOSE_COUNTRIES : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_countries)],
        const.States.CHOOSE_CATEGORY : [telegram.ext.MessageHandler(telegram.ext.Filters.text, choose_category)]
    }
    fallbacks = []
    menu_navigation = telegram.ext.ConversationHandler(entry_points, states, fallbacks, persistent=True, name="menu_navigation")
    dispatcher.add_handler(menu_navigation)

    logging.info("Waiting for updates...")
    updater.start_polling()
    updater.idle()

# Run main function when opened as script
if __name__ == "__main__":
    main()
