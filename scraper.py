import requests
from bs4 import BeautifulSoup
import json

def fetch_and_save_ipo():
    url = "https://cdsc.com.np/ipolist"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("Fetching data from CDSC...")
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table')
        if not table:
            print("Error: Could not find the IPO table on the page.")
            return

        # Extract headers
        table_head = table.find('thead')
        headers_list = [th.get_text(strip=True) for th in table_head.find_all('th')]

        # Extract rows
        ipo_list = []
        for row in table.find('tbody').find_all('tr'):
            cols = [td.get_text(strip=True) for td in row.find_all('td')]
            if len(cols) == len(headers_list):
                ipo = dict(zip(headers_list, cols))
                ipo_list.append(ipo)

        # Save to local JSON file
        with open('ipo_data.json', 'w') as f:
            json.dump(ipo_list, f, indent=4)
        
        print(f"Successfully saved {len(ipo_list)} items to ipo_data.json")

    except Exception as e:
        print(f"Scraping failed: {e}")

if __name__ == "__main__":
    fetch_and_save_ipo()
