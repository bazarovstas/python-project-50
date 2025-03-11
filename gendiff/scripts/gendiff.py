#!/usr/bin/env python3

from gendiff.gendiff import generate_a_difference
from gendiff.cli import parse_arguments


def main():
    args = parse_arguments()

    print(generate_a_difference(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
