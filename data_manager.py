
# Imports

import pandas as pd
import const
import logging
import schedule
import time
from os import listdir
from urllib.request import urlopen
from shutil import copyfileobj
from datetime import date
from datetime import timedelta
from datetime import datetime
from urllib.error import HTTPError
from pickle import dump

# !!! Check out "file_structure.md" to see where to get the data. !!!

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
        with open(f"data/{link}.csv", "rb") as f:
            df = pd.read_csv(f)
        
        df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
        # df = df.reset_index().groupby("Country/Region").sum().drop(['index'], axis=1)

        with open(f"storage/{link}_df.pkl", "wb") as f:
            dump(df, f)
        logging.info(f"Storing {link}...")

        print(df)

    # calculate active: active = confirmed - recovered - deaths
    
    logging.info("Done pulling data from jh")

    # Save today as last update
    last_update = date.today()
    with open("storage/last_update.pkl", "wb") as f:
        dump(last_update, f)

def per_population(**kwargs):
    """Returns a saved image that plots numbers about the corona crisis from different countries relative to their population.

    Keyword arguments: 
    category -- "dead", "cured", "infected" or "active".
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
