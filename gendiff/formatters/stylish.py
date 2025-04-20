INDENT = "    "
OFFSET = 2


def stringify(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            line = f"{INDENT * (depth + 1)}{key}: {stringify(val, depth + 1)}"
            lines.append(line)
        result = "\n".join(lines)
        return f"{{\n{result}\n{INDENT * depth}}}"

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_node(key, value, sign, depth):
    sign_indent = INDENT * depth
    sign_indent = sign_indent[:-OFFSET]
    return f"{sign_indent}{sign} {key}: {stringify(value, depth)}"


def format_stylish(diff, depth=1):
    lines = []

    for key in sorted(diff.keys()):
        node_type, data = diff[key]

        if node_type == "nested":
            children = format_stylish(data, depth + 1)
            lines.append(f"{INDENT * depth}{key}: {children}")
        elif node_type == "added":
            lines.append(format_node(key, data, "+", depth))
        elif node_type == "removed":
            lines.append(format_node(key, data, "-", depth))
        elif node_type == "changed":
            old, new = data
            lines.append(format_node(key, old, "-", depth))
            lines.append(format_node(key, new, "+", depth))
        elif node_type == "unchanged":
            lines.append(format_node(key, data, " ", depth))

    result = "\n".join(lines)
    return f"{{\n{result}\n{INDENT * (depth - 1)}}}"
