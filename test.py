#!usr/bin/env python3
""" tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Captain, {} {} off the larboard bow!"


def test_exists():
    """exists"""
    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


def test_consonant():
    """brigantine -> a brigantine"""
    for word in consonant_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("a", word)


def test_consonant_upper():
    """Brigantine -> a Brigantine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("A", word.title())


def test_vowel():
    """aviso -> an aviso"""
    for word in vowel_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("an", word)


def test_vowel_upper():
    """Aviso -> an Aviso"""
    for word in vowel_words:
        out = getoutput(f"{prg} {word.upper()}")
        assert out.strip() == template.format("An", word.upper())


def test_input():
    """ "test for input"""

    for side_docked in ["starboard", "deck"]:
        for option in ["-s", "--side"]:
            rv, out = getstatusoutput(f"{prg} object {option} {side_docked}")
            assert rv == 0
            assert out.strip().endswith(f"{side_docked} bow!")


def test_starts_with_alphabet():
    """test for non inputs that do not start with alphabetic characters"""

    for word in ["7up", "$$%spoon", ".!##**#"]:
        rv, out = getstatusoutput(f"{prg} {word}")
        assert rv == 0
        assert out.strip().startswith("ERROR")
