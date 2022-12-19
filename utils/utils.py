import json
from bs4 import BeautifulSoup
from requests import get

def get_flights_div_list():
    with open('/home/thebvrtosz/repos/flight-price-notifier/properties.json', 'r') as f:
        requirements = json.loads(f.read())
    
    poznan_url = requirements['azAir-poznan-url']
    url_content = get(poznan_url).content
    url_soup = BeautifulSoup(url_content, 'html.parser')
    flights_search_result_div = url_soup.find("div", class_="list")
    flights_divs_list = flights_search_result_div.find_all("div", class_="result")
    return flights_divs_list
