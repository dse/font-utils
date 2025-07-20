__all__ = [
    "fsTypeData",
    "fontFamilyClassData",
    "unicodeRangeData",
    "macStyleData",
]

from os2_data import \
    OS2_WIDTH_CLASS_NAMES, \
    OS2_WEIGHT_CLASS_NAMES, \
    OS2_FS_TYPE_VALUES, \
    IBM_FONT_FAMILY_CLASSES, \
    IBM_FONT_FAMILY_SUBCLASSES, \
    UNICODE_RANGES

def fsTypeData(fsTypeNumber):
    data = {}
    usagePermissions = fsTypeNumber & 0x0f
    if usagePermissions == 0:
        data["usagePermissions"] = "installable"
    elif usagePermissions == 2:
        data["usagePermissions"] = "restrictedLicense"
    elif usagePermissions == 4:
        data["usagePermissions"] = "previewAndPrint"
    elif usagePermissions == 8:
        data["usagePermissions"] = "editable"
        data["noSubsetting"]        = bool(fsTypeNumber & (1 << 8))
        data["bitmapEmbeddingOnly"] = bool(fsTypeNumber & (1 << 9))
    return data

def fontFamilyClassData(familyClassNumber):
    data = {}
    fontClassNumeric    = familyClassNumber >> 8
    fontSubclassNumeric = familyClassNumber & 0xff;

    data["classNumeric"] = fontClassNumeric
    data["subclassNumeric"] = fontSubclassNumeric

    if fontClassNumeric in IBM_FONT_FAMILY_CLASSES:
        fontClass = IBM_FONT_FAMILY_CLASSES[fontClassNumeric]
        if fontClass is not None:
            data["class"] = fontClass
            if fontClassNumeric in IBM_FONT_FAMILY_SUBCLASSES[fontClassNumeric]:
                fontSubclass = IBM_FONT_FAMILY_SUBCLASSES[fontClassNumeric][fontClassNumeric]
                data["subclass"] = fontSubclass
    return data

def unicodeRangeData(unicodeRanges):
    unicodeRanges = list(unicodeRanges)
    unicodeRanges = [value + 4294967296 if value < 0 else value  for  value in unicodeRanges]
    ranges = []
    for bit in range(0, len(UNICODE_RANGES)):
        idx1 = int(bit/32)
        idx2 = bit % 32
        if idx1 >= 4:
            continue
        if unicodeRanges[idx1] & (1 << idx2):
            for r in UNICODE_RANGES[bit]:
                ranges.append(r)
    return ranges

def macStyleData(macStyleNumeric):
    data = {
        "bold":        bool(macStyleNumeric & 0x01),
        "italic":      bool(macStyleNumeric & 0x02),
        "underline":   bool(macStyleNumeric & 0x04),
        "outline":     bool(macStyleNumeric & 0x08),
        "shadow":      bool(macStyleNumeric & 0x10),
        "condensed":   bool(macStyleNumeric & 0x20),
        "extended":    bool(macStyleNumeric & 0x40),
        "reservedBit": bool(macStyleNumeric & 0x80),
    }
    return data
