import requests


def neighbourhoods() -> dict:
    url= f"https://data.police.uk/api/leicestershire/neighbourhoods"
    response_json = requests.get(url).json()
    return response_json

def street_crimes() -> dict:
    " Geef een criminele activiteit in de wijk. "
    url= f"https://data.police.uk/docs/method/crime-street/"
    response_json = requests.get(url).json()
    return response_json["drinks"][0]

def forces() -> dict:
    " Geef de verschillende forces. "
    url= f"https://data.police.uk/api/forces"
    response_json = requests.get(url).json()
    return response_json["drinks"][0]

def specificneighbourhood(specific_code: str) -> dict:
    " Geef de verschillende forces. "
    url= f"https://data.police.uk/api/leicestershire/{specific_code}"
    response_json = requests.get(url).json()
    return response_json

def stopandsearch() -> dict:
    " Geef de verschillende forces. "
    url= f"https://data.police.uk/api/stops-street?date=2024-01&lat=52.629729&lng=-1.131592"
    response_json = requests.get(url).json()
    return response_json