
# Imports

import pandas as pd
import numpy as np
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
from glob import glob


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
        with open(f"data/{link}.csv", "rb") as f:
            df = pd.read_csv(f)

        # Remove uneccecary columns
        df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)

        # Aggregating all rows with the same country name
        df = df.groupby("Country/Region").sum()

        # Creating the DataFrame with values per 100.000 citizens
        with open(f"data/populations.csv", "rb") as f:
            populations = pd.read_csv(f)

        # Store
        pickle_this(df, f"storage/{link}_df.pkl")
        # with open(f"storage/{link}_df.pkl", "wb") as f:   ### Bin mir nicht sicher, ob das funktioniert
        #    dump(df, f) ### Bin mir nicht sicher, ob das funktioniert

        # Get the data frame with all values in relation to their population size
        # Formula = df_values / population count * 100.000
        df_per_population = np.divide(df.values.T, populations).T  # df_values / population
        df_per_population = df_per_population*100000
        pickle_this(df, f"storage/{link}_per_population_df.pkl")
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

    #storenp.core.defchararray.add
    pickle_this(active_df,f"storage/active_df.pkl")


    logging.info(f"Storing {link}...")

    logging.info("Done pulling data from jh")

    # Save today as last update
    last_update = date.today()
    with open("storage/last_update.pkl", "wb") as f:
        dump(last_update, f)

def filter_countries_in_country_list(DataFrame, country_list):
    """Creates a new df with by extracting the rows of the original
    dataframe, that contain the passed country names """

    df = DataFrame.loc[country_list]
    return(df)

def plot_title(category, country_list):
    category_title_names = {
        "deadths" : "Deaths",
        "active" : "Active cases",
        "infected" : "Infected",
        "cured": "Cured cases"
    }
    # Defining the first words of the title
    for category_name, category_title_name in category_title_names.items():
        if category_name == category:
            Title_beginning = category_title_name

    Title= Title_beginning+' for countries: \n'

    # Adding countries shown in plot to title
    for i in range(len(country_list)):
        # Add country to the list with comma if it is not the last one
        if country_list[i]!= country_list[-1]:
            Title = Title+country_list[i]+", "
        # Add country to the list with "and" and period if it is the last one
        else:
            Title = Title+'and '+country_list[i]+"."
    return(Title)


def per_population(): # define formatulation(category, country_list):
    """Returns a df saved image that plots numbers about the corona crisis from different countries relative to their population.

    Keyword arguments:
    category -- "dead", "cured", "infected" or "active". // rename DEATHS
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    """

    df = f"storage/{category}_per_population_df.pkl"
    df = filter_countries_in_country_list(df)

    # Tanspose aka pivot
    df = df.T
    # Initiate plot
    plt.plot()

    # Converting the dates (indecies of df) to the data type datetime
    # This enables me to modify the dateformat with matplotlib
    x_values = pd.to_datetime(df.index) # List of dates

    # Adding the graphs for countries in country_list to the plot
    for country in df.columns: # Selected countries
        # Converting the column name into a list. Prequisit for .plot()  ## not entirely sure...
        y_values = df[country].tolist()
        plt.plot(x_values,y_values)

    #Format the date to something like: Apr,02 2042
        # Define format
    date_format = mpl_dates.DateFormatter('%b, %d, %Y')
        # format the dates
    plt.gca().xaxis.set_major_formatter(date_format)
        # Rotate the dates
    plt.gcf().autofmt_xdate()

    Title = plot_title(category, country_list)
    plt.title(Title)
    plt.savefig("Plot.png") ### bin mir nicht sicher ob das hier sein kann oder in die Funktionen unten rein muss
    return(open("Plot.png", "rb"))

def since_outbreak(**kwargs):
    """Returns a saved image that plots numbers about the corona crisis from different countries per day since the day they reached 100 cases.

    Keyword arguments:
    category -- "dead", "cured", "infected" or "active".
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    """



    print(kwargs)
    return(open("isaac-smith-6EnTPvPPL6I-unsplash.jpg", "rb"))

def compare_deaths(country_list):
    """Returns a list of saved images that show a cake-diagram that compares corona deaths with all other deaths.

    We assume that an average amount of people died since the first corona cases. (to compute this see "data/death_counts.csv") We assume that all people that are listed under corona-deaths would not have died otherwise. So we conclude that the total amount of deaths since the first corona cases is the average amount of deaths + the deaths from corona. This function shows how much of the total amount of deaths since the first corona cases are deaths from corona.

    Keyword arguments:
    countries -- List with country names. For example ["Germany", "Italy", "USA"]
    death_rates -- df with death rates for all countries
    """


    df = unpickle_this(f"storage/deaths.pkl")
    df = filter_countries_in_country_list(df, country_list)

    with open(f"data/{death_rates}.csv", "rb") as f:
        death_rates = pd.read_csv(f) # Define that this is the time from the beginning of our research

    #converting death_rates into Series   ## maybe this should be in the setup
    index = death_rates['countries'].tolist()
    values = death_rates['death_rate'].values
    death_rates_s = pd.Series(values, index = index)

    image_count = 0

    for i in range(len(country_list)):
        plt.plot()
        # calculate the sizes of the pie slices
        country = country_list[i]
        days_regarded = len(df)
        corona_deaths_in_days_regarded = df.loc[country].sum()
        Normal_deaths_in_days_regarded = days_regarded * death_rates_s[country]
        all_deaths = Normal_deaths_in_days_regarded + corona_deaths_in_days_regarded

        #Slice sizes
        normal_deaths = Normal_deaths_in_days_regarded/all_deaths
        corona_deaths = corona_deaths_in_days_regarded/corona_deaths_in_days_regarded

        labels = country_list
        sizes = [normal_deaths, corona_deaths]
        colors = ['blue', 'green']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90) // what are these texts?
        plt.legend(patches, labels, loc="best")
        plt.show()

        image_number = str(image_count)
        plt.savefig(f"Plot-{image_number}.png")
        image_count += 1

    image_paths = glob("*.png")
    return (image_paths)



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
