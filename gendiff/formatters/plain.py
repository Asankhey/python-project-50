def format_plain(diff, path=""):
    lines = []

    def to_str(value):
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, bool):
            return str(value).lower()
        if value is None:
            return 'null'
        if isinstance(value, str):
            return f"'{value}'"
        return str(value)

    for key in sorted(diff.keys()):
        status, *values = diff[key]
        property_path = f"{path}.{key}" if path else key

        if status == 'nested':
            lines.append(format_plain(values[0], property_path))
        elif status == 'added':
            value = to_str(values[0])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif status == 'updated':
            old = to_str(values[0])
            new = to_str(values[1])
            lines.append(f"Property '{property_path}' was updated. From {old} to {new}")

    return '\n'.join(lines)