import asyncio
from playwright.async_api import async_playwright
import json
import os
from amazon import get_product as get_amazon_product
from requests import post

AMAZON = "https://amazon.ca"

URLS = {
    AMAZON: {
        "search_field_query": 'input[name="field-keywords"]',
        "search_button_query": 'input[value="Go"]',
        "product_selector": "div.s-card-container"
    }
}

available_urls = URLS.keys()

def load_auth():
    FILE = os.path.join("Scraper", "auth.json")
    with open(FILE, "r") as f:
        return json.load(f)

# place your bright data credentials in auth.json file with keys: "username", "password" and "host"
cred = load_auth()
auth = f'{cred["username"]}:{cred["password"]}'
browser_url = f'wss://{auth}@{cred["host"]}'