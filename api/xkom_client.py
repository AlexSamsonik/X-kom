"""There is XKomClient for working by HTTP."""

from faker import Faker
from requests import Session

from api.xkom_response import XKomResponse
from constants.constant import get_constants

# pylint: disable=R0903


class XKomClient:
    """XKomClient for working by HTTP."""

    CONSTANTS = get_constants()  # Get Constant object

    def get_request(self, x_kom_code: int) -> XKomResponse:
        """GET request via HTTP use unique kod x-kom e.g. 540711.

        :param x_kom_code: kod x-kom for item in internet market.
        """

        url = f"{self.CONSTANTS.url}/{x_kom_code}"
        headers = {
            "x-api-key": self.CONSTANTS.x_api_key,
            "user-agent": Faker().random_element(self.CONSTANTS.user_agents),
        }

        return XKomResponse(Session().get(url=url, headers=headers, timeout=4))
