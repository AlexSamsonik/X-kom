"""There is main function."""
from argparse import ArgumentParser

from api.xkom_client import XKomClient

if __name__ == '__main__':
    parser = ArgumentParser('Parameters for getting detailed information about item in internet-market x-kom.pl')
    parser.add_argument('-k', '--kod', help='X-Kom kod', required=True)
    args = parser.parse_args()

    x_kom_response = XKomClient().get_request(args.kod)
    print(f"{x_kom_response.producer.name} {x_kom_response.name} - {x_kom_response.price} zł")
