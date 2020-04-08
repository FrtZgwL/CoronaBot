
# File Structure #

- __The data we analyze:__
    + stored as ".csv"
    + Day to day corona data is stored in "data/" as ".csv"-files with the name of the date. For example "data/04-07-2020.csv" Remember to run data.manager.update_data() to pull fresh data from the Internet.
    + Population sizes are stored in "data/populations.csv".
    + Death counts are stored in "data/death_counts.csv".
- __The data we generate:__
    + python objects that need to be stored are pickled and stored in "storage/" as a ".pkl" file.