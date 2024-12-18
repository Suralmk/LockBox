import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--photoshop_password', default='123456')
parser.add_argument('--basnet_service_ip', required=True, help="The BASNet service IP address")
parser.add_argument('--basnet_service_host', help="Optional, the BASNet service host")
args = parser.parse_args()

print(f"Hello, {args.naphotoshop_passwordme}! You are {args.basnet_service_ip} years old.")
