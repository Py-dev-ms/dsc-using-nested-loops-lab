soccer_match = [
    {"home_team": True,
     "away_team": False,
     "country": "France",
     "num_passes": 484,
     "passes_completed": 423,
     "fouls_committed": 16,
     "colors": ["blue", "white", "red"],
     "players": [
         {
             "name": "Hugo LLORIS",
             "captain": True,
             "shirt_number": 1,
             "position": "Goalie"
         },
         {
             "name": "Benjamin PAVARD",
             "captain": False,
             "shirt_number": 2,
             "position": "Defender"
         },
         {
             "name": "Raphael VARANE",
             "captain": False,
             "shirt_number": 4,
             "position": "Defender"
         },
         {
             "name": "Samuel UMTITI",
             "captain": False,
             "shirt_number": 5,
             "position": "Defender"
         },
         {
             "name": "Paul POGBA",
             "captain": False,
             "shirt_number": 6,
             "position": "Midfield"
         },
         {
             "name": "Antoine GRIEZMANN",
             "captain": False,
             "shirt_number": 7,
             "position": "Forward"
         },
         {
             "name": "Kylian MBAPPE",
             "captain": False,
             "shirt_number": 10,
             "position": "Forward"
         },
         {
             "name": "Ousmane DEMBELE",
             "captain": False,
             "shirt_number": 11,
             "position": "Forward"
         },
         {
             "name": "Corentin TOLISSO",
             "captain": False,
             "shirt_number": 12,
             "position": "Midfield"
         },
         {
             "name": "Ngolo KANTE",
             "captain": False,
             "shirt_number": 13,
             "position": "Midfield"
         },
         {
             "name": "Lucas HERNANDEZ",
             "captain": False,
             "shirt_number": 21,
             "position": "Defender"
         }
     ],
     },
    {"home_team": False,
        "away_team": True,
        "country": "Australia",
        "num_passes": 390,
        "passes_completed": 332,
        "fouls_committed": 19,
        "colors": ["green", "gold"],
        "players": [
            {
                "name": "Mathew RYAN",
                "captain": False,
                "shirt_number": 1,
                "position": "Goalie"
            },
            {
                "name": "Mark MILLIGAN",
                "captain": False,
                "shirt_number": 5,
                "position": "Defender"
            },
            {
                "name": "Mathew LECKIE",
                "captain": False,
                "shirt_number": 7,
                "position": "Forward"
            },
            {
                "name": "Robbie KRUSE",
                "captain": False,
                "shirt_number": 10,
                "position": "Forward"
            },
            {
                "name": "Andrew NABBOUT",
                "captain": False,
                "shirt_number": 11,
                "position": "Forward"
            },
            {
                "name": "Aaron MOOY",
                "captain": False,
                "shirt_number": 13,
                "position": "Midfield"
            },
            {
                "name": "Mile JEDINAK",
                "captain": True,
                "shirt_number": 15,
                "position": "Midfield"
            },
            {
                "name": "Aziz BEHICH",
                "captain": False,
                "shirt_number": 16,
                "position": "Defender"
            },
            {
                "name": "Joshua RISDON",
                "captain": False,
                "shirt_number": 19,
                "position": "Defender"
            },
            {
                "name": "Trent SAINSBURY",
                "captain": False,
                "shirt_number": 20,
                "position": "Defender"
            },
            {
                "name": "Tom ROGIC",
                "captain": False,
                "shirt_number": 23,
                "position": "Midfield"
            }
        ]
     }
]


# print("Information about soccer_match")
# print("Type:", type(soccer_match))
# print("Length:", len(soccer_match))
# print()

# print("Information about soccer_match[0]:")
# print("Type:", type(soccer_match[0]))
# print("Length:", len(soccer_match[0]))
# print("Keys:", soccer_match[0].keys())
# print("Values:", soccer_match[1].values())

countries = []

for match in soccer_match:
    countries.append(match['country'])

# print(countries)

colors = []

for match in soccer_match:
    for color in match['colors']:
        colors.append(color)

# print(colors)

players = []

for match in soccer_match:
    for player in match['players']:
        players.append(player)

# print(players)

captains = []


## Captains: Another List of Dictionaries!
# Iterate over the `soccer_match` list to create a new list with the captains from each team.

# This should be a single list containing the dictionaries for each of the countries' captains.
    
for match in soccer_match:
    for player in match['players']:
        if player['captain'] == True:
            captains.append(player)

# print(captains)


## Home Team Players: A Third List of Dictionaries
# Iterate over the `soccer_match` list to create a new list with the players from ONLY the home team.

# Do not "hard-code" which team this is; use the `'home_team'` key.

home_team_players = []

for match in soccer_match:
    if match['home_team'] == True:
        for player in match["players"]:
            home_team_players.append(player)

# print(home_team_players)

## Away Team Forwards: Yup, a List of Dictionaries
# Iterate over the `soccer_match` list to create a new list with the information for each of the away team players whose `position` is `"Forward"`.

away_team_forwards = []

for match in soccer_match:
    for player in match['players']:
        if player['position'] == "Forward":
            away_team_forwards.append(player)

# print(away_team_forwards)

## Player with the Highest Number
# Iterate over the `soccer_match` list and find the player with the highest `shirt_number`.  
# Store this player's information in the `player_with_highest_num` variable.

player_with_highest_num = None
highest_no = 0
for match in soccer_match:
    for player in match['players']:
        if player['shirt_number'] > highest_no:
            highest_no = player['shirt_number']
            player_with_highest_num = player

# print(player_with_highest_num)

# alternative
# player_with_highest_num = None
# shirt_numbers = []

# for soccer in soccer_match:
#     for player in soccer['players']:
#         shirt_numbers.append(player['shirt_number'])
#         if player['shirt_number'] == max(shirt_numbers):
#             player_with_highest_num = player

# print(player_with_highest_num)

player_names = []

for match in soccer_match:
    for player in match["players"]:
        player_names.append(player['name'].title())

print(player_names)