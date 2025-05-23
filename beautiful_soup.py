import requests, json, time
from bs4 import BeautifulSoup

BASE = "http://quotes.toscrape.com"
url = BASE
all_quotes = []

while url:
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    for quote_block in soup.select(".quote"):
        text = quote_block.select_one(".text").get_text(strip=True)
        author = quote_block.select_one(".author").get_text(strip=True)
        all_quotes.append({"quote": text, "author": author})

    next_link = soup.select_one("li.next > a")
    url = BASE + next_link["href"] if next_link else None
    time.sleep(1)                     # polite pause

with open("bs_quotes.json", "w") as f:
    json.dump(all_quotes, f, indent=2)

print(f"Saved {len(all_quotes)} quotes.")