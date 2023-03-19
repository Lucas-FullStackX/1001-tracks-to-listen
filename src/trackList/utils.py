import requests
from bs4 import BeautifulSoup
from src.constant import USER_AGENT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# URL = "https://www.1001tracklists.com/charts/year/2022/index.html"


def get_tracks(url: str):
    # set Header
    headers = {
        "User-Agent": USER_AGENT
    }
    tracks_list = []
    _next = True
    i = 1
    while _next:
        print(i)
        page = requests.get(
            f'{url}/index{i}.html', headers=headers)
    # convert to HTML
        soup = BeautifulSoup(page.content, "html.parser")
    # find div container
        results = soup.find(id="middle")

    # get all titles
        tracks_elements = results.find_all("div", class_="fontL")
        print(len(tracks_elements))
        print(tracks_list)
        if (len(tracks_elements) == 0):
            _next = False
            break
    # get only name list
        for track in tracks_elements:
            track_name = track.find("a")
            tracks_list.append(track_name.text)
        i += 1
    return tracks_list
