"""There is Constant module. Use it you can load constant file and get object."""

from yaml import load, YAMLObject, FullLoader


class Constant(YAMLObject):
    """Provide object from constant file."""
    yaml_tag = u'!Constant'

    def __init__(self, url, x_api_key, user_agents):
        self.url = url
        self.x_api_key = x_api_key
        self.user_agents = user_agents


def get_constants() -> Constant:
    """Provide instance of Constant class."""
    with open("constants/constant.yaml") as file:
        return load(file, Loader=FullLoader)
