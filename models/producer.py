"""There is Producer object which can get in GET request."""

from typing import Dict

# pylint: disable=R0903


def producer_decoder(json_dict: Dict[str, str]):
    """Producer decoder which return Producer object from Json dict.

    :param json_dict: json dictionary.
    :return: Producer object.
    """
    return Producer(json_dict.get("Id"), json_dict.get("Name"))


class Producer:
    """Producer object."""

    def __init__(self, producer_id: str, name: str):
        """Initialize Producer object using json dictionary.

        :param producer_id: producer id.
        :param name: producer name.
        """
        self.producer_id = producer_id
        self.name = name
