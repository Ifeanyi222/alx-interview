#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (see input format above)
    Number of lines by status code: 
"""
import sys

status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
ct = 0  

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

        
            total_size += file_size

            ct += 1

        if ct == 10:
            ct = 0
            print('File size: {}'.format(total_size))

            for key, value in sorted(status_codes_dict.itms()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.itms()):
        if value != 0:
            print('{}: {}'.format(key, value))
