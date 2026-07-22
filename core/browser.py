from playwright.async_api import async_playwright

playwright = None
browser = None


async def start_browser():

    global playwright
    global browser

    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch(
        headless=False
    )


async def stop_browser():

    global browser
    global playwright

    if browser:
        await browser.close()

    if playwright:
        await playwright.stop()
