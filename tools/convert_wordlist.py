"""Convert a Church translation word list (.rtf) into the format the translate skill searches.

Input layout (one entry per block):
    ENGLISH TERM Graphic
    French terme français Note optional note

Usage:
    pip install striprtf
    python tools/convert_wordlist.py French_140_wordlist1.rtf ~/.claude/skills/translate/wordlist-140.md

Entries with no French line are marked "(same word in French)": the same word is used in both languages.
Some source files merge two headwords into one block ("See: ..." lines); review those by hand.
"""
import re
import sys

from striprtf.striprtf import rtf_to_text


def parse(text):
    rows, eng = [], None

    def flush():
        nonlocal eng
        if eng is not None:
            rows.append([eng, "", ""])
            eng = None

    for s in (line.strip() for line in text.splitlines()):
        if not s or (len(s) == 1 and s.isalpha() and s.isupper()):
            continue  # blank line or A-Z section letter
        tagged = re.match(r"^<(\w+)>(.*)$", s)
        if tagged and rows and eng is None:
            # Extra line for the previous entry: "<Frenhc>adorer", "<source>(es 8:3)", "<Classword>verb"
            tag, val = tagged.group(1).lower(), tagged.group(2).strip()
            if tag in ("source", "classword", "wordclass"):
                rows[-1][2] = f"{rows[-1][2]} [{tag}: {val}]".strip()
            else:
                rows[-1][1] = f"{rows[-1][1]} ; {val}".strip(" ;")
            continue
        if s.startswith("See:"):
            rest = re.sub(r"\s*Graphic\s*$", "", s[4:]).strip()
            if ">" in rest:  # "See: ASSISTANT>aide-bibliothécaire" under LIBRARY
                part, fr = rest.split(">", 1)
                base = eng or rows[-1][0]
                flush()
                rows.append([f"{base} {part.strip()}", fr.strip(), ""])
            elif eng is not None and rest:
                eng = f"{eng} (see: {rest})"
            continue
        if s.startswith("French"):
            fr, note = s[6:].strip(), ""
            m = re.search(r"\bNote\b", fr)
            if m:
                fr, note = fr[: m.start()].strip(), fr[m.end():].strip()
            if eng is not None:
                rows.append([eng, fr, note])
                eng = None
            continue
        flush()
        eng = re.sub(r"\s*Graphic\s*$", "", s)
    flush()

    for row in rows:
        if not row[1]:
            row[1] = row[0]
            row[2] = f"(same word in French) {row[2]}".strip()
    return rows


def main(src, dest):
    with open(src, encoding="cp1252", errors="ignore") as f:
        rows = parse(rtf_to_text(f.read()))
    esc = lambda x: x.replace("|", "/")
    with open(dest, "w", encoding="utf-8") as f:
        f.write("# Official Church terminology word list (English → French)\n\n")
        f.write("One entry per line: `English | French | Note`.\n")
        f.write("Hymn entries end with hymn numbers (English hymnbook # → French *Cantiques* #).\n")
        f.write('Where the source gives no French, the same word is used in both languages (marked "(same word in French)").\n')
        f.write("Search with Grep (case-insensitive) rather than reading the whole file.\n\n")
        for eng, fr, note in rows:
            f.write(f"{esc(eng)} | {esc(fr)} | {esc(note)}".rstrip(" |") + "\n")
    print(f"{len(rows)} entries written to {dest}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
