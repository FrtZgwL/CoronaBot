
# File Structure #

- __The data we analyze:__
    + stored as ".csv"
    + Day to day corona data is stored in "data/" as ".csv"-files with the name of the date. For example "data/2020-04-07.csv" (YYYY-MM-DD) Remember to run data.manager.update_data() to pull fresh data from the Internet. We are using the [international standard time notation](https://www.cl.cam.ac.uk/~mgk25/iso-time.html).
    + Population sizes are stored in "data/populations.csv".
    + Death counts are stored in "data/death_counts.csv".
- __The data we generate:__
    + python objects that need to be stored are pickled and stored in "storage/" as a ".pkl" file.