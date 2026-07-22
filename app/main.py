from fastapi import FastAPI

from core.browser import start_browser
from core.browser import stop_browser

app = FastAPI(title="MAX Autoposter")


@app.on_event("startup")
async def startup():

    await start_browser()


@app.on_event("shutdown")
async def shutdown():

    await stop_browser()


@app.get("/")
async def root():

    return {
        "status": "ok",
        "service": "MAX Autoposter"
    }
