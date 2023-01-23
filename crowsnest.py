#!/usr/bin/env python3
"""
Author : Sopuruchi Chisom
Purpose: Choose an article(Ship warning call)
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Choose an article(Ship warning call)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("object", metavar="object", help="The object in sea", type=str)

    parser.add_argument(
        "-s",
        "--side",
        metavar="side",
        help="The side of the ship where the object was spotted",
        default="larboard",
    )

    return parser.parse_args()


def helper_function(args):
    """This function prints the call-out message to the captain using the appropriate article"""

    object_in_sea = args.object
    side_of_ship = args.side
    vowels = ["a", "e", "i", "o", "u"]
    article = ""

    if not object_in_sea[0].isalpha():
        print("ERROR: Items at sea must start with a letter")
        return

    if object_in_sea[0].islower():
        article = "an" if object_in_sea[0].lower() in vowels else "a"
    else:
        article = "An" if object_in_sea[0].lower() in vowels else "A"

    print(f"Ahoy, Captain, {article} {object_in_sea} off the {side_of_ship} bow!")


def main():
    """Make a triumphant noise here"""

    args = get_args()
    helper_function(args)


if __name__ == "__main__":
    main()
