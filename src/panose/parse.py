from .data import PANOSE_DATA

def parse_panose(panose):
    result = { }
    family_kind_digit = panose[0] # 2
    if family_kind_digit >= len(PANOSE_DATA):
        raise Exception("invalid first panose digit: %d" % family_kind_digit)
    family_kind_data = PANOSE_DATA[family_kind_digit]
    family_kind_name = family_kind_data["name"]
    result["family_kind"] = family_kind_name
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
