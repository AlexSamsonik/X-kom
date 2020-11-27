"""There is main function."""
from api.xkom_client import XKomClient

if __name__ == '__main__':
    x_kom_kod = 540711  # TODO: Create configuration for running.
    response = XKomClient().get_request(x_kom_kod)
    print(f"{response.producer.name} {response.name} - {response.price} zł")
