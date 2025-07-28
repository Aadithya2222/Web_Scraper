import requests
from bs4 import BeautifulSoup
import json

# Function to get the URL and container selector from the user
def get_user_input():
    url = input("Enter the URL to scrape: ")
    container_selector = input("Enter the main container selector (e.g., .quote): ")
    print("Enter the fields you want to extract in the format: field_name:css_selector")
    print("Type 'done' when you are finished.")
    
    fields = {}
    while True:
        field = input("Field: ")
        if field.lower() == "done":
            break
        try:
            field_name, selector = field.split(":")
            fields[field_name.strip()] = selector.strip()
        except ValueError:
            print("Invalid format. Use field_name:css_selector")
    
    return url, container_selector, fields

# Function to scrape the content from the provided URL
def scrape_dynamic(url, container_selector, fields):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the main container for the content
    container = soup.select_one(container_selector)
    if not container:
        print(f"Could not find the container with selector: {container_selector}")
        return []
    
    # Extract content based on user-defined fields
    scraped_data = []
    for item in container.find_all("a"):  # Modify this to target the correct elements
        item_data = {}
        for field_name, selector in fields.items():
            element = item.select_one(selector)
            if element:
                item_data[field_name] = element.get_text(strip=True)
            else:
                item_data[field_name] = "Not Found"
        scraped_data.append(item_data)
    
    return scraped_data

# Function to save data to a JSON file
def save_to_json(data, filename="scraped_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

# Main program
if __name__ == "__main__":
    # Get user inputs
    url, container_selector, fields = get_user_input()
    
    # Scrape the data
    scraped_data = scrape_dynamic(url, container_selector, fields)
    
    # Print the scraped data (optional)
    for item in scraped_data:
        print(item)
    
    # Save the scraped data to a file
    save_to_json(scraped_data)
