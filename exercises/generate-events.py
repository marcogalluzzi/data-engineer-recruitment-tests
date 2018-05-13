#!/usr/bin/env python3
import argparse
import uuid
import datetime
import time
import os


# Timestamp formats
TMST_FORMAT_FILE = '%Y-%m-%d-%H-%M-%S-%f'
TMST_FORMAT_EVENT = '%Y-%m-%dT%H:%M:%SZ'

# Order types
ORDER_TYPE_PLACED = 'OrderPlaced'
ORDER_TYPE_ACCEPTED = 'OrderAccepted'
ORDER_TYPE_CANCELLED = 'OrderCancelled'


def ceil_and_remainder(num, den):
    """Compute the ceiling of num/den and the remainder of the integer division"""
    remainder = num % den
    ceil = num // den
    if remainder > 0:
        ceil += 1
    return ceil, remainder


def get_unique_id():
    """Generate a unique ID from a random UUID"""
    return str(uuid.uuid4())


def get_timestamp(string_format):
    """Return the current UTC time as string with a specific format"""
    return datetime.datetime.utcnow().strftime(string_format)


def generate_event(order_type, order_id, timestamp):
    """Create a business event as a JSON string"""
    return f'{{ "Type": "{order_type}", "Data": {{ "OrderId": "{order_id}", "TimestampUtc": "{timestamp}" }} }}'


def parse_arguments():
    """Parse script input arguments"""
    parser = argparse.ArgumentParser(description='Core Business Events Generator')

    parser.add_argument('--output-directory', type=str, required=True,
                        help='output directory for all created files')

    parser.add_argument('--number-of-orders', type=int, default=100,
                        help='number of orders to generate (default: %(default)s)')

    parser.add_argument('--batch-size', type=int, default=10,
                        help='batch size of events per file (default: %(default)s)')

    parser.add_argument('--interval', type=int, default=1,
                        help='interval in seconds between each file being created (default: %(default)s)')

    return parser.parse_args()


def main():
    args = parse_arguments()

    number_of_files, remaining_orders = ceil_and_remainder(args.number_of_orders, args.batch_size)
    order_no = 0

    for file_no in range(number_of_files):
        file_name = 'orders-' + get_timestamp(TMST_FORMAT_FILE) + '.json'
        directory = args.output_directory.rstrip('/') + '/'
        temporary_file_path = directory + "temp_" + file_name

        with open(temporary_file_path, 'wt', encoding='utf_8', newline='\n') as file:

            last_file_with_few_orders = (file_no == number_of_files-1 and remaining_orders > 0)
            number_of_orders = remaining_orders if last_file_with_few_orders else args.batch_size

            for i in range(number_of_orders):
                order_id = get_unique_id()
                timestamp = get_timestamp(TMST_FORMAT_EVENT)

                second_event_type = ORDER_TYPE_CANCELLED if order_no % 5 == 4 else ORDER_TYPE_ACCEPTED

                first_event = generate_event(ORDER_TYPE_PLACED, order_id, timestamp)
                second_event = generate_event(second_event_type, order_id, timestamp)

                file.write(first_event+'\n'+second_event+'\n')
                order_no += 1

        os.rename(temporary_file_path, directory + file_name)
        time.sleep(1)


if __name__ == '__main__':
    main()
