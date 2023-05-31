#!/usr/bin/python

import sys

with open(sys.argv[1], 'r') as file:
    line_num = 0;
    for line in file:
        if line_num < 3:
            print(line, end = '')
            line_num = line_num + 1
        else:
            print(line.replace('\n', '%\n'), end = '')
            line_num = 0
