
# Imports

import const
import logging
from os import listdir
from urllib.request import urlopen
from shutil import copyfileobj
from datetime import date
from datetime import timedelta
from urllib.error import HTTPError
from datetime import date
from pickle import dump

# !!! Check out "file_structure.md" to see where to get the data. !!!

def update_data():
    """Pulls up to date data into the "data/"-folder."""

    logging.basicConfig(level=logging.INFO)

    # Figure out how much data we have
    file_names = listdir("data/daily_reports")
    file_names = sorted(file_names)
    if (len(file_names) > 0):
        last_entry = file_names[-1]
    else:
        last_entry = const.first_jh_daily_entry

    # Try to get newer files until the server declines 
    one_day = timedelta(days=1)
    current_date = date.fromisoformat(last_entry[:-4])
    current_date += one_day # starting with the entry of the day after the last one we have
    while(True):
        url = const.jh_url
        jh_file_name = "{:02d}-{:02d}-{}.csv".format(
            current_date.month,
            current_date.day,
            current_date.year)
        url += jh_file_name

        logging.info(f"Pulling from {url}...")

        try:
            with urlopen(url) as response, open(f"data/daily_reports/{current_date}.csv", "wb") as f:
                copyfileobj(response, f) # TODO: dahin: 
        except HTTPError as e:
            if e.code == 404:
                print(f"Could not pull from {url}")
                break
            else:
                raise e     

        current_date += one_day

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


