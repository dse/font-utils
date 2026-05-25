def parse_char(param, default=Exception, orig_param=None):
    if orig_param is None:
        orig_param = param
    kwargs = { "default": default, "orig_param": orig_param }
    if type(param) == int:
        if param not in range(0, 0x110000):
            if default is Exception:
                raise ValueError("invalid codepoint: %s" % repr(orig_param))
            return default
        return param
    if type(param) == float:
        if param != round(param):
            if default is Exception:
                raise ValueError("float codepoint must be integer: %s" % repr(orig_param))
            return default
        return parse_codepoint_argument(int(param), **kwargs)
    if type(param) == str:
        if len(str) == 1:
            return parse_codepoint_argument(ord(param), **kwargs)
        if len(str) == 2:
            hi = ord(str[0]) - 0xd800
            lo = ord(str[1]) - 0xdc00
            if hi in range(0, 0x0400) and lo in range(0, 0x0400):
                return 0x10000 + hi * 1024 + lo
        if re.fullmatch(r'uni[0-9a-f]{8}', param, re.IGNORECASE):
            if default is Exception:
                raise ValueError("character name stands for a ligature: %s" % repr(orig_param))
            return default
        if match := re.fullmatch(r'(?:u\+?|0?x)([0-9a-f]+)', param, re.IGNORECASE):
            return parse_codepoint_argument(int(match[1], 16), **kwargs)
        try:
            return unicodedata.lookup(param.upper())
        except ValueError:
            pass
        codepoint = fontforge.unicodeFromName(param)
        if codepoint in range(0, 0x110000):
            return parse_codepoint_argument(codepoint, **kwargs)
        if default is Exception:
            raise ValueError("invalid character name: %s" % repr(orig_param))
        return default
    if default is Exception:
        raise TypeError("invalid argument type, must be int, float, or str; got %s" % repr(type(param)))
    return default
