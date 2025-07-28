import requests
from bs4 import BeautifulSoup
def scrape_quotes():
    next_page="/"
    q=[]
    v=set()
    author_details={}

    while next_page and next_page not in v:
        v.add(next_page)
        print(f"Scraping: {url + next_page}")
        respond=requests.get(url+next_page)
        soup=BeautifulSoup(respond.text,"html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            author_link=quote.find("a")["href"]

            if author not in author_details:
                author_page=requests.get(url+author_link)
                author_soup=BeautifulSoup(author_page.text,"html.parser")
                birth_date = author_soup.find("span", class_="author-born-date").text
                birth_place = author_soup.find("span", class_="author-born-location").text
                author_details[author] = {
                    "birth_date": birth_date,
                    "birth_place": birth_place,
                }

                q.append({
                "quote": text,
                "author": author,
                "birth_date": author_details[author]["birth_date"],
                "birth_place": author_details[author]["birth_place"],
            })
                
        next_button=soup.find("li",class_="next")
        next_page=next_button.find("a")["href"] if next_button else None

    return q


import pandas as pd

def save_to_csv(data, filename="data/quotes.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(data)} quotes to {filename}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    quotes = scrape_quotes()
    for q in quotes:
        print(f"{q['quote']} — {q['author']}")
    save_to_csv(quotes)
