#!/usr/bin/python3

""" Python script that reads stdin line by line and computes metrics:
  - Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
  - After every 10 lines and/or a keyboard interruption (CTRL + C),
  print these statistics from the beginning:
    - Total file size: File size for all previous lines
    - Status codes: Status codes from all previous lines in ascending order
"""

import sys


def print_statistics(total_file_size, status_codes):
    """
    Print statistics including total file size and status code counts.
    """
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parse a line and extract file size and status code.
    Return file size and status code if the line matches the expected format,
    otherwise return None.
    """
    parts = line.split()  # split line into components
    # check if parts matches the expected format
    if len(parts) >= 7 and parts[-2].isdigit() and parts[-1].isdigit():
        return int(parts[-1]), parts[-2]
    return None, None


def main():
    """ Read stdin line by line and compute metrics.
    """
    # initialize variables to store metrics
    total_file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        # loop over each line in stdin
        for line in sys.stdin:
            # increment line count to track when to print statistics
            line_count += 1
            file_size, code = parse_line(line)

            if file_size is not None and code in status_codes:
                total_file_size += file_size
                status_codes[code] += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_statistics(total_file_size, status_codes)
        sys.exit(0)

    finally:
        # Ensure statistics are printed at the end of input
        print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    main()
