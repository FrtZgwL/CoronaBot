
import pickle
from telegram import Bot
from telegram.error import InvalidToken

def main():
    print("Please input your bot token:")
    token = input()

    try:
        bot = Bot(token=token)

        with open("storage/token.pkl", "wb") as f:
            pickle.dump(token, f)

        print("Token erfolgreich gespeichert.")

    except InvalidToken:
        print("Ungültiges Token.")


if __name__ == "__main__":
    main()