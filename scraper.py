import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_to_file():
    url = "https://cdsc.com.np/ipolist"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        headers_list = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

        ipo_list = []
        # Current time in Nepal format (approximate)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for row in table.find('tbody').find_all('tr'):
            cols = [td.get_text(strip=True) for td in row.find_all('td')]
            ipo = dict(zip(headers_list, cols))
            ipo["Last Update"] = now # Match your original API's field
            ipo_list.append(ipo)

        with open('ipo_data.json', 'w') as f:
            json.dump(ipo_list, f, indent=4)
        print("Update Successful!")

    except Exception as e:
        print(f"Scrape failed: {e}")

if __name__ == "__main__":
    scrape_to_file()
