
# Imports

import pandas as pd
import const
import logging
import schedule
import time
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from os import listdir
from urllib.request import urlopen
from shutil import copyfileobj
from datetime import date, timedelta, datetime
from urllib.error import HTTPError
from pickle import dump, load

# !!! Check out "file_structure.md" to see where to get the data. !!!

def pickle_this(pickle_object, pickle_object_path):
    with open(pickle_object_path, "wb") as f:
        dump(pickle_object, f)

def unpickle_this(pickle_object_path):
    with open(pickle_object_path, "rb") as f:
        object = load(pickle_object_path)
        return(object)

def update_data():
    """Pulls up to date data into the "data/"-folder."""

    logging.basicConfig(level=logging.INFO)
    logging.info(f"{datetime.now()}, Starting to pull data...")

    # get confirmed, deaths and recovered from jh
    links = {
        "confirmed" : "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        "deaths" : "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        "recovered" : "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    }

    for link in links:
        logging.info(f"Pulling {link} from {links[link]}...")

        # Pull from jh server
        with urlopen(links[link]) as response, open(f"data/{link}.csv", "wb") as f:
            copyfileobj(response, f)

        # Store as pd df
        df = unpickle_this(f"data/{link}.csv")
        #with open(f"data/{link}.csv", "rb") as f:
        #    df = pd.read_csv(f)

        # Remove uneccecary columns
        df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)

        # Aggregating all rows with the same country name
        df = df.groupby("Country/Region").sum()

        # Store
        pickle_this(df, f"storage/{link}_df.pkl")
        # with open(f"storage/{link}_df.pkl", "wb") as f:
        #    dump(df, f)

        logging.info(f"Storing {link}...")

        print(df)

    # Open dfs for creating the active cases df
    confirmed_df = unpickle_this(f"storage/confirmed.pkl")
    deaths_df = unpickle_this(f"storage/deaths.pkl")
    recovered_df = unpickle_this(f"storage/recovered.pkl")


    # Calculate active: active = confirmed - recovered - deaths
    # The ".value" attribute returns an nd-array(n-dimensional) of the values in the data frame.
    active_nd = confirmed_df.values - deaths_df.values - recovered_df.values

    # Copying column and index names from another df for turning
    # the  active cases nd-array into a pandas data frame

    countries = confirmed_df.index
    dates = confirmed_df.columns

    active_df = pd.DataFrame(active_nd, index = countries, columns = dates)

    #store
    pickle_this(active_df,f"storage/active_df.pkl")


    logging.info(f"Storing {link}...")

    logging.info("Done pulling data from jh")

    # Save today as last update
    last_update = date.today()
    with open("storage/last_update.pkl", "wb") as f:
        dump(last_update, f)

def per_population(category, countries):
    """Returns a saved image that plots numbers about the corona crisis from different countries relative to their population.

    Keyword arguments:
    category -- "dead", "cured", "infected" or "active". // rename DEATHS
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    """
    print(kwargs)
    return(open("isaac-smith-6EnTPvPPL6I-unsplash.jpg", "rb"))

def since_outbreak(**kwargs):
    """Returns a saved image that plots numbers about the corona crisis from different countries per day since the day they reached 100 cases.

    Keyword arguments:
    category -- "dead", "cured", "infected" or "active".
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    """
    print(kwargs)
    return(open("isaac-smith-6EnTPvPPL6I-unsplash.jpg", "rb"))

def compare_deaths(**kwargs):
    """Returns a list of saved images that show a cake-diagram that compares corona deaths with all other deaths.

    We assume that an average amount of people died since the first corona cases. (to compute this see "data/death_counts.csv") We assume that all people that are listed under corona-deaths would not have died otherwise. So we conclude that the total amount of deaths since the first corona cases is the average amount of deaths + the deaths from corona. This function shows how much of the total amount of deaths since the first corona cases are deaths from corona.

    Keyword arguments:
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    """
    print(kwargs)
    photos = []
    for i in range(len(kwargs)):
        photos.append(open("isaac-smith-6EnTPvPPL6I-unsplash.jpg", "rb"))
    return(photos)

def main():
    logging.basicConfig(level=logging.INFO)

    # Update data daily
    schedule.every().day.at("18:09").do(update_data)
    logging.info("Data Updater running...")

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    main()
