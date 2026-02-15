import os, re
from silence import silence
from types import SimpleNamespace

# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../lib")
# from font_utils import ...

silence()
import fontforge
silence(False)

def table(field_names, rows):
    if type(field_names) == list and type(rows) == list:
        strs = []
        max_lengths = [max([len(field_name), *[ len(row[field_name]) for row in rows ]]) for field_name in field_names]
        field_tuples = list(zip(max_lengths, field_names))
        strs.append(" | ".join([("%-*s" % (tuple[0], tuple[1])) for tuple in field_tuples]))
        strs.append("-|-".join([("-" * tuple[0]) for tuple in field_tuples]))
        for row in rows:
            strs.append(" | ".join(["%-*s" % (tuple[0], row[tuple[1]]) for tuple in field_tuples]))
        return "\n".join(strs)
    raise Exception("invalid arguments")

def table_keys(rows):
    field_names = []
    for row in list(rows):
        for key in row.keys():
            if key not in field_names:
                field_names.append(key)
    return field_names

def table_dict(rows):
    field_names = table_keys(rows)
    return table(field_names, rows)

def flatten(values):
    result = []
    for item in values:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def tsv_value_escape(str):
    str = str.replace("\\", "\\\\")
    str = str.replace("\t", "\\t")
    str = str.replace("\r", "\\r")
    str = str.replace("\n", "\\n")
    return str

# excel dialect
def csv_value_escape(str):
    if '"' not in str and ',' not in str and '\r' not in str and '\n' not in str:
        return str
    str = str.replace('"', '""')
    return '"' + str + '"'

def camel_case(str):
    str = re.sub(r'^[^A-Za-z0-9]+', '', str)
    str = re.sub(r'[^A-Za-z0-9]+$', '', str)
    str = re.sub(r'\'+', '', str)
    words = re.split(r'[^A-Za-z0-9]+', str)
    words = [words[i].lower() if i == 0 else words[i][0].upper() + words[i][1:] for i in range(0, len(words))]
    return "".join(words)

MAX_VERBOSE_SILENT = 2

def open_font(filename, verbose=False, flags=()):
    if verbose is None:
        verbose = False
    else:
        verbose = int(verbose)
    if verbose <= MAX_VERBOSE_SILENT:
        silence()
    try:
        if verbose:
            print("Opening %s" % filename)
        font = fontforge.open(filename, flags)
    except OSError as e:
        if e.args[0] != "Open failed":
            raise
        if verbose <= MAX_VERBOSE_SILENT:
            silence(False)
        return
    if verbose <= MAX_VERBOSE_SILENT:
        silence(False)
    return font

def u(codepoint):
    if codepoint < 0:
        return "%-8d" % codepoint
    return "U+%04X" % codepoint

def save_font(font, dest_filename, verbose=False):
    (_, ext) = os.path.splitext(dest_filename)
    if ext == '.sfd':
        if verbose:
            print("Saving %s" % dest_filename)
        font.save(dest_filename)
    else:
        if verbose:
            print("Generating %s" % dest_filename)
        font.generate(dest_filename)

def compute_dest_filename(source_filename, dest_filename, font_name=None):
    (source_dirname, source_basename) = os.path.split(source_filename)
    (source_basename_root, source_ext) = os.path.splitext(source_basename)
    if re.fullmatch(r'\.[^./]+', dest_filename):
        basename_root = font_name if font_name is not None else source_basename_root
        return os.path.join(source_filename, basename_root + dest_filename)
    if font_name is not None:
        if dest_filename.find('{}') >= 0:
            return dest_filename.replace("{}", font_name, 1)
        raise Exception("""\
When converting from font collection files, each destination filename must
either be an extension (e.g., '.ttf') or a filename containing at least one
occurrence of '{}' (e.g., '/home/xyz/{}.ttf')""")
    return dest_filename

is_silent = None

def fonts_in(filenames, close=True, verbose=0, ttc=True, open_font=True, names=False):
    if not open_font and not names:
        raise Exception("fonts_in without open_font or names does not make sense")
    global is_silent
    if is_silent is None:
        is_silent = verbose < 2
    for filename in filenames:
        fonts_in_file = fontforge.fontsInFile(filename)
        if (not ttc) and len(fonts_in_file) >= 2:
            raise Exception("fonts_in: .ttc files not supported when ttc=%s is specified" % repr(ttc))
        font_structs = []
        if len(fonts_in_file) < 2:
            font_structs = [SimpleNamespace(
                filename=filename,
                filename_open=filename,
                filename_noext=os.path.splitext(filename)[0],
                fontname=None,
                ttc=False,
            )]
        else:
            font_structs = [SimpleNamespace(
                filename=filename,
                filename_open="%s(%s)" % (filename, font_in_file),
                filename_noext="%s(%s)" % (os.path.splitext(filename)[0], font_in_file),
                fontname=font_in_file,
                ttc=True,
            ) for font_in_file in fonts_in_file]
        for font_struct in font_structs:
            if not open_font:
                yield font_struct
                continue
            try:
                if is_silent:
                    silence(True)
                print("Opening %s" % font_struct.filename_open)
                font = fontforge.open(font_struct.filename_open)
                print("Opened")
            except Exception as err:
                if is_silent:
                    silence(False)
                raise err
            if is_silent:
                silence(False)
            if names:
                if font_struct.fontname is None:
                    font_struct.fontname = font.fontname
                font_struct.font = font
                yield font_struct
            else:
                yield font
            if close:
                font.close()
