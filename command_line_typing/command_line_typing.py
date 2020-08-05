import time
from random import choice

from typing import List
from typing import Tuple

FILE_NAME = "phrases"


def load_practice_phrases() -> Tuple[List[str], List[str], List[str]]:
    """ Loads phrases from file and returns 3 lists (short, medium, long)"""
    short = []
    medium = []
    long = []
    size = ""
    with open(FILE_NAME, "r") as f:
        data = f.read()

    for line in data.splitlines():
        if line == "[SHORT]":
            size = "short"
        elif line == "[MEDIUM]":
            size = "medium"
        elif line == "[LONG]":
            size = "long"
        elif size == "short":
            short.append(line)
        elif size == "medium":
            medium.append(line)
        elif size == "long":
            long.append(line)

    return short, medium, long


def check_for_mistakes(practice_phrase: str, typed_phrase: str) -> int:
    # todo make this better
    practice_len = len(practice_phrase)
    typed_len = len(typed_phrase)
    error_count = 0
    for p, t in zip(practice_phrase, typed_phrase):
        if p != t:
            error_count += 1
    error_count += abs(practice_len - typed_len)
    return error_count


def practice(practice_phrase: str) -> None:
    print()
    print(practice_phrase)
    print()
    start_time = time.time()
    data = input()
    elapse_time = time.time() - start_time
    error_count = check_for_mistakes(practice_phrase, data)

    # calculate wpm
    adjusted_len = len(data) / 5
    gross_wpm = adjusted_len / (elapse_time / 60.0)
    net_wpm = (adjusted_len - error_count) / (elapse_time / 60.0)

    print()
    print("STATS:")
    print(f"Gross WPM: {gross_wpm:.1f}")
    print(f"Errors: {error_count}")
    print(f"Net WPM: {net_wpm:.1f}")
    print(f"Time: {elapse_time:.1f} seconds")


def main() -> int:
    short_phrases, medium_phrases, long_phrases = load_practice_phrases()
    practice(choice(short_phrases))
    return 0


if __name__ == "__main__":
    exit(main())
