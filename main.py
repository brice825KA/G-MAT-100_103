#!/usr/bin/env python3

from Src.help import help

import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        help()
    elif len(sys.argv) != 4:
        print('Invalid number of arguments')
        sys.exit(0)


if __name__ == '__main__':
    main()