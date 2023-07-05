import requests

API_KEY = 'your_api_key'
BASE_URL = 'https://api.opendota.com/api/'

def get_player_data(player_id):
    url = f'{BASE_URL}players/{player_id}'
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_match_history(player_id):
    url = f'{BASE_URL}players/{player_id}/matches'
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def analyze_player_performance(player_id):
    player_data = get_player_data(player_id)
    if player_data:
        player_name = player_data['profile']['personaname']
        mmr = player_data['mmr_estimate']['estimate']
        print(f"Player: {player_name}")
        print(f"MMR Estimate: {mmr}")
        print("Match History:")
        match_history = get_match_history(player_id)
        if match_history:
            for match in match_history:
                match_id = match['match_id']
                hero_id = match['hero_id']
                duration = match['duration']
                result = match['radiant_win'] if match['player_slot'] < 128 else not match['radiant_win']
                print(f"Match ID: {match_id}, Hero ID: {hero_id}, Duration: {duration}, Result: {'Win' if result else 'Loss'}")
        else:
            print("Failed to retrieve match history.")
    else:
        print("Failed to retrieve player data.")

# Usage example
player_id = '123456789'  # Replace with the desired player's ID
analyze_player_performance(player_id)
