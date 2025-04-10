SPACES_COUNT = 4
INDENT = ' '


def stringify(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = INDENT * (depth * SPACES_COUNT)
        closing_indent = INDENT * ((depth - 1) * SPACES_COUNT)
        for key, val in sorted(value.items()):
            lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=1):
    lines = []
    indent_size = depth * SPACES_COUNT
    current_indent = INDENT * (indent_size - 2)
    closing_indent = INDENT * ((depth - 1) * SPACES_COUNT)

    for key in sorted(diff.keys()):
        status, *values = diff[key]
        if status == 'added':
            lines.append(f"{current_indent}+ {key}: {stringify(values[0], depth)}")
        elif status == 'removed':
            lines.append(f"{current_indent}- {key}: {stringify(values[0], depth)}")
        elif status == 'unchanged':
            lines.append(f"{current_indent}  {key}: {stringify(values[0], depth)}")
        elif status == 'updated':
            lines.append(f"{current_indent}- {key}: {stringify(values[0], depth)}")
            lines.append(f"{current_indent}+ {key}: {stringify(values[1], depth)}")
        elif status == 'nested':
            nested = format_stylish(values[0], depth + 1)
            lines.append(f"{current_indent}  {key}: {nested}")

    return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"