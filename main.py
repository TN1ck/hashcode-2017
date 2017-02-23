#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Hash Code 2016 - Qualification
#
# © 2017 Team "TU_DUDES"
#
# Version: 0.1
#

"""Google Hash Code 2017"""

import sys
import numpy as np

class Pizza(object):
    """A pizza about to be sliced"""

    def __init__(self, rows, cols, min_num_ingridients, max_slice_size):
        self.rows = rows
        self.cols = cols
        self.min_num_ingridients = min_num_ingridients
        self.max_slice_size = max_slice_size
        self.avail_grid = np.ones((rows, cols))
        self.ingridients = np.zeros((rows, cols))
        self.slices = []

    def __str__(self):
        print('TODO')

    def solve(self):
        """Solve this problem"""
        print('TODO')
        return


def read_file(file_path):
    """Read input file"""
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        header = lines[0]
        [rows, cols, min_num_ingridients, max_slice_size] = [int(x) for x in header.split(' ')]
        pizza = Pizza(rows, cols, min_num_ingridients, max_slice_size)
        # read ingridients
        for i, line in enumerate(lines[1:]):
            for j in range(cols):
                if line[j] == 'T':
                    pizza.ingridients[i, j] = 1
        return pizza

def write_file(pizza, filename):
    """Write output file."""
    with open(filename, 'w') as file_out:
        file_out.write('{}\n'.format(len(pizza.slices)))
        for cur_slice in pizza.slices:
            [start_row, end_row, start_col, end_col] = cur_slice
            file_out.write('{} {} {} {}\n'.format(start_row, start_col, end_row-1, end_col-1))


def main():
    """Main function."""

    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    # read data
    pizza = read_file(sys.argv[1])
    # write output file
    write_file(pizza, sys.argv[2])


if __name__ == '__main__':
    print('HASHCODE - TU_DUDES')
    print('running python {}'.format(sys.version_info.major))
    # main()

