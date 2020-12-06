from django.apps import AppConfig
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField

class LokumAppConfig(AppConfig):
    name = 'lokum'

REPLACESYMB = [
    ('.', ''),
    (',', ''),
    (' ', '-'),
    ('?', ''),
    ('!', ''),
    (':', ''),
    (';', ''),
    ("/", '-'),
    ("\\", '-'),
    ('&', ''),
    ('"', ''),
    ("'", ''),
    ('#', ''),
    ('(', ''),
    (')', ''),
    ('*', ''),
]

ISO9PAIRS = [
    (u'А', u'a'),
    (u'Б', u'b'),
    (u'В', u'v'),
    (u'Г', u'g'),
    (u'Д', u'd'),
    (u'Е', u'e'),
    (u'Ё', u'yo'),
    (u'Ж', u'zh'),
    (u'З', u'z'),
    (u'И', u'i'),
    (u'Й', u'j'),
    (u'К', u'k'),
    (u'Л', u'l'),
    (u'М', u'm'),
    (u'Н', u'n'),
    (u'О', u'o'),
    (u'П', u'p'),
    (u'Р', u'r'),
    (u'С', u's'),
    (u'Т', u't'),
    (u'У', u'u'),
    (u'Ф', u'f'),
    (u'Х', u'h'),
    (u'Ц', u'c'),
    (u'Ч', u'ch'),
    (u'Ш', u'sh'),
    (u'Щ', u'csh'),
    (u'Ь', u''),
    (u'Ы', u'y'),
    (u'Ъ', u''),
    (u'Э', u'e'),
    (u'Ю', u'yu'),
    (u'Я', u'ya'),
    (u'І', u'i'),
    (u'Є', u'e'),
    (u'Ї', u'j'),
    (u'Ґ', u'g'),
    (u'а', u'a'),
    (u'б', u'b'),
    (u'в', u'v'),
    (u'г', u'g'),
    (u'д', u'd'),
    (u'е', u'e'),
    (u'ё', u'yo'),
    (u'ж', u'zh'),
    (u'з', u'z'),
    (u'и', u'i'),
    (u'й', u'j'),
    (u'к', u'k'),
    (u'л', u'l'),
    (u'м', u'm'),
    (u'н', u'n'),
    (u'о', u'o'),
    (u'п', u'p'),
    (u'р', u'r'),
    (u'с', u's'),
    (u'т', u't'),
    (u'у', u'u'),
    (u'ф', u'f'),
    (u'х', u'h'),
    (u'ц', u'c'),
    (u'ч', u'ch'),
    (u'ш', u'sh'),
    (u'щ', u'csh'),
    (u'ь', u''),
    (u'ы', u'y'),
    (u'ъ', u''),
    (u'э', u'e'),
    (u'ю', u'yu'),
    (u'я', u'ya'),
    (u'і', u'i'),
    (u'є', u'e'),
    (u'ї', u'j'),
    (u'ґ', u'g'),

]

def transliterate(str):
    """Transliterate str based on transpairs pairs of strings

    `str` is a unicode string to be parsed.
    `transpairs` is a list of 2-tuples containing character pairs
    There is no need to prepend `(?u)` to the first character in a character
    pair, as this is done for you by `transliterate()`.
    """
    for pair in REPLACESYMB:
        str = str.replace(pair[0], pair[1])

    for pair in ISO9PAIRS:
        str = str.replace(pair[0], pair[1])
    return str




