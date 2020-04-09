

# Check out "file_structure.md" to see where to get the data.

def update_data():
    """Pulls up to date data into the "data/"-folder."""
    print("WIP")

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


