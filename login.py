import asyncio

from telegram.login import TelegramBrowser


async def main():
    browser = TelegramBrowser()

    await browser.start()
    await browser.open()
    await browser.wait_login()

    print("Авторизация сохранена.")
    print("Теперь можешь закрыть браузер.")

    input("Нажми Enter...")

    await browser.stop()


if __name__ == "__main__":
    asyncio.run(main())
