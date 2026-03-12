from playwright.sync_api import sync_playwright

def browse_web(query):

    print("Web Agent is searching the internet...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"https://www.google.com/search?q={query}"
        page.goto(search_url)

        results = page.inner_text("body")

        browser.close()

    return results[:2000]
