#!/usr/bin/python3
"""
This script reads stdin line by line &
computes metrics
"""
import sys


status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        listofline = line.split(" ")
        if len(listofline) > 4:
            code = listofline[-2]
            size = int(listofline[-1])
            if code in status_counts.keys():
                status_counts[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print(f'File size: {total_size}')
            for key, value in sorted(status_counts.items()):
                if value != 0:
                    print(f'{key}: {value}')

except Exception as err:
    pass

finally:
    print(f'File size: {total_size}')
    for key, value in sorted(status_counts.items()):
        if value != 0:
            print(f'{key}: {value}')
