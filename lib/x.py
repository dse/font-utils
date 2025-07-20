import re

from font_panose_data import PANOSE

def upper_snake_case(str):
    str = str.upper()
    str = re.sub(r'\'', '', str)
    str = re.sub(r'^[^0-9A-Za-z]+', '', str)
    str = re.sub(r'[^0-9A-Za-z]+$', '', str)
    str = re.sub(r'[^0-9A-Za-z]+', '_', str)

    str = re.sub('^ASPECT_RATIO_OF_CHARACTER_', 'ASPECT_RATIO_CHAR_', str)
    return str

for (index, data) in enumerate(PANOSE):
    FAMILY_KIND_NAME = upper_snake_case(data["name"])
    print("FAMILY_KIND_%s = %d" % (FAMILY_KIND_NAME, index))
print()

for (index, data) in enumerate(PANOSE):
    FAMILY_KIND_NAME = upper_snake_case(data["name"])
    if "sub_digits_data" not in data:
        continue
    for (index2, data2) in enumerate(data["sub_digits_data"]):
        FIELD_NAME = upper_snake_case(re.sub(r' \(.*\)$', '', data2["name"]))
        print("%s__%s = %d" % (FAMILY_KIND_NAME, FIELD_NAME, index2))
    print()

    for (index2, data2) in enumerate(data["sub_digits_data"]):
        FIELD_NAME = upper_snake_case(re.sub(r' \(.*\)$', '', data2["name"]))
        if "values" not in data2:
            continue
        for (index3, data3) in enumerate(data2["values"]):
            if data3 is None:
                continue
            VALUE_NAME = upper_snake_case(data3["name"])
            print("%s__%s__%s = %d" % (FAMILY_KIND_NAME, FIELD_NAME, VALUE_NAME, index3))
        print()
