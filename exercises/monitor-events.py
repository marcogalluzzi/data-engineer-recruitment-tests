#!/usr/bin/env python3
import argparse
import time
import glob
import sys


def parse_arguments():
    """Parse script input arguments"""
    parser = argparse.ArgumentParser(description='Event Files Monitoring')

    parser.add_argument('--directory', type=str, required=True,
                        help='directory to monitor for event files')

    parser.add_argument('--interval', type=int, default=5,
                        help='interval in seconds between each directory check for new files (default: %(default)s)')

    return parser.parse_args()


def main():
    args = parse_arguments()

    order_type_list = ['OrderCancelled', 'OrderAccepted', 'OrderPlaced']
    order_type_count = {x: 0 for x in order_type_list}
    last_filename = ''

    while True:
        for filename in sorted(glob.glob(args.directory.rstrip('/') + '/orders*.json')):
            if filename > last_filename:
                last_filename = filename

                with open(file=filename, mode='rt') as file:
                    for line in file:
                        for order_type in order_type_count:
                            if line.find(order_type) > -1:
                                order_type_count[order_type] += 1
                                break

        for order_type in order_type_list:
            print(f'"{order_type}": {order_type_count[order_type]}')

        time.sleep(args.interval)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminated by the user!')
        sys.exit(0)
