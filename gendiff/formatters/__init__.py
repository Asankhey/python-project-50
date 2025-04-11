from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def get_formatter(name):
    if name == 'stylish':
        return format_stylish
    elif name == 'plain':
        return format_plain
    else:
        raise ValueError(f"Unknown formatter: {name}")