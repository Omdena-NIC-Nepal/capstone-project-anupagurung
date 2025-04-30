import os
import pandas as pd

def load_datasets():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "data")

    daily = pd.read_csv(os.path.join(data_path, "dailyclimate.csv"))
    stations = pd.read_csv(os.path.join(data_path, "meteorological-station-of-nepal.csv"))
    rainfall = pd.read_csv(os.path.join(data_path, "annual-and-seasonal-rainfall2014.csv"))
    temps = pd.read_csv(os.path.join(data_path, "anual-max-min-and-avg-temperaturetable01.csv"))

    return daily, stations, rainfall, temps

