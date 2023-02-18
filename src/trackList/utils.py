import requests
from bs4 import BeautifulSoup


def get_tracks():
    tracks_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    URL = "https://www.1001tracklists.com/charts/year/2022/index.html"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="middle")
    tracks_elements = results.find_all("div", class_="fontL")
    print(results.prettify())
    print(tracks_elements)
    for track in tracks_elements:
        track_name = track.find("a")
        tracks_list.append(track_name.text)
    print("TEST")
    return tracks_list
