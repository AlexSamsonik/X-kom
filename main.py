"""There is main function."""
from api.xkom_client import XKomClient

if __name__ == '__main__':
    x_kom_kod = 540711  # TODO: Create configuration for running.
    x_kom_response = XKomClient().get_request(x_kom_kod)
    print(f"{x_kom_response.producer.name} {x_kom_response.name} - {x_kom_response.price} zł")
