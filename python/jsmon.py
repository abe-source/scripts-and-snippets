# Downloads js files from given website for further inspection
# Logs everything to output.txt

from playwright.sync_api import Playwright, sync_playwright
import requests
import tldextract
from datetime import date
import os

website_url = "https://www.target.com/"
domain = tldextract.extract(website_url).domain
current_date = date.today().strftime("%Y-%m-%d")

def log_output(text):
    with open("output.txt", "a") as f:
        print(f"====== Date: {current_date} Target: {domain}======", file=f)
        print(text, file=f)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(website_url)
    if not os.path.exists(f"{domain}"):
        os.makedirs(f"{domain}/screenshots/")
        os.makedirs(f"{domain}/jsfiles/")
    page.wait_for_timeout(5000)
    page.screenshot(path=f"{domain}/screenshots/{domain}-{current_date}.png")
    js_files = page.query_selector_all("script[src]")
    for js_file in js_files:
        js_url = js_file.get_attribute("src")
        response = requests.get(js_url)
        file_name = os.path.basename(js_url)
        if(os.path.isfile(f"{domain}/jsfiles/{file_name}")):
            log_output(f"File: {file_name} already exists!")
        else:
            with open(os.path.join(f"{domain}/jsfiles",file_name), "wb") as f:
                f.write(response.content)
                log_output(f"New file: {file_name} has been added!")       
    browser.close()
