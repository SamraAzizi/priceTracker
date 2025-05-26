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

async def search(metadata, page, search_text):
    print(f"Searching for {search_text} on {page.url}")
    search_field_query = metadata.get("search_field_query")
    search_button_query = metadata.get("search_button_query")

    if search_field_query and search_button_query:
        print("Filling input field")
        search_box = await page.wait_for_selector(search_field_query)
        await search_box.type(search_text)
        print("Pressing search button")
        button = await page.wait_for_selector(search_button_query)

        await button.click()
    else:
        raise Exception("Could not search.")

    await page.wait_for_load_state()
    return page


async def get_products(page, search_text, selector, get_product):