import requests



def neighbourhoods(search:str) -> dict:
    "geef de eerste wijk die er is. "
    url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}"
    response_json = requests.get(url).json()

    if response_json == {"drinks": None}:
        return False
    return response_json["drinks"][0]

def get_random_drink() -> dict:
    " Geef een random drankje "
    url= f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response_json = requests.get(url).json()
    return response_json["drinks"][0]