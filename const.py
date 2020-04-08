
# Define states for the ConversationHandler

class States():
    CHOOSE_QUESTION = 0
    CHOOSE_CATEGORY = 1
    CHOOSE_COUNTRIES = 2

question_keyboard = {
    "keyboard" : [
        ["Pro 1000 Einwohner"],
        ["Ab 100. Fall"],
        ["Corona / durchschnittliche Tote"]
    ],
    "resize_keyboard" : True
}

category_keyboard = {
    "keyboard" : [
        ["Tote", "Infizierte"],
        ["Geheilte", "Aktive"]
    ],
    "resize_keyboard" : True
}

remove_keyboard = {
    "remove_keyboard" : True
}

