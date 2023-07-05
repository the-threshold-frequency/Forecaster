import requests
from api import get_api


def get_data(place, days=1):
    API_key = get_api()

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    df = response.json()
    value = 8*days
    fil = df['list']
    date = [i['dt_txt'] for i in fil][:value]
    t = [i['main']['temp']/10 for i in fil][:value]
    sky = [i['weather'][0]['main'] for i in fil][:value]

    url_current = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_key}"
    response_current = requests.get(url_current)
    df_current = response_current.json()
    temp_current = df_current['main']['temp'] / 10
    min_temp = df_current['main']['temp_min'] / 10
    max_temp = df_current['main']['temp_max'] / 10
    weather_current = df_current['weather'][0]['description']
    return date, t, sky, temp_current, weather_current, min_temp, max_temp


