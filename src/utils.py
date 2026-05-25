from .parse import parse_char

def uplus(codepoint):
    if codepoint not in range(0, 0x110000):
        return "%d" % codepoint
    return "U+%04X" % codepoint

def create_char(font, param):
    """
    Convenience function.

    for glyph in create_char(0x1f4a9):
        ...
    """
    codepoint = parse_char(param)
    glyph = font.createChar(codepoint)
    glyph.clear()
    return [g]

def get_fonts_from(filenames, with_filenames=False, ttc=True):
    for filename in filenames:
        fonts_in_file = fontforge.fontsInFile(filename)
        if len(fonts_in_file) < 2:
            try:
                silence.on()
                font = fontforge.open(filename)
                silence.off()
            except:
                silence.off()
                raise
            if with_filenames:
                yield [font, filename, filename]
            else:
                yield font
            font.close()
        elif not ttc:
            raise Exception("get_fonts_from: this call instructed to not open .ttc files")
        else:
            for font_in_file in fonts_in_file:
                try:
                    silence.on()
                    font = fontforge.open(font_in_file)
                    silence.off()
                except:
                    silence.off()
                    raise
                if with_filenames:
                    yield [font, filename, font_in_file]
                else:
                    yield font
                font.close()

def get_base_codepoint(param, default=None):
    base_glyphname = None
    if type(param) == fontforge.glyph:
        if param.unicode in range(0, 0x110000):
            return param.unicode
        base_glyphname = param.glyphname.split(".")[0]
    elif type(param) == str:
        base_glyphname = str.split(".")[0]
    codepoint = fontforge.unicodeFromName(base_glyphname)
    if codepoint < 0:
        return default
    return codepoint

def get_base_glyphname(param, default=None):
    codepoint = get_base_codepoint(param, default=None)
    if codepoint is None:
        return default
    return fontforge.nameFromUnicode(codepoint)

def get_variant_name(glyph):
    splitz = glyph.glyphname.split(".", 1)
    if len(splitz) > 1:
        return splitz[1]
    return None
