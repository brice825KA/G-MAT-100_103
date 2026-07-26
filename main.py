#!/usr/bin/env python3

from Src.help import help
from Src.LoopShell import LoopShell

import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        help()
    elif len(sys.argv) == 2 and sys.argv[1] == '-S':
        LoopShell()
    else:
        print('Invalid number of arguments')
        sys.exit(0)
    sys.exit(0)


if __name__ == '__main__':
    main()