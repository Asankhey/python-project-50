import json
import yaml
import os


def read_data(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath) as file:
        if ext in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError(f'Unsupported file format: {ext}')


def generate_diff(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
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
