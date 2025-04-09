import json


def read_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = []
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(f"  {key}: {data1[key]}")
            else:
                result.append(f"- {key}: {data1[key]}")
                result.append(f"+ {key}: {data2[key]}")
        elif key in data1:
            result.append(f"- {key}: {data1[key]}")
        elif key in data2:
            result.append(f"+ {key}: {data2[key]}")

    return "\n".join(result)
