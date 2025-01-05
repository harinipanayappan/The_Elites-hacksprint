import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebsiteScraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            card_elements = soup.find_all('li', class_='event-card event-card-link')  

            for card in card_elements:
                
                title = card.find('h3', class_='').text.strip()
                location = card.find('div', class_='subtitle').text.strip()
                date = card.find('div',class_='date').text.strip()

                self.data.append({'Title': title, 'Location': location,'Date':date})

    def save_to_csv(self, filename='events.csv'):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')

    def print_data(self):
        for item in self.data:
            print(item)

scraper = WebsiteScraper('https://allevents.in/coimbatore/all?ref=cityhome-popmenu')
scraper.scrape()
scraper.save_to_csv()