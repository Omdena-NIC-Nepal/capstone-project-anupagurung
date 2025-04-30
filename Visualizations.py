import plotly.express as px

def plot_temperature_trend(data, district):
    return px.line(data[data['District'] == district], x="Date", y="Temp_2m", title=f"Temperature Trend - {district}")

def plot_precipitation_trend(data, district):
    return px.line(data[data['District'] == district], x="Date", y="Precip", title=f"Precipitation Trend - {district}")

def plot_station_distribution(data):
    return px.histogram(data, x="District", title="Number of Stations per District")
