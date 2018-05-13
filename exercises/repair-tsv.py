#!/usr/bin/env python3
import argparse

# Constants
CHAR_SEPARATOR = '\t'
CHAR_NEWLINE = '\n'
CHAR_QUOTES = '\''
SPECIAL_CHARACTERS = ('\n', '\r')
ENCODING_OUTPUT = 'utf_8'


def parse_arguments():
    """Parse script input arguments"""
    parser = argparse.ArgumentParser(description='Repair a TSV file')

    parser.add_argument('--input-filename', type=str, required=True,
                        help='input TSV file to repair')

    parser.add_argument('--output-filename', type=str, required=True,
                        help='output file where to write the repaired TSV file')

    parser.add_argument('--input-encoding', type=str, default=None,
                        help='encoding of input file, e.g. "utf_16_le", or None to use platform default encoding '
                             '(default: %(default)s)')

    parser.add_argument('--num-columns', type=str, default=None,
                        help='number of columns or None to autodetect it by reading first line (default: %(default)s)')

    parser.add_argument('--buffer-size', type=int, default=512,
                        help='size of read buffer (default: %(default)s)')

    return parser.parse_args()


def autodetect_num_columns(input_filename, input_encoding):
    """Detect how many columns has a TSV file by reading the first line"""
    with open(input_filename, 'rt', encoding=input_encoding, newline='') as input_file:
        num_columns = len(input_file.readline().split(CHAR_SEPARATOR))
    return num_columns


def main():
    args = parse_arguments()

    if args.num_columns is None:
        num_columns = autodetect_num_columns(args.input_filename, args.input_encoding)
    else:
        num_columns = args.num_columns

    with open(args.output_filename, 'wt', encoding=ENCODING_OUTPUT, newline='') as output_file:
        with open(args.input_filename, 'rt', encoding=args.input_encoding, newline='') as input_file:
            quoting = False
            col_no = 0
            field = ''

            input_buffer = input_file.read(args.buffer_size)
            while input_buffer != '':
                output_buffer = ''

                for char in input_buffer:

                    if (char == CHAR_SEPARATOR) or (char == CHAR_NEWLINE and col_no == num_columns-1):
                        if quoting:
                            field += CHAR_QUOTES
                            quoting = False
                        output_buffer += field + char
                        field = ''
                        col_no = (col_no + 1) % num_columns

                    elif char in SPECIAL_CHARACTERS and not quoting:
                        field = CHAR_QUOTES + field + char
                        quoting = True

                    else:
                        field += char

                output_file.write(output_buffer)
                input_buffer = input_file.read(args.buffer_size)

        output_file.write(field)


if __name__ == '__main__':
    main()
