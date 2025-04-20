INDENT = "    "
SIGN_OFFSET = 2


def stringify(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()
        if value is None:
            return "null"
        return str(value)

    indent = INDENT * (depth + 1)
    lines = [
        f"{indent}{key}: {stringify(val, depth + 1)}"
        for key, val in value.items()
    ]
    result = "\n".join(lines)
    closing_indent = INDENT * depth
    return f"{{\n{result}\n{closing_indent}}}"


def format_node(key, value, sign, depth):
    indent = INDENT * depth
    sign_indent = indent[:-SIGN_OFFSET]
    return f"{sign_indent}{sign} {key}: {stringify(value, depth)}"


def iter_(node, depth):
    lines = []

    for item in node:
        key = item["key"]
        node_type = item["type"]

        if node_type == "nested":
            children = iter_(item["children"], depth + 1)
            lines.append(f"{INDENT * depth}{key}: {{\n{children}\n{INDENT * depth}}}")
        elif node_type == "added":
            lines.append(format_node(key, item["value"], "+", depth))
        elif node_type == "removed":
            lines.append(format_node(key, item["value"], "-", depth))
        elif node_type == "changed":
            lines.append(format_node(key, item["old_value"], "-", depth))
            lines.append(format_node(key, item["new_value"], "+", depth))
        elif node_type == "unchanged":
            lines.append(format_node(key, item["value"], " ", depth))

    return "\n".join(lines)


def format_stylish(tree):
    return f"{{\n{iter_(tree, 1)}\n}}"
