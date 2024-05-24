import requests
from bs4 import BeautifulSoup

# Soccer website to retrieve Champion League Stats from
soccer_url = 'https://fbref.com/en/comps/8/Champions-League-Stats'

# Recieved 200 response - success!
data = requests.get(soccer_url)

soup = BeautifulSoup(data.text)

# Found the table that had all the data, now we need to get all the anchors that harbors every team in the UCL stats.
standings_table = soup.find('table', id='results2023-202480_overall').find_all('a')[:]

# href has the team's url
links = [l.get("href") for l in standings_table]

# We only want the links that include squads, not the referee or any other anchor that exists in the table.
links = [l for l in links if '/squads' in l] 

# The links only included the unique identifier of the url so we need to pass the whole url, given they all start with the same string.
team_urls = [f"https://fbref.com{l}" for l in links]



