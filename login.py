from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto("http://172.16.148.1:1000", wait_until="domcontentloaded")

    page.wait_for_selector("#ft_un", timeout=30000)

    page.fill("#ft_un", USERNAME)
    page.fill("#ft_pd", PASSWORD)

    page.click("button.primary")

    page.wait_for_timeout(3000)

    browser.close()