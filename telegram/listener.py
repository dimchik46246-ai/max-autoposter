from playwright.async_api import TimeoutError


class TelegramListener:

    def __init__(self, browser):

        self.browser = browser

    async def open_channel(self, channel):

        await self.browser.page.goto(channel)

    async def wait_messages(self):

        await self.browser.page.wait_for_selector(
            ".Message",
            timeout=60000
        )

    async def get_last_message(self):

        messages = await self.browser.page.locator(".Message").all()

        return messages[-1]

    async def get_text(self):

        message = await self.get_last_message()

        html = await message.inner_html()

        return html
