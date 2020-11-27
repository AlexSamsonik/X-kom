"""There is Producer object which can get in GET request."""
from typing import Dict


class Producer:
    """Producer object."""

    def __init__(self, json_dict: Dict[str, str]):
        """Initialize Producer object using json dictionary.

        :param json_dict: json dictionary
        """
        self.producer_id = json_dict.get("Id")
        self.name = json_dict.get("Name")
