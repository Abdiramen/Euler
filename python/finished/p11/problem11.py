#!/usr/bin/env python3

import argparse
import numpy as np

from functools import reduce


def iterativeSolver(npData):
    result = 0
    for y in range(len(npData)):
        for x in range(len(npData[y])):
            for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                prod, coord = npData[y][x], (y, x)
                for i in range(1, 4):
                    coord = coord[0] + direction[0], coord[1] + direction[1]
                    if coord[0] >= len(npData) or \
                       coord[0] < 0 or \
                       coord[1] >= len(npData[y]) or \
                       coord[1] < 0:
                        prod = 0
                        break
                    else:
                        print(coord, npData[coord[0]][coord[1]])
                        prod *= npData[coord[0]][coord[1]]
                if prod > result:
                    result = prod
                print(result)
                print("____")
    return result


def functionalSolver(grid):
    return max(
        [
            (
                reduce(
                    (lambda a, b: a*b),
                    [
                        grid[y + n*direction[0]][x + n*direction[1]]
                        for n in range(4) if y + n*direction[0] < len(grid)
                        and y+n*direction[0] >= 0
                        and x+n*direction[1] < len(grid[y])
                        and x+n*direction[1] >= 0
                    ]
                )
            )
            for y in range(len(grid))
            for x in range(len(grid[y]))
            for direction in ((0, 1), (1, 0), (1, 1), (1, -1))])


def solve(dataFile):
    data = np.loadtxt(dataFile, dtype=int)
    print(functionalSolver(data))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        help='NxN grid of ints',
        required=True
    )
    args = parser.parse_args()

    solve(args.file)


if __name__ == "__main__":
    main()
