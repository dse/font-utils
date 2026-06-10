#!/usr/bin/env -S fontforge -quiet -lang=py -script
import os, sys, re

progname = os.path.basename(sys.argv[0]).split(".")[0]
if progname == "bdftool":
    raise Exception("not expected to be invoked as pdftool")

def main():
    for [fh, filename] in magic_filehandle():
        process_bdf_from_fh(fh, filename)

def process_bdf_from_fh(fh, filename):
    line_number = 0
    reading_bitmap = 0
    y = None
    bbx_width = None
    bbx_height = None
    bbx_ofs_x = None
    bbx_ofs_y = None
    encoding_line_printed = False
    try:
        for line in fh:
            line_number += 1
            [keyword, *params] = parse_line(line)
            keyword = keyword.upper()

            line = line.strip() # removes ALL leading AND trailing whitespace

            if reading_bitmap:
                if keyword in ["ENDCHAR", "STARTCHAR", "ENDFONT", "ENCODING"]:
                    reading_bitmap = 0
                elif re.match(r'[|+^]', line):
                    if progname == "bdfhex":
                        line = to_hex(line)
                    y -= 1
                    continue
                elif re.fullmatch(r'[0-9a-f]+', line, flags=re.I):
                    if progname == "bdfpx":
                        line = to_px(line)[0:bbx_width]
                        if y == 0:
                            line = "^" + line + "^"
                        else:
                            line = "|" + line + "|"
                    y -= 1
                    continue
                else:
                    reading_bitmap = 0

            encoding_line = None
            if progname == "bdfcharname" and keyword == "STARTCHAR":
                charname = params[0]
                enc = None
                if match := re.fullmatch(r'(?:u\+?|0?x)([0-9a-f]+)', charname, re.I):
                    enc = int(match[1], 16)
                else:
                    enc = fontforge.unicodeFromName(charname)
                if enc is not None:
                    if enc in range(0, 0x110000):
                        line = "STARTCHAR " + fontforge.nameFromUnicode(enc)
                        encoding_line = "ENCODING %d" % enc

            if progname == "bdfcharname":
                if keyword == "ENCODING" and encoding_line_printed:
                    encoding_line_printed = False
                    continue

            print(line)

            if progname == "bdfcharname":
                if keyword == "STARTCHAR" and encoding_line is not None:
                    print(encoding_line)
                    encoding_line_printed = True

            if re.match(r'(bitmap)(?:$|\s)', line, flags=re.I):
                reading_bitmap = 1
                continue
            elif match := re.match(r'bbx\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)(?:$|\s)', line, re.I):
                bbx_width = int(match[1])
                bbx_height = int(match[2])
                bbx_ofs_x = int(match[3])
                bbx_ofs_y = int(match[4])
                y = bbx_height + bbx_ofs_y - 1
            elif re.match(r'(endchar|startchar|endfont|encoding)(?:$|\s)', line, flags=re.I):
                bbx_width = None
                bbx_height = None
                bbx_ofs_x = None
                bbx_ofs_y = None

    except BDFSyntaxError as err:
        print("%s line %s: %s" % (filename, line_number, err.details), file=sys.stderr)
        exit(1)

def to_hex(px_str):
    px_str = px_str.strip("|^+")
    bits = 0
    byte = 0
    hex_str = ""
    for px in px_str:
        bit = 1 if re.search(r'\S', px) else 0
        byte = (byte << 1) | bit
        bits += 1
        if bits == 8:
            hex_str += "%02X" % byte
            bits = 0
            byte = 0
    if bits:
        byte = byte << (8 - bits)
        hex_str += "%02X" % byte
    return hex_str

def to_px(hex_str):
    bin_str = ""
    for nybble in hex_str:
        digit = int(nybble, 16)
        binary = bin(digit)[2:]
        binary = ("0" * ((4 - len(binary)) % 4)) + binary
        bin_str += binary
    bin_str += "0" * ((2 - len(bin_str)) % 2)
    bin_str = bin_str.replace("0", " ").replace("1", "#")
    return bin_str

def magic_filehandle():
    if len(sys.argv) < 2:
        yield [sys.stdin, "<stdin>"]
        return
    for filename in sys.argv[1:]:
        with open(filename, "r", encoding="utf-8") as fh:
            yield [fh, filename]

def parse_line(line):
    orig_line = line
    line = line.strip()
    words = []
    while True:
        line = line.lstrip()
        if line == "":
            break
        word = None
        while True:
            suffix = None
            if match := re.match(r'[^" \t]+', line):
                substr = match[0]
                line = line[match.end():]
            elif match := re.match(r'"(?:""|[^"]+)*"', line):
                substr = match[0][1:-1].replace('""', '"')
                line = line[match.end():]
            elif line == "" or (match := re.match(r'[ \t]', line)):
                break
            else:
                idx = len(orig_line) - len(line)
                printed_line = orig_line[0:idx] + "<HERE>" + orig_line[idx:]
                if line[0] == '"':
                    raise BDFSyntaxError("unterminated quoted string starting <HERE>", printed_line)
                else:
                    raise BDFSyntaxError("malformed line starting <HERE>", printed_line)
            if word is None:
                word = substr
            else:
                word += substr
        if word is not None:
            words.append(word)
            if len(words) == 1 and word.upper() == "COMMENT":
                if re.match(r'\s', line):
                    line = line[1:]
                return [word, line]
    return words

class BDFSyntaxError(Exception):
    def __init__(self, message, details):
        self.details = details
        super().__init__(message)
    pass

# print(repr(parse_line("comment lkdsfj lskjdf lksdfj lksdfjlkf jsdklf ")))
# print(repr(parse_line("comment  lkdsfj lskjdf lksdfj lksdfjlkf jsdklf ")))
# print(repr(parse_line("bbx 1 2 -3 -4")))
# print(repr(parse_line("bbx 1 2 -3 -4 ")))
# print(repr(parse_line("font \"lksdj flkj \"\"fdlkfj lkj fdfs\"  \"")))
# exit()

main()
