import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_lebron_quotes():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.brainyquote.com/authors/lebron-james-quotes")

    quotes = {}
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "b-qt")))
    
    quote_elements = driver.find_elements(By.CLASS_NAME, "b-qt")
    for idx, quote in enumerate(quote_elements, 1):
        quotes[idx] = quote.text.strip()
    
    driver.quit()
    
    return quotes

def save_quotes_to_json(quotes, filename="quotes.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

def print_quotes(quotes):
    for idx, quote in quotes.items():
        print(f"{idx}: {quote}")

if __name__ == "__main__":
    lebron_quotes = fetch_lebron_quotes()
    save_quotes_to_json(lebron_quotes)
    print_quotes(lebron_quotes)