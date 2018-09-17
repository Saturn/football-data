## Python API for football-data.org

Basic API wrapper for [football-data.org](https://www.football-data.org/).

Currently it does not support everything. You can view the full API reference [here](https://www.football-data.org/documentation/api).


##### Auth Token

Auth tokens can be obtained from [here](https://www.football-data.org/client/register).


You can use the `auth_token` parameter or save your auth token in `config.json`.


```python
fd = FootballData()  # Auth token saved in config.json

fd = FootballData(auth_token='YOUR_AUTH_TOKEN_HERE')
```

##### Competitions

```python
standings = fd.get_competition_standings(id="PL")

print("Pos\tTeam")
for team in standings[0:10]:
    print("{}\t{}".format(team['position'], team['team']['name']))

```

```
Pos     Team
1       Chelsea FC
2       Liverpool FC
3       Manchester City FC
4       Watford FC
5       AFC Bournemouth
6       Tottenham Hotspur FC
7       Arsenal FC
8       Manchester United FC
9       Wolverhampton Wanderers FC
10      Leicester City FC
```

##### Matches

```python

matches = fd.get_competition_matches("PL", status="FINISHED")

# Print most recent 10 results in PL (English Premier League)
for match in matches[-10:]:
    home_team = match['homeTeam']['name']
    away_team = match['awayTeam']['name']
    home_goals = match['score']['fullTime']['homeTeam']
    away_goals = match['score']['fullTime']['awayTeam']
    print("{} {}-{} {}".format(home_team,
                               home_goals,
                               away_goals,
                               away_team))
```
```
Watford FC 2-1 Tottenham Hotspur FC
Tottenham Hotspur FC 1-2 Liverpool FC
Manchester City FC 3-0 Fulham FC
Newcastle United FC 1-2 Arsenal FC
Chelsea FC 4-1 Cardiff City FC
Huddersfield Town AFC 0-1 Crystal Palace FC
AFC Bournemouth 4-2 Leicester City FC
Watford FC 1-2 Manchester United FC
Wolverhampton Wanderers FC 1-0 Burnley FC
Everton FC 1-3 West Ham United FC
```