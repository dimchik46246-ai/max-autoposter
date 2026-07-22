from bs4 import BeautifulSoup


class TelegramParser:

    @staticmethod
    def clean(html: str):

        soup = BeautifulSoup(html, "lxml")

        return soup.get_text("\n", strip=True)
