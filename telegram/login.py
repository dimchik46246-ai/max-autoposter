from pathlib import Path

from playwright.async_api import async_playwright


class TelegramBrowser:

    def __init__(self):

        self.playwright = None
        self.context = None
        self.page = None

    async def start(self):

        profile = Path("profiles/telegram")

        profile.mkdir(parents=True, exist_ok=True)

        self.playwright = await async_playwright().start()

        self.context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(profile),
            headless=True,
            viewport={"width":1500,"height":900},
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()

    async def open(self):

        await self.page.goto("https://web.telegram.org/k/")

    async def wait_login(self):

        print("\n==============================")
        print("Если Telegram не авторизован —")
        print("отсканируй QR код.")
        print("==============================\n")

        while True:

            url = self.page.url

            if "/k/" in url:
                break

            await self.page.wait_for_timeout(1000)

        print("Telegram авторизован.")

    async def stop(self):

        await self.context.close()

        await self.playwright.stop()
