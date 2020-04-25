
import pickle
from data_manager import update_data
from telegram import Bot
from telegram.error import InvalidToken

def main():
    update_data()

    print("Please input your bot token:")
    token = input()

    try:
        bot = Bot(token=token)

        with open("storage/token.pkl", "wb") as f:
            pickle.dump(token, f)

        print("Stored token successfully.")

    except InvalidToken:
        print("Invalid token.")


if __name__ == "__main__":
    main()