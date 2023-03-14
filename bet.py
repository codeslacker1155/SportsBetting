# Description: This is a file to find the odds of the current games going on in the NBA, NCAA (Basketball, Football, etc), NFL, NHL, and MLB.

import requests

odds_url = "https://odds.p.rapidapi.com/v4/sports/upcoming/odds"

querystring = {"regions":"us","oddsFormat":"american","markets":"h2h,spreads","dateFormat":"iso"}

headers = {
    "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
    "X-RapidAPI-Host": "odds.p.rapidapi.com"
}

response = requests.request("GET", odds_url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()

    # Extract the first upcoming game
    first_game = data

    # Get the number of games
    num_games = len(data)

    # Extract the home and away teams and their odds
    # home_team = first_game["home_team"]["name"]
    # away_team = first_game["away_team"]["name"]
    # home_odds = first_game["sites"][0]["odds"]["h2h"][0]
    # away_odds = first_game["sites"][0]["odds"]["h2h"][1]

    # Print the home and away teams and their odds
    print("There are " + str(num_games) + " games going on right now.\n")
    odds_0_list = []
    odds_1_list = []
    for i in range(num_games):
        sport_title = data[i]["sport_title"]
        commence_time = data[i]["commence_time"]
        home_team = data[i]["home_team"]
        away_team = data[i]["away_team"]
        for j in range (len(data[i]["bookmakers"])):
            bookmaker = data[i]["bookmakers"][j]["title"]
            last_updated = data[i]["bookmakers"][j]["last_update"]
            outcomes_0 = data[i]["bookmakers"][j]['markets'][0]["outcomes"]
            outcomes_1 = data[i]["bookmakers"][j]['markets'][1]["outcomes"]
            name_0 = data[i]["bookmakers"][j]['markets'][0]["outcomes"][0]['name']
            name_1 = data[i]["bookmakers"][j]['markets'][0]["outcomes"][1]['name']
            odds_0 = data[i]["bookmakers"][j]['markets'][0]["outcomes"][0]['price']
            odds_1 = data[i]["bookmakers"][j]['markets'][0]["outcomes"][1]['price']
            # Add odds_0 to a list and get the average of the list
            odds_0_list.append(odds_0)
            avg_odds_0 = sum(odds_0_list)/len(odds_0_list)

            
            # Add odds_1 to a list and get the average of the list
            odds_1_list.append(odds_1)
            avg_odds_1 = sum(odds_1_list)/len(odds_1_list)
            
    #Print the team names and odds, with the home team first, then the away team with bookmaker name and last updated time

        


else:
    print("Error getting data from API.")
