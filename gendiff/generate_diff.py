import json
import yaml
import os
from gendiff.formatters import get_formatter


def read_data(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath) as file:
        if ext in ['.yaml', '.yml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError(f'Unsupported file format: {ext}')


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}
    for key in keys:
        if key in data1 and key in data2:
            val1 = data1[key]
            val2 = data2[key]
            if isinstance(val1, dict) and isinstance(val2, dict):
                diff[key] = ('nested', build_diff(val1, val2))
            elif val1 == val2:
                diff[key] = ('unchanged', val1)
            else:
                diff[key] = ('updated', val1, val2)
        elif key in data1:
            diff[key] = ('removed', data1[key])
        elif key in data2:
            diff[key] = ('added', data2[key])
    return diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file_path1 = os.path.abspath(file_path1)
    file_path2 = os.path.abspath(file_path2)
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    diff = build_diff(data1, data2)
    formatter_func = get_formatter(formatter)
    return formatter_func(diff)