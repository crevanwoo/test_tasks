#!/usr/bin/env python3

import argparse

from termcolor import cprint

print('Set matrix size by passing --columns and --rows parameters. To see other options use --help.')

parser = argparse.ArgumentParser()
parser.add_argument("--columns", "-c", help="set columns amount")
parser.add_argument("--rows", "-r", help="set rows amount")
parser.add_argument(
    "--show", "-s", help="show final matrix", action="store_true")
args = parser.parse_args()


def set_offset(line, offt):
    if line == 3 or not (line - 3) % 4:
        return offt + 1
    return offt


def set_color(line, colors):
    colors_amount = len(colors)
    idx = line % colors_amount
    return colors[idx]


def set_range(is_dir, start, end):
    if is_dir:
        return range(start, end)
    return reversed(range(start, end))


def process_cell(matrix, row, col, c_left, line):
    pcolors = ['green', 'yellow', 'blue', 'magenta', 'cyan', 'red']
    text = str(row) + ' ' + str(col)
    matrix[row][col] = text
    cprint(text, set_color(line, pcolors))
    return c_left - 1


def run_snail(rows, cols):
    cells = rows * cols
    cells_left = cells

    matrix = []

    for item in range(rows):
        row = []
        for col in range(cols):
            row.append(False)
        matrix.append(row)

    is_direct = True
    offset = 0
    line_count = 0

    x = 0
    y = 0

    while cells_left > 0:
        if is_direct:
            offset = set_offset(line_count, offset)
            for y in set_range(is_direct, y, (cols - offset)):
                cells_left = process_cell(matrix, x, y, cells_left, line_count)
            line_count = line_count + 1
            x = x + 1

            offset = set_offset(line_count, offset)
            for x in set_range(is_direct, x, (rows - offset)):
                cells_left = process_cell(matrix, x, y, cells_left, line_count)
            line_count = line_count + 1
        else:
            offset = set_offset(line_count, offset)
            for y in set_range(is_direct, offset, y):
                cells_left = process_cell(matrix, x, y, cells_left, line_count)
            line_count = line_count + 1

            offset = set_offset(line_count, offset)
            for x in set_range(is_direct, offset, x):
                cells_left = process_cell(matrix, x, y, cells_left, line_count)
            line_count = line_count + 1
            y = y + 1

        is_direct = not is_direct

    return matrix


if args.columns and args.rows:
    print("Matrix size: {0} x {1}".format(args.columns, args.rows))
    cols = int(args.columns)
    rows = int(args.rows)

    matrix = run_snail(rows=rows, cols=cols)

    if args.show:
        for row in matrix:
            print(row)
