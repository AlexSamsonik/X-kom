"""There is XKomResponse object which contains specify attribute for working."""

from models.producer import producer_decoder

# pylint: disable=R0903


class XKomResponse:
    """Wrapper on response."""

    def __init__(self, response):
        self.json = response.json()
        self.name = self.json.get("Name")
        self.price = self.json.get("Price")
        self.producer = producer_decoder(self.json.get("Producer"))
        self.web_url = self.json.get("WebUrl")
