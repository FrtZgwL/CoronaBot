
import pickle
import pandas as pd
from data_manager import update_data
from telegram import Bot
from telegram.error import InvalidToken

def main():
    # TODO: Das später unter user Input
    # --- Get up to date data for the first time --- #

    update_data()


    # --- Create clean populations- and deathrate DataFrames --- #

    # load populations data
    pop_df = pd.read_csv("data/populations.csv", sep=";")
    pop_df = pop_df[["Country (or dependency)", "Population (2020)"]]
    pop_df.columns = ["country", "population"]
    pop_df = pop_df.set_index("country")

    def turn_to_int(input_str):
        int_number = int("".join(input_str.split(",")))
        return int_number

    pop_df = pop_df.applymap(turn_to_int)

    # make populations data compatible with jh data
    with open("storage/cases_df.pkl", "rb") as f:
        jh_df = pickle.load(f)

    jh_names = jh_df["Country/Region"].values
    jh_names = set(jh_names) # remove duplicate names in jh name list

    pop_names = pop_df.index.values

    final_dict = {}
    # for every name in jh
    for jh_name in jh_names:
        # if jh name in population data: store amount
        if jh_name in pop_names:
            final_dict[jh_name] = [pop_df.loc[jh_name]["population"]]
        # else: store `-1
        else:
            final_dict[jh_name] = [-1]

    pop_df = pd.DataFrame(final_dict)
    pop_df = pop_df.T
    pop_df.columns = ["population"]

    with open("storage/populations_df.pkl", "wb") as f:
        pickle.dump(pop_df, f)


    # --- Get Bot Token from user --- #

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