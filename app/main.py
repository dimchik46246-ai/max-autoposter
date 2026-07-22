from fastapi import FastAPI

from telegram.login import TelegramBrowser
from telegram.listener import TelegramListener
from telegram.parser import TelegramParser

app = FastAPI()

browser = TelegramBrowser()


@app.on_event("startup")
async def startup():

    await browser.start()

    await browser.open()

    await browser.wait_login()


@app.on_event("shutdown")
async def shutdown():

    await browser.stop()


@app.get("/last")
async def last():

    listener = TelegramListener(browser)

    await listener.open_channel(
        "https://t.me/CompPoint"
    )

    await listener.wait_messages()

    html = await listener.get_text()

    text = TelegramParser.clean(html)

    return {
        "text": text
    }
