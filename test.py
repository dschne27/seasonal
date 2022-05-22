from bs4 import BeautifulSoup
import requests
from datetime import datetime


def load_products():

    def get_season():

        current_month = datetime.now().month
        if current_month >= 1 and current_month <= 3:
            return "winter"
        elif current_month >= 4 and current_month < 6:
            return "spring" 
        elif current_month >= 6 and current_month < 9:
            return "summer"
        else:
            return "fall"
            

    seasonal_data = requests.get("https://snaped.fns.usda.gov/seasonal-produce-guide")
    soup = BeautifulSoup(seasonal_data.content, "html.parser")
    print(soup.prettify())

    veg_list = []

    month = get_season()

    content = soup.find("div", class_=month)
    ul = content.find("ul")
    li = ul.find_all("li")

    for veg in li:
        veg_list.append(veg.text)

        

    return veg_list
    
products = load_products()
