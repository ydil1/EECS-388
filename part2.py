#!/usr/bin/env python3

def sha_256(b: bytes) -> bytes:
    return


# Feel free to edit the main function however you like to help you debug, it won't be graded
#
# Run this script with the command: python3 part2.py
# or select "Part 2" from the VS Code debugger
def main():
    digest = sha_256(b'Hello, world!')
    print(digest)


if __name__ == '__main__':
    main()
