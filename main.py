#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Scores six original candidate roasts against the judge's five criteria
(weights 5/4/3/2/1, most important first) and writes the winner to
/output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first (weights 5..1):
# 1. Roasts a gadget/app people use every day.
# 2. Actually funny: the joke lands on a first read.
# 3. Fresh: an angle not seen before.
# 4. Neatly worded: tight, no wasted words, inside the limit.
# 5. One person's specific gripe, concrete detail of how it behaves.
WEIGHTS = (5, 4, 3, 2, 1)

CANDIDATES = [
    (
        "My printer only jams when the document matters \u2014 it has a "
        "sixth sense for deadlines and a vendetta against ink.",
        (5, 5, 5, 5, 5),
    ),
    (
        "My phone goes from 20% to dead in the time it takes to find a "
        "charger, like it is allergic to being saved.",
        (5, 4, 3, 4, 4),
    ),
    (
        "My smart TV remote has 47 buttons and I use exactly one \u2014 "
        "the one it hides under the couch.",
        (5, 4, 4, 4, 4),
    ),
    (
        "My laptop fan screams like a jet taking off every time I open a "
        "spreadsheet, as if maths were a runway.",
        (5, 4, 4, 3, 3),
    ),
    (
        "My phone's autocorrect has fixed my texts so many times my "
        "friends think I speak a different language.",
        (5, 3, 2, 4, 3),
    ),
    (
        "My earbuds die at 4% and spend their last breath announcing it, "
        "like a tiny drama queen with a battery.",
        (5, 4, 3, 3, 4),
    ),
]


def score(marks):
    """Weighted sum of the five criterion marks."""
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick(candidates):
    """Return the (line, total) with the highest score; ties go to the
    shorter line, then to the earlier candidate. Candidates outside the
    1-200 character gate are dropped before scoring, so a long line can
    never win on marks alone."""
    valid = [(line, marks) for line, marks in candidates
             if 1 <= len(line) <= 200 and line.strip()]
    assert valid, "no candidate passes the 1-200 character gate"
    best = None
    for line, marks in valid:
        total = score(marks)
        key = (total, -len(line))
        if best is None or key > best[0]:
            best = (key, line, total)
    return best[1], best[2]


def main():
    line, total = pick(CANDIDATES)
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"winner ({len(line)} chars, score {total}): {line}")


if __name__ == "__main__":
    main()
