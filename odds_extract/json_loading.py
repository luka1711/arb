import requests
from urllib.parse import quote
from datetime import datetime


def load_json_get(query_link, payload):
    try:
        response = requests.get(query_link, json=payload)
        response.raise_for_status()
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data


def load_json_url(query_link, query_params):
    response = requests.get(query_link, params=query_params)

    if response.status_code == 200:
        json_data = response.json()
    else:
        print("Error:", response.status_code)

    return json_data


def load_json_post(query_link, payload):
    try:
        response = requests.post(query_link, json=payload)
        response.raise_for_status()
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data

def load_leagues_list_maxbet(query_link):
    try:
        response = requests.get(query_link)
        response.raise_for_status()
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data

def load_matches_list_maxbet(query_link):
    try:
        response = requests.get(query_link)
        response.raise_for_status()
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data


def load_odds_maxbet(query_link):
    try:
        response = requests.get(query_link)
        response.raise_for_status()
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data

def loadPlayerName(name):
    encoded_name = quote(name)

    url = f"https://s.livesport.services/api/v2/search/?q={encoded_name}&lang-id=14&type-ids=1,2,3,4&project-id=14&project-type-id=1&sport-ids=2"
    try:
        response = requests.get(url)
        json_data = response.json()
        name = json_data[0]['name']
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    #name = json_data[0]['name']
    return name


def loadPlayerNameBasedOnMatch(name):
    encoded_name = quote(name)

    url = f'https://www.sofascore.com/api/v1/search/events?q={name}&page=0'
    try:
        response = requests.get(url)
        json_data = response.json()
        home_name = json_data['results'][0]['entity']['homeTeam']['name']
        away_name = json_data['results'][0]['entity']['awayTeam']['name']
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    # name = json_data[0]['name']
    return home_name + '-' + away_name


def loadOddsFromSofaScore(name):
    encoded_name = quote(name)

    url = f'https://www.sofascore.com/api/v1/search/events?q={name}&page=0'
    try:
        response = requests.get(url)
        json_data = response.json()
        id = json_data['results'][0]['entity']['id']
        url_odds = f'https://www.sofascore.com/api/v1/event/{id}/odds/226/all'
        try:
            response_odds = requests.get(url_odds).json()
            ki1 = response_odds['markets'][0]['choices'][0]['fractionalValue']
            ki2 = response_odds['markets'][0]['choices'][1]['fractionalValue']
            first_set1 = response_odds['markets'][1]['choices'][0]['fractionalValue']
            first_set2 = response_odds['markets'][1]['choices'][1]['fractionalValue']
        except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
            print(f"Error: {e}")
            return None
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    # name = json_data[0]['name']
    return ki1, ki2, first_set1, first_set2


def get_tournaments_suberbet(url):
    try:
        response = requests.get(url)
        json_data = response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data


def get_matches_suberbet(tournament_id):

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    url = "https://production-superbet-offer-rs.freetls.fastly.net/sb-rs/api/v2/sr-Latn-RS/events/by-date"
    params = {
    "currentStatus": "active",
    "tournamentIds": tournament_id,
    "startDate": formatted_date
    }
    # Send a GET request to the API
    try:
        json_data = requests.get(url, params=params).json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data


def get_odds_suberbet(match_id):
    url = f'https://production-superbet-offer-rs.freetls.fastly.net/sb-rs/api/v2/sr-Latn-RS/events/{match_id}?matchIds={match_id}'
    try:
        json_data = requests.get(url).json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None

    return json_data