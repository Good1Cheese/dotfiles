#!/usr/bin/env python3

# lf-keys.py - is the script that allows you to translate latin lf mapping
# to your non-latin keyboard layout (to allow all mappings to work as expected
# regardless of your current layout).

# USAGE
# grep '^map' lfrc | cat lf-defaults - | lf-keys.py
# paste the output below all your mappings in lfrc

# NOTE you will need a file with deafult lf bindings (for hjkl etc...)

from sys import stdin
import re

# maketrans - creates dictionary to translate characters in first line (as keys)
# to characters in second (values)
translists = [
    str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;,'.`",
        "ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯфисвуапршолдьтщзйкыегмцчняжбэюё"
    ),
    # e.g. above is latin >>> cyrillic
    # this will allow lf to interpret Ф as A, ф as a, etc
    # if you want to use more that one alternative layout -
    # put another maketrans here
    # e.g.
    # str.maketrans(
    #     "l", # etc
    #     "م"
    # )
]

def trans(s, translist, inv_translist):
    s = s.translate(translist)

    if re.search('<.-.>', s, flags=re.IGNORECASE):
        # fix ctrl, alt, and f1...
        for char in ['c', 'a', 'f']:
            mp = f'<{char}-'
            mpa = mp.translate(translist)
            s = s.replace(mpa, mp)

    if special := re.findall(r'<\w+>', s, re.IGNORECASE):
        for w in special:
            untrans = w.translate(inv_translist)
            s = s.replace(w, untrans)

    return s


if __name__ == '__main__':
    lines = [line.strip() for line in stdin.readlines()]

    # skip comments
    lines = filter(lambda line:
                        line != '' and
                        not re.match(r'^\s*#', line),
                        lines)

    lines = list(lines)

    unmapped = set()
    for line in lines:
        words = line.split()
        if len(words) == 2:
            unmapped.add(words[1])

    for translist in translists:
        inv_translist = {v: k for k, v in translist.items()}

        for line in lines:
            words = line.split()

            # don't translate unmapped defaults, <enter>...
            keys = words[1]
            if keys not in unmapped and not re.match(r'<\w+>', keys):
                cmd = f'push {keys}'
                new_keys = trans(keys, translist, inv_translist)

                if new_keys == keys:
                    continue

                print(' '.join(['map', f'"{new_keys}"', cmd]))
