from font_panose_data import PANOSE
from font_utils import camel_case
def expand_panose(panose, camel=False):
    result = { }
    family_kind_digit = panose[0] # 2
    if family_kind_digit >= len(PANOSE):
        raise Exception("invalid first panose digit: %d" % family_kind_digit)
    family_kind_data = PANOSE[family_kind_digit]
    family_kind_name = family_kind_data["name"]
    if camel:
        result["familyKind"] = family_kind_name
    else:
        result["Family Kind"] = family_kind_name
    if family_kind_digit in [0, 1]:
        return result
    if "sub_digits_data" not in family_kind_data:
        return result
    sub_digits_data = family_kind_data["sub_digits_data"]
    for sub_digit_index in range(1, 10):
        sub_digit_value = panose[sub_digit_index]
        sub_digit_data = sub_digits_data[sub_digit_index]
        if "name" not in sub_digit_data:
            continue
        data_name = sub_digit_data["name"]
        if camel:
            data_name = camel_case(data_name)
        result[data_name] = sub_digit_value # fallback
        if "values" not in sub_digit_data:
            continue
        data_values = sub_digit_data["values"]
        if sub_digit_value >= len(data_values):
            continue
        value_data = data_values[sub_digit_value]
        if "name" not in value_data:
            continue
        value_name = value_data["name"]
        result[data_name] = value_name
    return result
