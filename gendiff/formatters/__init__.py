from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json_formatter import format_json


def get_formatter(name):
    if name == 'stylish':
        return format_stylish
    elif name == 'plain':
        return format_plain
    elif name == 'json':
        return format_json
    else:
        raise ValueError(f"Unknown formatter: {name}")
